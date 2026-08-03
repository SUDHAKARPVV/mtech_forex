"""Content pass B: evaluation methodology, the five results slides, ablations,
interpretation, future plan, timeline, conclusion and references.

Every figure is one of the 124 values already verified against the results JSON.
"""
from pptx import Presentation
from pptx.util import Inches
from deckedit import set_lines, by_text, find, delete, fit_picture

FIG = "C:/Sudhakar/Github/Forex_Price_Prediction/report/figures"
P = Presentation("work.pptx")
S = list(P.slides)
def sl(n): return S[n - 1]

# ============================================================ 18  Evaluation Methodology
s = sl(18)
set_lines(find(s, sid=11), ["Evaluation Methodology"])
set_lines(find(s, sid=4), [
 "The protocol is stated before the results, because it is what makes them interpretable"])
set_lines(find(s, sid=6), ["THE BASE-RATE CONTROL"])
set_lines(find(s, sid=7), [
 "• Directional accuracy is meaningless without the unconditional base rate of the test "
 "window. If an instrument rises in 53.4% of bars, an always-long rule scores 0.534 with "
 "no skill.",
 "• Every directional figure is reported as an edge — accuracy minus base rate — never as "
 "a raw number.",
 "• The base rate is recomputed on whatever bars the claim is made on. A selective "
 "strategy changes its own benchmark.",
 "• This reversed a headline result: the Trend-Gated Committee scored 0.5637 on the bars "
 "it selected, but the always-long rule on those same bars scored 0.5697 — a true edge of "
 "−0.59 pp.",
])
set_lines(find(s, sid=9), ["PROTOCOL & SIGNIFICANCE"])
set_lines(find(s, sid=10), [
 "• Chronological 70/15/15 split, never shuffled. Gold: 14,458 train, 3,102 validation, "
 "9,297 test origins.",
 "• Normalisation fitted on train only; model selected on validation; test scored once.",
 "• ARIMA, GARCH and XGBoost re-fitted walk-forward, so baselines face the same "
 "information constraint.",
 "• Three seeds (9, 36, 99) on every headline result.",
 "• Block bootstrap (2,000 resamples, block 50), Diebold–Mariano with Newey–West HAC at "
 "lag 10, and the Hansen Model Confidence Set at 90%.",
])

# ============================================================ 20  Results 1 — direction
s = sl(20)
set_lines(find(s, sid=36), ["Results 1 — Directional Accuracy vs the Base Rate"])
set_lines(find(s, sid=4), [
 "Hourly H1, three instruments, three seeds — every model measured against the always-up "
 "base rate of the same bars"])
set_lines(find(s, sid=6),  ["Instrument"])
set_lines(find(s, sid=7),  ["Hybrid"])
set_lines(find(s, sid=8),  ["Base rate"])
set_lines(find(s, sid=9),  ["Edge"])
set_lines(find(s, sid=11), ["Gold  (XAU/USD)"]);   set_lines(find(s, sid=12), ["0.5178"])
set_lines(find(s, sid=13), ["0.5344"]);            set_lines(find(s, sid=19), ["− 1.7 pp"])
set_lines(find(s, sid=16), ["Silver  (XAG/USD)"]); set_lines(find(s, sid=17), ["0.5145"])
set_lines(find(s, sid=18), ["0.5354"]);            set_lines(find(s, sid=14), ["− 2.1 pp"])
set_lines(find(s, sid=21), ["Euro  (EUR/USD)"]);   set_lines(find(s, sid=22), ["0.4984"])
set_lines(find(s, sid=23), ["0.5037"]);            set_lines(find(s, sid=24), ["− 0.5 pp"])
set_lines(find(s, sid=25), [
 "Seed dispersion is 0.0005 / 0.0018 / 0.0015 — one to two orders of magnitude smaller "
 "than the gap to the base rate."])
set_lines(find(s, sid=27), ["0 of 3"])
set_lines(find(s, sid=28), ["instruments clear their own base rate"])
set_lines(find(s, sid=30), ["~15"])
set_lines(find(s, sid=31), ["alternative framings tested — all landed at the base rate"])
set_lines(find(s, sid=33), ["− 0.59 pp"])
set_lines(find(s, sid=34), ["true edge of the Trend-Gated Committee once its subset base rate is computed"])
set_lines(find(s, sid=35), [
 "Discussion:  GARCH scores a higher raw accuracy (0.5378 on gold) but that is momentum "
 "drift reproducing the base rate — it too fails to clear it.",
 "Direction is not forecastable at hourly resolution by this system or by the classical "
 "baselines. This is consistent with market efficiency, and is reported as a finding."])

# ============================================================ 21  Results 2 — magnitude
s = sl(21)
set_lines(find(s, sid=36), ["Results 2 — Move-Magnitude Forecasting"])
set_lines(find(s, sid=4), [
 "Spearman rank skill against the realised absolute 10-bar move — three-seed means, "
 "versus the two natural volatility benchmarks"])
set_lines(find(s, sid=6),  ["Instrument"])
set_lines(find(s, sid=7),  ["Hybrid"])
set_lines(find(s, sid=8),  ["ATR%"])
set_lines(find(s, sid=9),  ["GARCH-σ"])
set_lines(find(s, sid=11), ["Gold  (XAU/USD)"]);   set_lines(find(s, sid=12), ["0.3288"])
set_lines(find(s, sid=13), ["0.3086"]);            set_lines(find(s, sid=19), ["0.3043"])
set_lines(find(s, sid=16), ["Silver  (XAG/USD)"]); set_lines(find(s, sid=17), ["0.4178"])
set_lines(find(s, sid=18), ["0.3771"]);            set_lines(find(s, sid=14), ["0.3463"])
set_lines(find(s, sid=21), ["Euro  (EUR/USD)"]);   set_lines(find(s, sid=22), ["0.2316"])
set_lines(find(s, sid=23), ["0.0894"]);            set_lines(find(s, sid=24), ["0.1453"])
set_lines(find(s, sid=25), [
 "Large-move classification agrees: 0.5517 / 0.5520 / 0.5709 for the hybrid against "
 "adaptive base rates of 0.5046 / 0.5119 / 0.4969."])
set_lines(find(s, sid=27), ["3 of 3"])
set_lines(find(s, sid=28), ["seeds beat both baselines on both metrics — the harness verdict is ROBUST"])
set_lines(find(s, sid=30), ["0.4178"])
set_lines(find(s, sid=31), ["silver — highest absolute rank skill of the three instruments"])
set_lines(find(s, sid=33), ["+0.142"])
set_lines(find(s, sid=34), ["euro's edge over ATR% — the largest, but against a weak baseline"])
set_lines(find(s, sid=35), [
 "Discussion:  The same model loses on direction and wins on magnitude because volatility "
 "clusters in time while the sign of the next return is close to a martingale.",
 "It does not mean the system predicts returns. It means that on the axis where structure "
 "exists, the deep model extracts more of it than ATR% or GARCH-σ."])

# ============================================================ 22  Results 3 — significance
s = sl(22)
set_lines(find(s, sid=36), ["Results 3 — Statistical Significance of the Magnitude Edge"])
set_lines(find(s, sid=4), [
 "Three tests on the frozen seed-9 forecasts — the bootstrap scores the rank metrics, "
 "Diebold–Mariano and the MCS score squared error"])
set_lines(find(s, sid=6),  ["Instrument"])
set_lines(find(s, sid=7),  ["Boot. p"])
set_lines(find(s, sid=8),  ["Diebold–Mariano p"])
set_lines(find(s, sid=9),  ["MCS 90%"])
set_lines(find(s, sid=11), ["Gold  (XAU/USD)"]);   set_lines(find(s, sid=12), ["0.271"])
set_lines(find(s, sid=13), ["0.268  /  0.257"]);   set_lines(find(s, sid=19), ["all 3 retained"])
set_lines(find(s, sid=16), ["Silver  (XAG/USD)"]); set_lines(find(s, sid=17), ["0.0055"])
set_lines(find(s, sid=18), ["0.446  /  0.216"]);   set_lines(find(s, sid=14), ["all 3 retained"])
set_lines(find(s, sid=21), ["Euro  (EUR/USD)"]);   set_lines(find(s, sid=22), ["< 0.0001"])
set_lines(find(s, sid=23), ["0.251  /  0.256"]);   set_lines(find(s, sid=24), ["all 3 retained"])
set_lines(find(s, sid=25), [
 "Bootstrap p is the worst of four comparisons per instrument. Every Diebold–Mariano "
 "statistic is positive — the tests fail on significance, not on sign."])
set_lines(find(s, sid=27), ["4 of 4"])
set_lines(find(s, sid=28), ["gold confidence intervals contain zero — it matches, not beats"])
set_lines(find(s, sid=30), ["8 of 8"])
set_lines(find(s, sid=31), ["silver and euro intervals exclude zero"])
set_lines(find(s, sid=33), ["0 of 3"])
set_lines(find(s, sid=34), ["instruments separated by the squared-error tests"])
set_lines(find(s, sid=35), [
 "Why they disagree:  squared error is dominated by a few extreme moves and is sensitive "
 "to forecast scale; rank metrics depend only on ordering.",
 "Defensible claim:  on silver and euro the hybrid orders magnitude significantly better "
 "than ATR% and GARCH-σ, but is not demonstrably better in squared-error terms; on gold "
 "it is statistically indistinguishable from both."])

# ============================================================ 23  Results 4 — conformal
s = sl(23)
set_lines(find(s, sid=36), ["Results 4 — Calibrated Uncertainty via Adaptive Conformal Inference"])
set_lines(find(s, sid=4), [
 "Empirical test coverage on gold — calibrated on 3,102 validation origins, evaluated on "
 "9,297 test origins, per horizon"])
set_lines(find(s, sid=6),  ["Nominal level"])
set_lines(find(s, sid=7),  ["Gaussian"])
set_lines(find(s, sid=8),  ["Split conformal"])
set_lines(find(s, sid=9),  ["ACI"])
set_lines(find(s, sid=11), ["80%"]); set_lines(find(s, sid=12), ["63.3%"])
set_lines(find(s, sid=13), ["61.9%"]); set_lines(find(s, sid=19), ["79.9%"])
set_lines(find(s, sid=16), ["90%"]); set_lines(find(s, sid=17), ["72.9%"])
set_lines(find(s, sid=18), ["75.8%"]); set_lines(find(s, sid=14), ["90.0%"])
set_lines(find(s, sid=21), ["95%"]); set_lines(find(s, sid=22), ["79.0%"])
set_lines(find(s, sid=23), ["84.5%"]); set_lines(find(s, sid=24), ["95.0%"])
set_lines(find(s, sid=25), [
 "Cost is reported next to coverage: at 90% the ACI half-width is 1.558% against the "
 "Gaussian 1.172% — 33% wider."])
set_lines(find(s, sid=27), ["72.9%"])
set_lines(find(s, sid=28), ["raw Gaussian coverage at a nominal 90% — badly over-confident"])
set_lines(find(s, sid=30), ["90.0%"])
set_lines(find(s, sid=31), ["ACI coverage at the same nominal level, under regime shift"])
set_lines(find(s, sid=33), ["2 – 11%"])
set_lines(find(s, sid=34), ["of origins where the controller widens to an unbounded interval — a regime-stress flag"])
set_lines(find(s, sid=35), [
 "Split conformal is not enough:  the 2024–2026 test window is materially more volatile "
 "than the calibration window, violating the exchangeability it requires.",
 "ACI makes the miscoverage level a controlled variable, so a run of misses widens later "
 "intervals until coverage recovers. This is the most robust contribution of the work — "
 "it states uncertainty rather than predicting returns, and is deployed live."])

# ============================================================ 24  Results 5 — cross-instrument
s = sl(24)
set_lines(find(s, sid=11), ["Results 5 — Cross-Instrument Comparison"])
set_lines(find(s, sid=4), [
 "Magnitude edge over the classical volatility baselines by instrument, with bootstrap "
 "significance"])
for sid in (5, 6, 7, 8, 9, 10):
    delete(find(s, sid=sid))
fit_picture(s, f"{FIG}/fig_cross_currency.png", 0.62, 1.62, 12.10, 4.35)
tb = s.shapes.add_textbox(Inches(0.62), Inches(6.15), Inches(12.10), Inches(0.85))
tf = tb.text_frame
tf.word_wrap = True
from pptx.util import Pt
from pptx.dml.color import RGBColor
for i, line in enumerate([
    "Absolute skill tracks how much volatility structure an instrument has; the edge tracks "
    "how badly the classical baselines handle it — and the two are not the same ranking.",
    "Silver is the strongest genuine result: highest absolute skill (0.418) against baselines "
    "that are themselves competent. Euro's larger edge reflects a weak ATR% (0.089 rank skill, "
    "below its own base rate)."]):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    r = p.add_run(); r.text = line
    r.font.size = Pt(11.5); r.font.name = "Calibri"
    r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

# ============================================================ 25  Ablations / negative results
s = sl(25)
set_lines(find(s, sid=26), ["Feature & Architecture Studies — Including Negative Results"])
set_lines(find(s, sid=4), [
 "Every candidate improvement was pre-checked on training and validation data only, "
 "before wiring — and is reported regardless of outcome"])
cards = [
 (6, 7, 8, 9,
  "Modality ablation",
  "Do news and macro add magnitude skill over price features?",
  "Finding:  No. Price-only reaches 0.321 Spearman against 0.329 for the full multi-modal "
  "model — inside the bootstrap interval.",
  "▸ Qualifies the multi-modal premise"),
 (11, 12, 13, 14,
  "HAR-RV features",
  "Do multi-timescale realised-volatility features help?",
  "Finding:  Pre-check strong (partial ρ +0.11 to +0.17) but the retrained model did not "
  "improve — 0.326 against 0.329.",
  "▸ A strong pre-check does not guarantee a gain"),
 (16, 17, 18, 19,
  "CFTC positioning & Fair Value Gaps",
  "Does institutional positioning or ICT-style imbalance predict anything?",
  "Finding:  Direction dead (|ρ| ≤ 0.014 and ≤ 0.018); magnitude signal largely redundant "
  "with ATR%.",
  "▸ Both channels dropped"),
 (21, 22, 23, 24,
  "Quantile heads & order book",
  "Would pinball-loss heads beat sigma + conformal? Can depth-of-market be used?",
  "Finding:  Quantiles added only 0.8 pp of coverage — ACI already handles the regime "
  "shift. No historical order book exists for spot metals and FX.",
  "▸ ACI retained; order flow unavailable"),
]
for t_id, s_id, f_id, a_id, title, sub, finding, arrow in cards:
    set_lines(find(s, sid=t_id), [title])
    set_lines(find(s, sid=s_id), [sub])
    set_lines(find(s, sid=f_id), [finding])
    set_lines(find(s, sid=a_id), [arrow])

# ============================================================ 26  Interpretation & limitations
s = sl(26)
set_lines(find(s, sid=11), ["Interpretation & Limitations"])
set_lines(find(s, sid=4), ["What the results mean — and where the honest boundaries are"])
set_lines(find(s, sid=6), ["INTERPRETATION"])
set_lines(find(s, sid=7), [
 "• The negative and positive results are load-bearing for each other: the same "
 "architecture, features, test bars and protocol produced both, which rules out a broken "
 "pipeline or a mis-built test set.",
 "• Direction fails because the sign of an hourly return carries almost no exploitable "
 "structure; magnitude succeeds because volatility clusters in time.",
 "• Sentiment adds approximately zero magnitude skill at H1 despite 98–99.9% test-bar "
 "coverage — the ordering of results follows volatility structure, not news volume.",
 "• Calibrated uncertainty is the component untouched by market efficiency: it does not "
 "predict returns, only how uncertain a forecast is.",
])
set_lines(find(s, sid=9), ["LIMITATIONS"])
set_lines(find(s, sid=10), [
 "• One test window per instrument. Gold's is a strong bull market, which raises its base "
 "rate and makes the directional result window-specific in degree.",
 "• Three seeds — enough to separate effect from initialisation noise, not a full "
 "walk-forward retraining study.",
 "• No transaction costs, spread or slippage are modelled, so no figure here is a return "
 "claim.",
 "• The conformal layer is fitted for gold only; extension to silver and euro is the first "
 "item of future work.",
 "• Sentiment is headline-level, so the null cannot separate a property of markets from a "
 "limit of headline granularity.",
 "• No order-flow data, so the directional conclusion is about this feature set, not all "
 "possible feature sets.",
])

# ============================================================ 27  Future plans
s = sl(27)
set_lines(find(s, sid=21), ["Future Plan — Ordered by the Evidence Behind It"])
set_lines(find(s, sid=6),  ["Complete the uncertainty layer"])
set_lines(find(s, sid=7), [
 "Extend adaptive conformal inference to silver and euro. Strong evidence, low effort — it "
 "runs on frozen forecasts with no retraining — and it completes the most robust result of "
 "the project."])
set_lines(find(s, sid=10), ["Volatility-targeted decision layer"])
set_lines(find(s, sid=11), [
 "Since magnitude is the predictable axis, drive position sizing and risk budgeting from "
 "the calibrated interval width rather than attempting directional trading."])
set_lines(find(s, sid=14), ["Explainability from the existing gates"])
set_lines(find(s, sid=15), [
 "The presence gate, temporal gate λ and the two expert trust gates are already computed "
 "at inference. Exposing them is instrumentation, not modelling — the trust gates reveal "
 "when the network defers to GARCH."])
set_lines(find(s, sid=18), ["Test the null results, don't just add capacity"])
set_lines(find(s, sid=19), [
 "Long-context encoding of full statements, and a lower-frequency macro study — each tests "
 "a specific alternative explanation for a null result. Order flow stays blocked: no "
 "historical source is obtainable."])

# ============================================================ 28  Timeline
s = sl(28)
set_lines(find(s, sid=4), ["From data pipeline to final submission — what actually happened"])
set_lines(find(s, sid=9),  ["Jan – May 2026"])
set_lines(find(s, sid=10), ["Data & baselines"])
set_lines(find(s, sid=11), ["Two-pipeline data, FinBERT scoring, initial hybrid."])
set_lines(find(s, sid=15), ["Jun 2026"])
set_lines(find(s, sid=16), ["Mid-term review"])
set_lines(find(s, sid=17), ["Full hybrid, ARIMA/GARCH baselines, first results."])
set_lines(find(s, sid=20), ["Jun – Jul 2026"])
set_lines(find(s, sid=21), ["Final research"])
set_lines(find(s, sid=22), ["H1 migration, 3 pairs, base-rate control, conformal layer."])
set_lines(find(s, sid=25), ["Jul 2026"])
set_lines(find(s, sid=26), ["Final submission (now)"])
set_lines(find(s, sid=27), ["Significance tests, dissertation, live dashboard."])

# ============================================================ 29  Conclusion
s = sl(29)
set_lines(find(s, sid=7),  ["Built an end-to-end multi-modal FX forecasting system"])
set_lines(find(s, sid=8), [
 "Real price, macro and FinBERT sentiment streams feed a dual-tower Hybrid "
 "CNN-LSTM-Transformer with trust-gated experts and regime-aware probabilistic outputs — "
 "4,401,767 parameters across three instruments at hourly resolution."])
set_lines(find(s, sid=11), ["Direction is not forecastable at H1 — established, not assumed"])
set_lines(find(s, sid=12), [
 "Across 3 instruments, 3 seeds and ~15 framings no configuration exceeded its own "
 "always-up base rate. Apparent successes dissolved once the base rate of the selected "
 "subset was computed. Reported as a finding, not hidden."])
set_lines(find(s, sid=15), ["Magnitude is forecastable, and the hybrid beats the classical models"])
set_lines(find(s, sid=16), [
 "Better than ATR% and GARCH-σ on both metrics, all three instruments, every seed; "
 "significant on silver (p ≤ 0.0055) and euro (p < 0.0001). Squared-error tests do not "
 "separate the models, and that disagreement is reported in full."])
set_lines(find(s, sid=19), ["Calibrated uncertainty is the most robust contribution"])
set_lines(find(s, sid=20), [
 "Adaptive conformal inference restores nominal coverage — 90.0% against a nominal 90%, "
 "from 72.9% under the raw Gaussian band — and is deployed live. Next: extend it to all "
 "three instruments and drive position sizing from interval width."])

# ============================================================ 30  References
s = sl(30)
# NB: on this cloned layout the title is shape 45 — shape 26 is a decorative bar
set_lines(find(s, sid=45), ["References"])
set_lines(find(s, sid=4), [
 "IEEE style, numbered by order of first citation; bibliographic details verified against "
 "Crossref records"])
REFS = [
 (7, 8, "[1]  Dave, Varastehpour & Shakiba (2025)",
  "Predicting forex prices: LSTM, XGBoost and transformer architectures. EECT, pp. 1–6. doi:10.1109/EECT64505.2025.10966964"),
 (11, 12, "[2]  Yohannes et al. (2025)",
  "Forecasting stock prices with sequential deep learning: an LSTM approach. ICVEE, pp. 177–183. doi:10.1109/ICVEE66651.2025.11281457"),
 (15, 16, "[3]  Luangluewut & Thiennviboon (2023)",
  "Forex price trend prediction using a convolutional neural network. ECTI-CON, pp. 1–4. doi:10.1109/ECTI-CON58255.2023.10153142"),
 (19, 20, "[4]  Tadphale, Saraswat, Sonawane & Deshmukh (2023)",
  "Impact of news sentiment on foreign exchange rate prediction. CONIT, pp. 1–8. doi:10.1109/CONIT59222.2023.10205534"),
 (23, 24, "[5]  Araci (2019)",
  "FinBERT: financial sentiment analysis with pre-trained language models. arXiv:1908.10063"),
 (27, 28, "[6]  Leushuis & Petkov (2026)",
  "Advances in forecasting realized volatility: a review. Financial Innovation, vol. 12. doi:10.1186/s40854-025-00809-5"),
 (31, 32, "[7]  Corsi (2009)",
  "A simple approximate long-memory model of realized volatility. J. Financial Econometrics 7(2):174–196. doi:10.1093/jjfinec/nbp001"),
]
for t_id, d_id, title, desc in REFS:
    set_lines(find(s, sid=t_id), [title])
    set_lines(find(s, sid=d_id), [desc])

P.save("work.pptx")
print("pass B applied to slides 18, 20-30")
