"""Diagrams for Section 4 (Evaluation Methodology). PNG + editable SVG."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diagram_lib import *   # noqa

OUT = os.path.dirname(os.path.abspath(__file__)) + "/figs"
os.makedirs(OUT, exist_ok=True)

# ============================================================ E1  chronological split
c = Canvas(12.6, 6.6, "Section 4.1 — Chronological splitting and walk-forward evaluation",
           "The split is made in time order and never shuffled; every fitted quantity looks only backwards")

# ---- the split bar --------------------------------------------------------
X0, X1, YB, HB = 0.070, 0.955, 0.760, 0.078
w_tr, w_va = 0.70 * (X1 - X0), 0.15 * (X1 - X0)
c.band(X0, YB, w_tr, HB, "#0E7C86", "#0E7C86")
c.band(X0 + w_tr, YB, w_va, HB, "#6D48C7", "#6D48C7")
c.band(X0 + w_tr + w_va, YB, w_va, HB, "#0F766E", "#0F766E")
c.label(X0 + w_tr / 2, YB + HB / 2, "TRAIN  ·  70%", fs=10.5, color="white", bold=True)
c.label(X0 + w_tr + w_va / 2, YB + HB / 2, "VALIDATION\n15%", fs=8.0, color="white", bold=True)
c.label(X0 + w_tr + 1.5 * w_va, YB + HB / 2, "TEST\n15%", fs=8.0, color="white", bold=True)
c.label(X0, YB + HB + 0.030, "Jan 2016", fs=8.2, color=INK, ha="left", bold=True)
c.label(X1, YB + HB + 0.030, "Jul 2026", fs=8.2, color=INK, ha="right", bold=True)
# annotations: left block under TRAIN, right block right-aligned so the wide
# origin counts cannot run past the canvas edge or collide with each other
c.label(X0 + w_tr / 2, YB - 0.072,
        "training origins strided by 3\n(consecutive windows overlap by 59 of 60 bars)",
        fs=7.6, color=INK)
c.label(X1, YB - 0.072,
        "gold: 14,458 train · 3,102 validation · 9,297 test origins\n"
        "silver 9,339 and euro 9,828 held-out test origins",
        fs=7.6, color=INK, ha="right")
c.label((X0 + X1) / 2, YB - 0.148, "time  →", fs=8.4, color=GREY, italic=True)

# ---- what is fitted where -------------------------------------------------
W, H = 0.230, 0.070
c.box("norm", 0.185, 0.545, W, H, "Normalisation statistics", TEAL, fs=8.4,
      sub="mean and scale from TRAIN only")
c.box("early", 0.470, 0.545, W, H, "Early stopping", PURPLE, fs=8.6,
      sub="model selected on VALIDATION loss")
c.box("frozen", 0.760, 0.545, W, H, "Frozen forecasts", GREEN, fs=8.4,
      sub="TEST scored once, never tuned on")
c.arrow("norm", "early"); c.arrow("early", "frozen")

# ---- walk-forward strip ---------------------------------------------------
c.band(0.045, 0.135, 0.910, 0.300, "#F4F7FB", "#E3EAF2",
       "Classical baselines (ARIMA, GARCH, XGBoost) are re-fitted walk-forward")
BW, BH = 0.118, 0.056
xs = [0.100, 0.268, 0.436, 0.604, 0.772]
for i, x in enumerate(xs):
    c.box(f"h{i}", x, 0.330, BW, BH, f"history ≤ t{i}", "#8FA3B8", tc=INK, fs=7.6)
    c.box(f"p{i}", x, 0.205, BW, BH, f"predict block {i+1}", TEAL, fs=7.6)
    c.arrow(f"h{i}", f"p{i}", s_side="B", d_side="T")
    if i:
        c.line(xs[i-1] + BW / 2, 0.330, x - BW / 2, 0.330, color=EDGE, lw=1.0, style=":")
c.label(0.905, 0.268, "…", fs=13, color=GREY)
c.note("No shuffling at any point: a random split would let the model interpolate between neighbouring hourly bars and is invalid for time series.\n"
       "Each baseline block is predicted by a model fitted only on data preceding it, so the classical comparators face exactly the same information constraint.",
       y=0.055)
c.save(f"{OUT}/fig_eval_split")

# ============================================================ E2  base-rate control
c = Canvas(12.4, 7.0, "Section 4.2 — The base-rate control, applied globally and to any selected subset",
           "Accuracy is only evidence of skill when compared against the best fixed rule on the same bars")
W, H = 0.205, 0.074
c.box("acc",  0.155, 0.815, W, H, "Reported accuracy", NAVY, fs=8.6, sub="A on a set of bars S")
c.box("base", 0.155, 0.660, W, H, "Base rate on S", AMBER, fs=8.6, sub="B = best fixed rule on S")
c.box("edge", 0.470, 0.738, W, H, "Edge = A − B", GREEN, fs=9.0, sub="the only quantity reported")
c.box("yes",  0.790, 0.815, W, H, "Edge > 0", TEAL, fs=8.8, sub="evidence of skill")
c.box("no",   0.790, 0.660, W, H, "Edge ≤ 0", "#B9C6D4", tc=INK, fs=8.8, sub="drift, not skill")
c.elbow("acc","edge",  s_side="R", d_side="L", mid=0.320, d_off=+0.28)
c.elbow("base","edge", s_side="R", d_side="L", mid=0.320, d_off=-0.28)
c.elbow("edge","yes",  s_side="R", d_side="L", mid=0.640, s_off=+0.28)
c.elbow("edge","no",   s_side="R", d_side="L", mid=0.640, s_off=-0.28)
c.label(0.500, 0.588, "S is whatever set of bars the claim is actually made on — the global test set, or the subset a selective rule chose to trade",
        fs=7.8, color=GREY, italic=True)

# ---- worked example -------------------------------------------------------
c.band(0.045, 0.205, 0.910, 0.335, "#FFF8F0", "#F3E4D2",
       "Worked example — the Trend-Gated Committee on gold, where the control changes the conclusion")
EW, EH = 0.200, 0.072
c.box("all",  0.150, 0.430, EW, EH, "All test bars", "#B9C6D4", tc=INK, fs=8.4, sub="9,297 origins")
c.box("gate", 0.150, 0.275, EW, EH, "Gated subset", AMBER, fs=8.4, sub="1,985 origins · 21.4%")
c.box("tgc",  0.450, 0.275, EW, EH, "Committee accuracy", TEAL, fs=8.4, sub="0.5637 — looks strong")
c.box("sub",  0.450, 0.430, EW, EH, "Base rate on that subset", AMBER, fs=8.0, sub="0.5697 always-long")
c.box("out",  0.775, 0.352, EW, EH, "True edge  −0.59 pp", "#8FA3B8", tc=INK, fs=8.6,
      sub="the gain was the subset's own drift")
c.arrow("all","gate", s_side="B", d_side="T")
c.arrow("gate","tgc")
c.elbow("gate","sub", s_side="R", d_side="L", mid=0.310)
c.elbow("tgc","out",  s_side="R", d_side="L", mid=0.640, d_off=-0.26)
c.elbow("sub","out",  s_side="R", d_side="L", mid=0.640, d_off=+0.26)
c.note("Selecting bars changes the benchmark. Filtering to trend-quality bars raised the committee's accuracy to 0.5637, but it raised the always-long\n"
       "rule on those same bars to 0.5697 — so the apparent gain was entirely the base rate of the selected subset. Silver −1.74 pp, euro −6.05 pp.",
       y=0.108)
c.save(f"{OUT}/fig_base_rate")

# ============================================================ E3  significance battery
c = Canvas(13.0, 6.9, "Section 4.4 — Three significance tests, and why two of them can disagree",
           "The tests are not interchangeable: they resample different objects and score different losses")
W, H = 0.250, 0.082
C1, C2, C3 = 0.190, 0.500, 0.810
c.box("fc", 0.500, 0.868, 0.300, 0.066, "Frozen seed-9 forecasts", NAVY, fs=9.0,
      sub="never re-tuned after scoring")
c.box("bs", C1, 0.660, W, H, "Block bootstrap", TEAL, fs=9.0,
      sub="2,000 resamples · block length 50")
c.box("dm", C2, 0.660, W, H, "Diebold–Mariano", NAVY, fs=9.0,
      sub="Newey–West HAC · lag 10")
c.box("mcs", C3, 0.660, W, H, "Hansen Model Confidence Set", "#6D48C7", fs=8.2,
      sub="90% level")
c.elbow("fc","bs",  s_side="B", d_side="T", mid=0.790)
c.arrow("fc","dm",  s_side="B", d_side="T")
c.elbow("fc","mcs", s_side="B", d_side="T", mid=0.790)

c.box("bs2", C1, 0.500, W, 0.062, "scores the RANK metrics", TEAL, fs=8.0,
      sub="Spearman · large-move accuracy")
c.box("dm2", C2, 0.500, W, 0.062, "scores SQUARED ERROR", NAVY, fs=8.0, sub="loss differential")
c.box("mcs2", C3, 0.500, W, 0.062, "scores SQUARED ERROR", "#6D48C7", fs=8.0, sub="elimination on loss")
for a, b in [("bs","bs2"), ("dm","dm2"), ("mcs","mcs2")]:
    c.arrow(a, b, s_side="B", d_side="T")

c.box("q1", C1, 0.352, W, 0.070, "Does the model ORDER\nmove sizes better?", "#0F766E", fs=8.2)
c.box("q2", C2, 0.352, W, 0.070, "Does it reduce\nmean squared error?", "#8FA3B8", tc=INK, fs=8.2)
c.box("q3", C3, 0.352, W, 0.070, "Is it distinguishable\nfrom the best forecaster?", "#8FA3B8", tc=INK, fs=8.2)
for a, b in [("bs2","q1"), ("dm2","q2"), ("mcs2","q3")]:
    c.arrow(a, b, s_side="B", d_side="T")

c.band(0.045, 0.115, 0.910, 0.180, "#F4F7FB", "#E3EAF2")
c.label(0.500, 0.245, "Why they diverge on silver and euro", fs=9.0, color=NAVY, bold=True)
c.label(0.500, 0.175,
        "Squared error is dominated by a handful of extreme moves and is sensitive to the SCALE of the forecast; rank metrics are unit-free and depend only on ORDER.\n"
        "A model can order future magnitude substantially better without reducing squared error — so the bootstrap can be significant while DM and the MCS are not.",
        fs=8.0, color=INK)
c.note("All three tests are run on the same frozen forecast arrays, and each result is reproduction-guarded against the committed point estimate before it is reported.",
       y=0.042)
c.save(f"{OUT}/fig_significance")

# ============================================================ E4  conformal protocol
c = Canvas(12.6, 7.2, "Section 4.6 — Interval calibration: split conformal and the adaptive extension",
           "Split conformal assumes exchangeability; ACI drops that assumption and controls coverage online")
W, H = 0.215, 0.074

c.band(0.040, 0.560, 0.920, 0.310, "#F4F7FB", "#E3EAF2",
       "Split conformal — one fixed quantile, computed once")
c.box("cal", 0.155, 0.700, W, H, "Calibration split", "#8FA3B8", tc=INK, fs=8.4,
      sub="3,102 held-out origins")
c.box("res", 0.400, 0.700, W, H, "Normalised residuals", NAVY, fs=8.4, sub="|y − μ| / σ")
c.box("qhat", 0.645, 0.700, W, H, "Quantile q̂(1−α)", NAVY, fs=8.6, sub="one number per horizon")
c.box("band1", 0.870, 0.700, 0.150, H, "μ ± q̂·σ", GREEN, fs=8.8)
c.arrow("cal","res"); c.arrow("res","qhat"); c.arrow("qhat","band1")
c.label(0.500, 0.598, "valid only while test residuals are exchangeable with calibration residuals — which a volatility regime shift breaks",
        fs=7.8, color=AMBER, italic=True)

c.band(0.040, 0.170, 0.920, 0.355, "#FFF8F0", "#F3E4D2",
       "Adaptive conformal inference — the level itself is a controlled variable")
c.box("at",  0.185, 0.395, W, H, "Working level αₜ", AMBER, fs=8.6, sub="starts at the nominal α")
c.box("int", 0.470, 0.395, W, H, "Interval at αₜ", GREEN, fs=8.6, sub="μ ± q̂(1−αₜ)·σ")
c.box("obs", 0.755, 0.395, W, H, "Observe outcome", NAVY, fs=8.6, sub="errₜ = 1 if outside")
c.box("upd", 0.470, 0.245, W, H, "Update the level", AMBER, fs=8.4,
      sub="αₜ₊₁ = αₜ + γ(α − errₜ)")
c.arrow("at","int"); c.arrow("int","obs")
# down from the observation, then straight up into the update box's top edge
c.elbow("obs","upd", s_side="B", d_side="T", mid=0.312)
# feedback rides a bus down the left margin and enters the level box side-on
c.elbow("upd","at",  s_side="L", d_side="L", mid=0.058, label="feedback")
c.formula(0.500, 0.128, "a run of misses lowers αₜ, widening later intervals until empirical coverage recovers",
          w=0.740, h=0.046, fs=8.6)
c.note("The guarantee changes character: split conformal offers finite-sample coverage under exchangeability, ACI offers long-run average coverage without it.\n"
       "The price is a wider and occasionally infinite interval — and that infinite fraction is itself a usable regime-stress signal.",
       y=0.042)
c.save(f"{OUT}/fig_conformal_protocol")

print("evaluation figures written (PNG + editable SVG):")
for f in sorted(os.listdir(OUT)):
    if f.startswith(("fig_eval", "fig_base", "fig_signif", "fig_conformal_p")) and f.endswith(".svg"):
        print("   ", f)
