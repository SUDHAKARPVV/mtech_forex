"""Diagrams for Sections 6 and 7. PNG + editable SVG."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diagram_lib import *   # noqa

OUT = os.path.dirname(os.path.abspath(__file__)) + "/figs"
os.makedirs(OUT, exist_ok=True)

# ============================================================ F1  roadmap
c = Canvas(13.0, 7.1, "Section 6 — Forward programme, ordered by the strength of the evidence behind it",
           "The measured results decide the priority: work on the axis that was shown to carry signal, not the one that was hoped to")
W, H = 0.250, 0.106          # tall enough for a two-line sub-caption
C1, C2, C3 = 0.185, 0.500, 0.815

c.band(0.035, 0.282, 0.300, 0.590, "#EAF5F4", "#BFDDDA",
       "Lane 1 · evidence already in hand")
c.band(0.350, 0.282, 0.300, 0.590, "#F6F4FC", "#DCD3F2",
       "Lane 2 · plausible, not yet tested")
c.band(0.665, 0.282, 0.300, 0.590, "#F5F6F8", "#DCE1E8",
       "Lane 3 · blocked on data access")

R = [0.752, 0.622, 0.492, 0.362]
c.box("a1", C1, R[0], W, H, "Extend ACI to silver and euro", GREEN, fs=8.2,
      sub="the layer is fitted for gold only;\ncoverage is the most robust result")
c.box("a2", C1, R[1], W, H, "Volatility-targeted sizing", GREEN, fs=8.4,
      sub="magnitude is the predictable axis,\nso size positions from interval width")
c.box("a3", C1, R[2], W, H, "Attention and trust-gate readout", GREEN, fs=8.0,
      sub="the gates are already interpretable;\nthis is instrumentation, not modelling")
c.box("a4", C1, R[3], W, H, "Per-instrument conformal study", GREEN, fs=8.0,
      sub="compare width and stress across pairs")

c.box("b1", C2, R[0], W, H, "Long-context statement encoding", PURPLE, fs=8.0,
      sub="tests whether the null sentiment result\nis about markets or about headlines")
c.box("b2", C2, R[1], W, H, "Lower-frequency macro study", PURPLE, fs=8.2,
      sub="the ablation is an H1 result; macro\nmay act over days rather than hours")
c.box("b3", C2, R[2], W, H, "Cross-instrument transfer", PURPLE, fs=8.4,
      sub="does silver's volatility structure\ntransfer to gold or euro?")
c.box("b4", C2, R[3], W, H, "RL execution layer", PURPLE, fs=8.4,
      sub="beyond the supervised scope\nof this dissertation")

c.box("c1", C3, R[0], W, H, "Order-flow / depth of market", "#8FA3B8", tc=INK, fs=8.2,
      sub="no consolidated book exists for spot\nmetals and FX; MT5 depth is live-only")
c.box("c2", C3, R[1], W, H, "Consolidated tape", "#8FA3B8", tc=INK, fs=8.4,
      sub="would require a commercial licence")
c.box("c3", C3, R[2], W, H, "Tick-level microstructure", "#8FA3B8", tc=INK, fs=8.2,
      sub="storage and licensing cost beyond\nthe scope of a dissertation")
c.label(C3, R[3], "These stay closed until the data\nbecomes available — they are recorded\nso the gap is explicit, not forgotten.",
        fs=8.0, color=GREY, italic=True)

c.label(C1, 0.240, "Do next", fs=9.4, color=GREEN, bold=True)
c.label(C2, 0.240, "Worth testing", fs=9.4, color=PURPLE, bold=True)
c.label(C3, 0.240, "Cannot start", fs=9.4, color=GREY, bold=True)
c.note("Lane 1 items follow directly from measured results: magnitude and interval calibration are where this system was shown to add value.\n"
       "Lane 2 items would each test a specific alternative explanation for a null result rather than simply adding capacity to the model.",
       y=0.130)
c.save(f"{OUT}/fig_roadmap")

# ============================================================ F2  claims and evidence
c = Canvas(13.2, 7.2, "Section 7 — The three claims, the evidence behind each, and how strongly each is held",
           "Every claim is stated with the scope that the evidence actually supports")
BW, BH = 0.215, 0.088
CX = [0.150, 0.415, 0.680, 0.910]
RY = [0.760, 0.545, 0.330]

c.label(CX[0], 0.878, "CLAIM", fs=8.6, color=GREY, bold=True)
c.label(CX[1], 0.878, "EVIDENCE", fs=8.6, color=GREY, bold=True)
c.label(CX[2], 0.878, "WHAT WOULD OVERTURN IT", fs=8.6, color=GREY, bold=True)
c.label(CX[3], 0.878, "STRENGTH", fs=8.6, color=GREY, bold=True)

rows = [
    ("d", RY[0], NAVY,
     "Hourly direction is\nnot forecastable",
     "3 instruments × 3 seeds ×\n~15 framings, every one at or\nbelow its own base rate",
     "A framing clearing the base rate\non the same bars it selects,\nreplicated across seeds",
     "STRONG", GREEN),
    ("m", RY[1], TEAL,
     "The hybrid orders move\nmagnitude better than\nATR% and GARCH-σ",
     "3/3 seeds on all pairs;\nbootstrap significant on silver\nand euro, not on gold",
     "A squared-error test separating\nthe models the other way, or\nfailure to replicate out of sample",
     "QUALIFIED", AMBER),
    ("c", RY[2], PURPLE,
     "Adaptive conformal\ninference restores\nhonest coverage",
     "79.9 / 90.0 / 95.0% against\nnominal, from 63.3 / 72.9 / 79.0%\nunder the Gaussian band",
     "Coverage failing on an instrument\nother than gold, where the layer\nis not yet fitted",
     "STRONG", GREEN),
]
for key, y, col, claim, ev, ov, strength, scol in rows:
    c.box(f"{key}1", CX[0], y, BW, BH, "", col, fs=8.2)
    c.label(CX[0], y, claim, fs=8.4, color="white", bold=True)
    c.box(f"{key}2", CX[1], y, BW, BH, "", "#F4F7FB", tc=INK, fs=7.8, ec="#D6DEE7", lw=1.0)
    c.label(CX[1], y, ev, fs=7.8, color=INK)
    c.box(f"{key}3", CX[2], y, BW, BH, "", "#F4F7FB", tc=INK, fs=7.6, ec="#D6DEE7", lw=1.0)
    c.label(CX[2], y, ov, fs=7.6, color=INK)
    c.box(f"{key}4", CX[3], y, 0.130, BH * 0.62, strength, scol, fs=8.6)
    c.arrow(f"{key}1", f"{key}2"); c.arrow(f"{key}2", f"{key}3"); c.arrow(f"{key}3", f"{key}4")

c.band(0.045, 0.070, 0.910, 0.175, "#F4F7FB", "#E3EAF2")
c.label(0.500, 0.196, "Why the negative result carries as much weight as the positive one", fs=9.0, color=NAVY, bold=True)
c.label(0.500, 0.128,
        "The same architecture, features, test bars and protocol produced the negative directional result and the positive magnitude result. A broken pipeline, an\n"
        "inadequate model or a mis-built test set would have suppressed both. That the two disagree is what makes each of them credible on its own terms.",
        fs=8.2, color=INK)
c.save(f"{OUT}/fig_claims")

print("final figures written (PNG + editable SVG):")
for f in sorted(os.listdir(OUT)):
    if f.startswith(("fig_roadmap", "fig_claims")) and f.endswith(".svg"):
        print("   ", f)
