# Decoding Currency Dynamics — Hybrid CNN-LSTM-Transformer FX Forecasting

M.Tech dissertation project (BITS Pilani WILP). A complete, runnable, tested
system that forecasts **XAU/USD, XAG/USD and EUR/USD at hourly (H1)
resolution**, fusing price, macroeconomic and FinBERT news-sentiment streams in
a 4.4-million-parameter dual-tower network with trust-gated econometric
experts — and, more importantly, an evaluation protocol under which every
directional claim is measured against the base rate of the same bars.

## Headline findings

**Direction is not forecastable at H1.** Across three instruments, three seeds
and roughly fifteen alternative framings, no configuration exceeded its own
always-up base rate.

| Instrument | Hybrid | GARCH | ARIMA | Base rate | Edge |
|---|---|---|---|---|---|
| Gold (XAU/USD) | 0.5178 | 0.5378 | 0.5063 | 0.5344 | **−1.7 pp** |
| Silver (XAG/USD) | 0.5145 | 0.5237 | 0.4925 | 0.5354 | **−2.1 pp** |
| Euro (EUR/USD) | 0.4984 | 0.5044 | 0.4875 | 0.5037 | **−0.5 pp** |

Read the **edge**, not the accuracy. Directional accuracy is uninterpretable
without the unconditional base rate of the test window: if an instrument rises
in 53.44% of bars, a rule that ignores its inputs entirely and always predicts
"up" scores 0.5344. Seed dispersion is 0.0005–0.0018, one to two orders of
magnitude smaller than the gap to the base rate — this is a stable finding, not
a bad training run.

**Move magnitude is forecastable.** The same model, the same features, the same
bars and the same protocol beat both volatility baselines on rank skill and
large-move classification, on all three instruments and every seed.

| Instrument | Spearman: Hybrid / ATR% / GARCH-σ | Large-move acc.: Hybrid vs base |
|---|---|---|
| Gold | 0.3288 / 0.3086 / 0.3043 | 0.5517 vs 0.5046 |
| Silver | 0.4178 / 0.3771 / 0.3463 | 0.5520 vs 0.5119 |
| Euro | 0.2316 / 0.0894 / 0.1453 | 0.5709 vs 0.4969 |

Significance is reported honestly: on gold all four bootstrap intervals contain
zero, while silver's and euro's eight all exclude it. Diebold–Mariano and the
Hansen MCS operate on squared-error loss — not the quantity claimed — and
separate nothing anywhere; all DM statistics favour the hybrid but none reach
significance, and that is reported rather than omitted.

**Calibrated uncertainty is the most deployable result.** The Gaussian head is
badly over-confident; adaptive conformal inference restores nominal coverage
where split conformal fails.

| Nominal | Gaussian | Split conformal | ACI |
|---|---|---|---|
| 80% | 63.3% | 61.9% | **79.9%** |
| 90% | 72.9% | 75.8% | **90.0%** |
| 95% | 79.0% | 84.5% | **95.0%** |

## Data

Three instruments with deliberately different liquidity, volatility and news
profiles, so a conclusion holding across all three is not an artefact of one
series. Each has an entirely independent pipeline, news archive and checkpoint.

| Instrument | Bars | Headlines | Sentiment coverage | Test origins |
|---|---|---|---|---|
| Gold (XAU/USD) | 62,049 | 22,833 | 99.9% | 9,297 |
| Silver (XAG/USD) | 62,328 | 11,413 | 99.5% | 9,339 |
| Euro (EUR/USD) | 65,587 | 10,605 | 98.0% | 9,828 |

- **Price** — hourly OHLCV, Jan 2016 – Jul 2026. A curated MetaTrader 5 CSV
  export supplies the history (genuine H1 back to 2010); a read-only live
  attachment supplies fresh bars for the dashboard, with Yahoo Finance as a
  live fallback and the export as a last resort.
- **News** — 44,851 headlines from GDELT DOC 2.0, Google News and public RSS,
  de-duplicated, filtered for instrument relevance, scored with FinBERT.
  Polarity × confidence is cached per headline, so historical news is never
  re-scored and a rerun is reproducible.
- **Macro** — real series: `^IRX`, `^TNX` and DXY via Yahoo, CPI via the US
  Bureau of Labor Statistics API, transformed to stationarity and lagged one
  day before they may touch a bar.

**37 features per bar** = 18 technical + 6 macro + 13 sentiment, over a
T = 60 bar lookback, predicting k = 10 steps ahead. Every feature is a
stationary transform; the ADF test on the close series confirms a unit root.

## Architecture

Dual-tower, 4,401,767 trainable parameters. Price and news are different kinds
of signal — one dense and numeric, the other sparse and semantic — so they stay
in separate towers that meet through an attention operator able to decline the
second stream entirely.

```
Price + macro (B,60,24) ──► Dilated causal CNN (d=1,2,4, RF 15 bars) ──┐
                                                                       ├─► Gated cross-attention (4 heads + presence gate)
FinBERT sentiment (B,60,13) ► Sentiment GRU (13→128) ──────────────────┘
                                        │
                                        ▼
              Causal Transformer (4 layers, 8 heads, d_model 256, FFN 1024)
                                        │
                        Bi-LSTM ‖ Bi-GRU, blended by a learned gate λ
                                        │
                            Attention pooling ──► (B, 256)
                                        │
        ┌───────────────────────────────┴──────────── deep μ ──────────┐
        ▼                                                              ▼
  μ, σ per horizon  ◄── nested convex blend ◄── trust gates σ(W·regime) ◄── GARCH + XGBoost
     (Gaussian NLL)                                                        (walk-forward experts)
```

The Transformer holds 3,159,040 parameters (71.8%) and 77.5% of the compute;
analytical cost is 253.2 M MAC ≈ 0.51 GFLOP per sample.

Design notes worth knowing:

1. **Presence-gated fusion.** `presence = sigmoid(text_gate(text))` is computed
   from the text itself, so when a window carries no headlines the gate closes
   and the fused representation reduces to the price tower. Combined with 40%
   modality masking during training, the network treats news as a
   sometimes-absent shock channel rather than an always-on feature.
2. **XGBoost and GARCH are internal experts, not baselines.** Both are fitted
   first, frozen, and blended inside `forward()` by regime-driven per-horizon
   trust gates. A deep-supervision term keeps the deep pathway a complete
   forecaster so it cannot collapse to zero.
3. **Two-stage freeze-and-tune.** Stage 1 trains the quantitative tower
   text-free over the full history; stage 2 freezes it and fine-tunes the text
   tower, fusion node and decoder on the news-dense period from 2018 at
   one-tenth the learning rate — so seventeen news-sparse years cannot dilute
   the sentiment pathway.

## Evaluation protocol

The protocol *is* the contribution. Two controls:

- **Global base-rate control.** Every directional figure is reported as an
  edge — accuracy minus the always-up base rate of the same bars — never raw.
- **Subset base-rate control.** If a rule trades only a selected subset, the
  base rate is recomputed on that subset. See the retraction above.

Leakage is prevented structurally, not checked afterwards: macro shifted
forward one day; headlines aligned on publication timestamp in a strictly
trailing window; normalisation statistics fitted on the train split alone;
left-only convolutional padding and a causal Transformer mask; classical
baselines re-fitted walk-forward; chronological 70/15/15 split.

## Repository structure

```
├── config.py                      # all hyper-parameters, as three dataclasses
├── main.py                        # end-to-end: build → split → experts → train → evaluate
├── generate_report.py             # regenerate the HTML report from a JSON file
├── data/
│   ├── dataset.py                 # 37-feature panel, windows, train-only normalisation
│   ├── real_data_feed.py          # price/news/macro acquisition and alignment
│   ├── mt5_feed.py                # MetaTrader 5 live API + CSV export loader
│   ├── sentiment.py               # FinBERT scoring, caching, per-bar features
│   ├── technical_indicators.py, pairs.py, synthetic_data.py
├── models/
│   └── hybrid_model.py            # the dual-tower network and its forward pass
├── baselines/                     # ARIMA, GARCH, XGBoost, TFT, vanilla LSTM, random walk
├── training/                      # loop, losses, metric summarisation
├── analysis/                      # significance, conformal, TGC, ablation scans
│   ├── significance_magnitude_gold.py   # block bootstrap, Diebold–Mariano, Hansen MCS
│   ├── conformal_intervals_gold.py      # Gaussian vs split conformal vs ACI
│   └── tgc_h1.py                        # the subset base-rate demonstration
├── scripts/
│   ├── run_multi_seed.py          # the benchmark: seeds 9/36/99 per pair
│   └── build_news_archive.py, build_dataset.py, generate_final_report.py
├── dashboard/app.py               # 5-page Streamlit app incl. live out-of-sample inference
├── tests/test_pipeline.py         # 29 integration tests
├── results/                       # metrics and summary JSONs (the run OUTPUTS)
└── exports/                       # feature panels, archives, checkpoints (the DATA store)
```

## Setup & run

```bash
pip install -r requirements.txt

python tests/test_pipeline.py          # 29/29 should pass
python main.py --quick                 # fast smoke test (synthetic)
python main.py --source real           # single full run on live data
python scripts/run_multi_seed.py       # the benchmark: seeds 9/36/99
streamlit run dashboard/app.py         # the dashboard
```

`streamlit` and `starlette` are pinned **together** in `requirements.txt`:
starlette 1.4.0 made `thread_minimum_size` a required argument of
`GZipResponder.__init__` that no streamlit release passes, which takes the
server down with a 500 on every request. `streamlit>=1.61.1` carries the
upstream cap. Do not bump one without the other.

## Dashboard

| Artifact | Where |
|---|---|
| Live dashboard | https://forex-price-prediction.streamlit.app |


## Known limitations

- One test window per instrument. Gold's is a strong bull market, which raises
  its base rate and makes the directional result window-specific in degree,
  though not in direction.
- Three seeds separate a real effect from initialisation noise but are not a
  substitute for a full walk-forward retraining study.
- No transaction costs, spread or slippage are modelled. This weakens no result
  here — none is a trading claim — but no figure should be read as an
  achievable return.
- The conformal layer is fitted for gold only; its transfer is demonstrated
  rather than assumed.
- Sentiment is headline-level polarity only, so the modality null cannot
  separate a property of markets from a limitation of headline granularity.
- No order-flow or depth-of-market data was available — no consolidated book
  exists for spot metals and FX — so the directional conclusion is a statement
  about *this* feature set, not about all possible feature sets.

## Environment notes

- **xgboost × torch OpenMP clash** (macOS + miniconda). Loading torch's bundled
  libomp first segfaults XGBoost's first `fit()`. Entry points import `xgboost`
  **before** `torch` — see the note at the top of `main.py`.
- **transformers × torch binary mismatch.** `from transformers import pipeline`
  can segfault outright. `data/sentiment.py` probes the import in a throwaway
  subprocess and falls back to a deterministic lexicon scorer if the probe dies.
- **MetaTrader 5 is Windows-only** and is deliberately *not* in
  `requirements.txt`, so the package cannot break a Linux deploy. The price
  chain degrades to Yahoo Finance and then to the curated export, and the
  dashboard states which source served every forecast.
