"""Content pass A: slides 1-17 and 19 (front matter, data, architecture, tools).

Every number here is one of the values already verified against the results
JSON / config / instantiated model during the report work.
"""
import sys
from pptx import Presentation
from deckedit import set_lines, by_text, find, delete

P = Presentation("work.pptx")
S = list(P.slides)


def sl(n):
    return S[n - 1]


# ============================================================ 1  Title
s = sl(1)
set_lines(by_text(s, "AI-Driven"),
          ["AI-Driven Multi-Step Forecasting of Foreign Exchange Rates"])
set_lines(by_text(s, "Student Name"),
          ["Student Name: PUPPALA V V SUDHAKAR",
           "BITS ID: 2024AA05488",
           "Final Semester Dissertation Review  ·  July 2026"])

# ============================================================ 2  Abstract
s = sl(2)
set_lines(by_text(s, "Foreign exchange markets are among"), [
 "Foreign exchange markets are among the most liquid and volatile financial markets, "
 "influenced by macroeconomic indicators, geopolitical events and market sentiment. "
 "Traditional approaches such as ARIMA and GARCH presuppose stationarity and linear "
 "dependence, which high-frequency currency data routinely violate.",
 "",
 "This dissertation designs and evaluates a hybrid CNN-LSTM-Transformer framework for "
 "multi-step forecasting on gold (XAU/USD), silver (XAG/USD) and the euro (EUR/USD) at "
 "hourly resolution over 2016–2026. The 4.4-million-parameter model fuses a dilated "
 "causal price encoder with a FinBERT sentiment encoder through gated cross-attention, "
 "and blends trust-gated GARCH and XGBoost experts under regime-aware Gaussian heads.",
 "",
 "The result is two-sided and both sides are reported. Hourly direction proved "
 "unforecastable once every claim was measured against the always-up base rate of the "
 "same bars. Move magnitude is forecastable: the hybrid beats ATR% and GARCH-σ on all "
 "three instruments, on every seed. Adaptive conformal inference restores nominal "
 "interval coverage under regime shift.",
])

# ============================================================ 3  Objectives
s = sl(3)
set_lines(by_text(s, "The objective of this dissertation"), [
 "The objectives of this dissertation project were to,",
 "Design and implement a Hybrid CNN-LSTM-Transformer with dual-tower multi-modal fusion "
 "for multi-step FX forecasting.",
 "Build a reproducible, leak-free pipeline over price, macroeconomic and FinBERT "
 "sentiment streams.",
 "Fuse GARCH and XGBoost experts into the network through learned trust gates.",
 "Evaluate directional accuracy against the always-up base rate rather than 0.50, across "
 "multiple random seeds.",
 "Evaluate move-magnitude forecasting against the ATR% indicator and the GARCH "
 "conditional-sigma baseline.",
 "Establish significance with a block bootstrap, Diebold–Mariano tests and the Hansen "
 "Model Confidence Set.",
 "Deliver calibrated uncertainty through adaptive conformal inference with measured "
 "empirical coverage.",
 "Extend the study from one instrument to three and compare behaviour across them.",
])

# ============================================================ 5  Methodology
# The five methodology rows are SmartArt, whose text lives in ppt/diagrams/ —
# handled by patch_diagram.py after this pass.

# ============================================================ 6  Key Findings
s = sl(6)
set_lines(find(s, sid=113), ["Direction is not forecastable"])
set_lines(find(s, sid=14), [
 "Across 3 instruments, 3 seeds and roughly 15 alternative framings, no configuration "
 "exceeded its own always-up base rate. The hybrid sits 0.5 to 2.1 pp below it."])
set_lines(find(s, sid=15), ["Magnitude is forecastable"])
set_lines(find(s, sid=16), [
 "On the absolute size of the next 10-bar move the hybrid beats both ATR% and GARCH-σ "
 "on rank skill and large-move classification, for all three instruments on every seed — "
 "significantly so for silver and the euro."])
set_lines(find(s, sid=17), ["Calibrated uncertainty"])
set_lines(find(s, sid=18), [
 "The raw Gaussian band covers only 72.9% at a nominal 90%. Adaptive conformal inference "
 "restores 90.0% under a regime shift that defeats split conformal — the most robust "
 "contribution of the work."])
set_lines(find(s, sid=2), ["Key Findings"])

# ============================================================ 7  Key Contributions
s = sl(7)
set_lines(find(s, sid=11), ["Key Contributions"])
set_lines(find(s, sid=4), ["A base-rate-controlled negative result on hourly FX direction"])
set_lines(find(s, sid=5), [
 "Established across three instruments, three seeds and roughly fifteen framings. The "
 "control also exposed how subset selection silently raises the benchmark: the "
 "Trend-Gated Committee scored 0.5637 on the bars it chose, but the always-long rule on "
 "those same bars scored 0.5697 — a true edge of −0.59 pp. Directional accuracy "
 "reported without a base rate is not evidence of skill."])
set_lines(find(s, sid=17), ["A demonstrated magnitude advantage over ATR% and GARCH-σ"])
set_lines(find(s, sid=18), [
 "Robust across all seeds on all three instruments and statistically significant on two "
 "of them under a block bootstrap. Silver is the strongest genuine result: 0.4178 "
 "Spearman rank skill against competent baselines at 0.3771 and 0.3463. The scope of the "
 "claim is stated precisely rather than generalised."])
set_lines(find(s, sid=21), ["An adaptive conformal layer, deployed rather than only measured"])
set_lines(find(s, sid=22), [
 "Split conformal is shown to be insufficient because the test window violates "
 "exchangeability. Adaptive conformal inference restores coverage to 79.9 / 90.0 / 95.0% "
 "against nominal 80 / 90 / 95, and runs live in the dashboard. Because it states "
 "uncertainty rather than predicting returns, it is untouched by the efficiency "
 "constraint that limits directional forecasting."])

# ============================================================ 9  Data Extraction
s = sl(9)
set_lines(by_text(s, "Three real, incrementally-cached"), [
 "Three independently acquired streams, aligned to a common hourly trading calendar "
 "across three instruments"])
set_lines(by_text(s, "PRICE"), ["PRICE — 3 instruments at H1"])
set_lines(find(s, sid=8), [
 "Source: MetaTrader 5 terminal (live) + curated CSV export",
 "Hourly OHLCV bars, Jan 2016 – Jul 2026",
 "Gold 62,049 · Silver 62,328 · Euro 65,587 bars",
 "Each pair has its own history and checkpoint",
])
set_lines(by_text(s, "NEWS"), ["NEWS — Financial Headlines"])
set_lines(find(s, sid=12), [
 "Sources: GDELT DOC 2.0, Google News, public RSS",
 "44,851 scored headlines in total (2016–2026)",
 "Gold 22,833 · Silver 11,413 · Euro 10,605",
 "Aligned on publication timestamp only — no look-ahead",
])
set_lines(by_text(s, "MACRO"), ["MACRO — Rates, Dollar, Inflation"])
set_lines(find(s, sid=16), [
 "Yahoo: ^IRX (13-wk T-bill), ^TNX (10-yr), DXY",
 "BLS public API: monthly CPI (yoy / mom)",
 "Every macro series shifted +1 day before use",
 "Stationary transforms (z-scores, changes)",
])
set_lines(find(s, sid=17), [
 "Two-pipeline design:   build_dataset.py verifies & caches the feature panel  →  "
 "run_multi_seed.py trains only on verified data (no re-fetch, no re-scoring).",
])

# ============================================================ 11  Technical indicators
s = sl(11)
set_lines(by_text(s, "12 technical features"), [
 "18 technical features per bar — computed from OHLCV, each capturing a distinct market "
 "facet"])

# ============================================================ 12  Feature engineering
s = sl(12)
set_lines(by_text(s, "Three parallel streams"), [
 "Three parallel streams → 37 aligned features over a 60-bar lookback, split into a "
 "dual-tower contract"])
set_lines(find(s, sid=7), ["18 features"])
set_lines(find(s, sid=8), [
 "• OHLC log-returns, RSI, MACD×3",
 "• Bollinger width, ATR%, ROC, %K",
 "• EMA ratio, volume z, realised vol",
 "• Envelope position, drift t-statistic",
 "• Min-max / z-scored within window",
])
set_lines(find(s, sid=11), ["6 features"])
set_lines(find(s, sid=15), ["13 features"])
set_lines(find(s, sid=18), [
 "Fusion & normalization:  Stationary transforms remove price-level dependence; every "
 "stream shares one 60-bar time axis; scaling statistics come from the training split alone.",
 "Dual-tower split:  24 quantitative features (18 technical + 6 macro) feed Tower A; "
 "13 sentiment features feed Tower B — kept as separate tensors so the text stream can "
 "be masked.",
])

# ============================================================ 13  Architecture flow
s = sl(13)
set_lines(find(s, sid=25), [
 "Fused expert:  Walk-forward XGBoost and GARCH forecasts are blended in through "
 "regime-driven per-horizon trust gates.  Total 4,401,767 trainable parameters."])

# ============================================================ 19  Tools & Platforms
s = sl(19)
set_lines(by_text(s, "An open-source, Python-centric"), [
 "An open-source, Python-centric, reproducible deep-learning and evaluation stack"])
set_lines(find(s, sid=8), ["• Python 3.13", "• PyTorch", "• NumPy & Pandas", "• scikit-learn"])
set_lines(find(s, sid=12), ["• Hugging Face Transformers", "• FinBERT (ProsusAI)", "• tokenizers"])
set_lines(find(s, sid=15), ["Baselines & Statistics"])
set_lines(find(s, sid=16), [
 "• arch (GARCH), statsmodels (ARIMA)",
 "• XGBoost expert",
 "• SciPy — bootstrap, Diebold–Mariano, MCS",
])
set_lines(find(s, sid=20), [
 "• MetaTrader 5 terminal (live + CSV)",
 "• GDELT DOC 2.0, Google News, RSS",
 "• Yahoo Finance, BLS public API",
])
set_lines(find(s, sid=23), ["Delivery & Runtime"])
set_lines(find(s, sid=24), [
 "• Streamlit live dashboard",
 "• Matplotlib figures",
 "• Windows / venv · Git version control",
])

P.save("work.pptx")
print("pass A applied to slides 1,2,3,5,6,7,9,11,12,13,19")
