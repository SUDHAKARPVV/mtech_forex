"""Content pass C: the slides passes A and B did not cover, plus the layout
corrections found during visual QA (titles that wrapped into their subtitle,
callout text wider than its box, text running past a card edge)."""
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from deckedit import set_lines, find

P = Presentation("work.pptx")
S = list(P.slides)

# ============================================================ 18  test-set sizes for all 3 pairs
set_lines(find(S[17], sid=10), [
 "• Chronological 70/15/15 split, never shuffled. Gold: 14,458 train, 3,102 validation, "
 "9,297 test origins; silver 9,339 and euro 9,828 test origins.",
 "• Normalisation fitted on train only; model selected on validation; test scored once.",
 "• ARIMA, GARCH and XGBoost re-fitted walk-forward, so baselines face the same "
 "information constraint.",
 "• Three seeds (9, 36, 99) on every headline result.",
 "• Block bootstrap (2,000 resamples, block 50), Diebold–Mariano with Newey–West HAC at "
 "lag 10, and the Hansen Model Confidence Set at 90%.",
])

# ============================================================ 6  key findings visual
# The left half was a mid-term Gantt chart (April–August, "IN PROGRESS" bars) —
# stale for a final review. Replaced with the headline directional chart.
from deckedit import delete, fit_picture
FIG = "C:/Sudhakar/Github/Forex_Price_Prediction/report/figures"
s = S[5]
for g in [sh for sh in s.shapes
          if sh.shape_type is not None and "GROUP" in str(sh.shape_type)]:
    delete(g)
fit_picture(s, f"{FIG}/fig_directional.png", 0.49, 1.55, 8.12, 4.90)

# ============================================================ 10  FinBERT
s = S[9]
set_lines(find(s, sid=4), [
 "Domain-specific transformer converts raw headlines into a per-bar sentiment signal, for "
 "each instrument separately"])
set_lines(find(s, sid=8), [
 "Instrument-relevant news from GDELT, Google News and public RSS, de-duplicated and "
 "filtered. 44,851 headlines scored in total."])
set_lines(find(s, sid=16), [
 "polarity × confidence stored per headline — historical news is never re-scored, so a run "
 "is reproducible."])
set_lines(find(s, sid=19), ["Align to bars"])
set_lines(find(s, sid=20), [
 "Aligned on publication timestamp only, then rolled into per-bar H1 features. Test-bar "
 "coverage 99.9% gold, 99.5% silver, 98.0% euro."])
set_lines(find(s, sid=23), ["▸ 13 sentiment features"])
set_lines(find(s, sid=24), [
 "rolling mean/std/min/max, momentum, decay, diffusion breadth, headline-count z-score, "
 "and four signal one-hots"])
set_lines(find(s, sid=27), ["▸ Test-bar coverage 98.0 – 99.9%"])

# ============================================================ 11  indicator count
set_lines(find(S[10], sid=4), [
 "18 technical features per bar, drawn from the 12 indicator families below — MACD and "
 "Bollinger each contribute several"])

# ============================================================ 14  layer-by-layer
s = S[13]
set_lines(find(s, sid=7),  ["(B,60,24) → (B,60,128)"])
set_lines(find(s, sid=8),  [
 "Left-padded dilations 1/2/4, no pooling — 15-bar receptive field at full 60-bar "
 "resolution; extracts local breaks a recurrent net smooths over."])
set_lines(find(s, sid=11), ["(B,60,13) → (B,60,128)"])
set_lines(find(s, sid=16), [
 "Four pre-norm layers, 8 heads, causal mask — every relation longer than one session; "
 "71.8% of all parameters."])
set_lines(find(s, sid=26), ["Trust-Gated GARCH + XGBoost Experts"])
set_lines(find(s, sid=27), ["nested convex blend"])
set_lines(find(s, sid=28), [
 "Walk-forward GARCH and XGBoost forecasts blended through volatility trust gates — "
 "bounded by the best single component."])

# ============================================================ 15  training techniques
s = S[14]
set_lines(find(s, sid=6), ["Two-stage freeze and fine-tune"])
set_lines(find(s, sid=7), [
 "The sentiment archive is dense only in recent years. Stage 1 trains the quantitative "
 "tower with the text tower bypassed over the full 2016–2026 history; stage 2 unfreezes "
 "the text tower, fusion node and decoder and fine-tunes at one-tenth the learning rate on "
 "the news-dense later period. This stops a sparse early stream from destabilising the "
 "price backbone while still exploiting news where it is dense."])
set_lines(find(s, sid=11), [
 "GARCH is famous for one thing — modelling how volatile the market is. That ability is "
 "built into the network directly: each head emits a mean and a log-variance per horizon "
 "and is trained under Gaussian negative log-likelihood, so over-confidence is punished by "
 "the squared-error term and under-confidence by the log-variance term. This sigma is what "
 "the conformal layer later calibrates."])
set_lines(find(s, sid=14), ["Modality masking (sentiment dropout p = 0.4)"])
set_lines(find(s, sid=15), [
 "The entire text stream is zeroed for a random 40% of training samples — deliberately "
 "close to the true fraction of news-poor bars, so the training distribution of gate "
 "states resembles deployment. Combined with the presence gate, one checkpoint serves both "
 "news-rich and news-poor periods, and it is what made the price-only ablation measurable "
 "on the same architecture."])
set_lines(find(s, sid=19), [
 "The forward path is long: CNN → cross-attention → Transformer → Bi-LSTM/Bi-GRU → heads. "
 "A deep-supervision term keeps the middle layers learning and stops the deep branch "
 "degenerating into a passive pass-through of the GARCH and XGBoost experts."])

# ============================================================ 16  tensor shapes
s = S[15]
set_lines(find(s, sid=9),  ["Technical (B,60,18) + Macro (B,60,6) + Sentiment (B,60,13)"])
set_lines(find(s, sid=14), ["Assembled to 37 features; routed to Tower A (24 quant) & Tower B (13 text)"])

# ============================================================ 17  system design
s = S[16]
set_lines(find(s, sid=8), [
 "MetaTrader 5 (live + CSV) · GDELT / Google News / RSS · Yahoo rates & DXY · BLS CPI API"])
set_lines(find(s, sid=23), [
 "Base-rate control · 3-seed stability · Block bootstrap · Diebold–Mariano · Hansen MCS · "
 "Conformal coverage"])

# ============================================================ 30  references 8-10 + title
s = S[29]
set_lines(find(s, sid=45), ["References"])
for t, d, title, desc in [
 (35, 36, "[8]  Gibbs & Candès (2021)",
  "Adaptive conformal inference under distribution shift. NeurIPS vol. 34. arXiv:2106.00170"),
 (39, 40, "[9]  Diebold & Mariano (1995)",
  "Comparing predictive accuracy. J. Business & Economic Statistics 13(3):253–263. "
  "doi:10.1080/07350015.1995.10524599"),
 (43, 44, "[10]  Hansen, Lunde & Nason (2011)",
  "The model confidence set. Econometrica 79(2):453–497. doi:10.3982/ECTA5771"),
]:
    set_lines(find(s, sid=t), [title])
    set_lines(find(s, sid=d), [desc])

# ============================================================ visual-QA corrections
# one-line titles: the title boxes are 6.81in (4.10in on slides 25/27) and a
# second line lands on top of the italic subtitle beneath
for n, t in {20: "Results 1 — Directional Accuracy",
             21: "Results 2 — Move-Magnitude Skill",
             22: "Results 3 — Statistical Significance",
             23: "Results 4 — Calibrated Uncertainty"}.items():
    set_lines(find(S[n - 1], sid=36), [t])
set_lines(find(S[23], sid=11), ["Results 5 — Cross-Instrument View"])
set_lines(find(S[24], sid=26), ["Negative Results"])
set_lines(find(S[26], sid=21), ["Future Plan"])

# callout captions must fit the 3.55in navy box
for n, items in {
 20: [(28, "instruments clear their own base rate"),
      (31, "framings tested — all landed at the base rate"),
      (34, "true edge of the Trend-Gated Committee")],
 21: [(28, "seeds beat both baselines, both metrics"),
      (31, "silver — best absolute rank skill"),
      (34, "euro's edge over ATR%, but a weak baseline")],
 22: [(28, "gold intervals contain zero — it matches"),
      (31, "silver & euro intervals exclude zero"),
      (34, "instruments separated by squared error")],
 23: [(28, "raw Gaussian coverage at a nominal 90%"),
      (31, "ACI coverage, same level, under shift"),
      (34, "of origins widened to an unbounded band")],
}.items():
    for sid, txt in items:
        set_lines(find(S[n - 1], sid=sid), [txt])

# 26 — limitations card was overflowing at six bullets
set_lines(find(S[25], sid=10), [
 "• One test window per instrument. Gold's is a strong bull market, which raises its base "
 "rate and makes the directional result window-specific in degree.",
 "• Three seeds — enough to separate effect from initialisation noise, not a full "
 "walk-forward retraining study.",
 "• No transaction costs, spread or slippage modelled, so no figure here is a return claim.",
 "• Conformal layer fitted for gold only; extending it is the first item of future work.",
 "• Sentiment is headline-level, and no order-flow data exists — so both nulls are about "
 "this feature set, not all possible ones.",
])

# 29 — conclusion text boxes were 0.18in wider than the dark card
s = S[28]
set_lines(find(s, sid=8), [
 "Real price, macro and FinBERT sentiment streams feed a dual-tower Hybrid "
 "CNN-LSTM-Transformer with trust-gated experts and regime-aware probabilistic outputs — "
 "4,401,767 parameters, three instruments, hourly resolution."])
set_lines(find(s, sid=12), [
 "Across 3 instruments, 3 seeds and ~15 framings, no configuration exceeded its own "
 "always-up base rate. Apparent successes dissolved once the subset base rate was "
 "computed. Reported as a finding."])
set_lines(find(s, sid=16), [
 "Better than ATR% and GARCH-σ on both metrics, all three instruments, every seed; "
 "significant on silver (p ≤ 0.0055) and euro (p < 0.0001). The squared-error tests do not "
 "separate the models, and that is reported too."])
set_lines(find(s, sid=20), [
 "Adaptive conformal inference restores coverage to 90.0% at a nominal 90%, up from 72.9% "
 "under the raw Gaussian band, and runs live. Next: extend to all three instruments."])
for sid in (7, 8, 11, 12, 15, 16, 19, 20):
    find(s, sid=sid).width = Inches(10.25)

# 3 — objectives: smaller type and tighter spacing so all nine lines are visible
sh = find(S[2], sid=7)
for p in sh.text_frame.paragraphs:
    for r in p.runs:
        r.font.size = Pt(10.5)
    p.space_after = Pt(3)

P.save("work.pptx")
print("pass C applied: slides 10,11,14,15,16,17,30 + visual-QA corrections")

# Row 3 of the results tables inherited the old highlight colour from the
# "Hybrid CNN-LSTM-Transformer" row it used to be. Now that it is just another
# instrument, match it to row 2 so no row reads as emphasised.
for n in (20, 21, 22, 23):
    s = S[n - 1]
    ref = None
    for p in find(s, sid=17).text_frame.paragraphs:
        for r in p.runs:
            ref = r.font.color
            break
        if ref is not None:
            break
    for sid in (22, 23, 24):
        for p in find(s, sid=sid).text_frame.paragraphs:
            for r in p.runs:
                try:
                    r.font.color.rgb = ref.rgb
                except (AttributeError, TypeError):
                    pass
                r.font.bold = False

P.save("work.pptx")
print("results table row 3 colour normalised on slides 20-23")
