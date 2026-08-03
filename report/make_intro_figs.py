"""Diagrams for Sections 1 and 2. PNG + editable SVG."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diagram_lib import *   # noqa

OUT = os.path.dirname(os.path.abspath(__file__)) + "/figs"
os.makedirs(OUT, exist_ok=True)

# ============================================================ I1  study at a glance
c = Canvas(13.0, 7.0, "Section 1 — The study at a glance",
           "Three instruments, one decade, two forecasting axes, and the controls that decide what counts as a result")

# ---- instruments ----------------------------------------------------------
c.band(0.035, 0.585, 0.930, 0.290, "#F4F7FB", "#E3EAF2",
       "Instruments — each with an entirely independent pipeline, archive and checkpoint")
IW, IH = 0.270, 0.158
for key, cx, name, sub in [
        ("g", 0.180, "Gold  ·  XAU/USD", "62,049 hourly bars\n22,833 scored headlines\n9,297 test origins"),
        ("s", 0.500, "Silver  ·  XAG/USD", "62,328 hourly bars\n11,413 scored headlines\n9,339 test origins"),
        ("e", 0.820, "Euro  ·  EUR/USD", "65,587 hourly bars\n10,605 scored headlines\n9,828 test origins")]:
    c.box(key, cx, 0.700, IW, IH, name, TEAL, fs=9.4, sub=sub)

# ---- the two axes ---------------------------------------------------------
AW, AH = 0.400, 0.115
c.box("dir", 0.255, 0.440, AW, AH, "Axis 1 — direction of the next move", NAVY, fs=9.0,
      sub="measured against the always-up base rate")
c.box("mag", 0.735, 0.440, AW, AH, "Axis 2 — magnitude of the next move", GREEN, fs=9.0,
      sub="measured against ATR% and GARCH-σ")
c.label(0.495, 0.440, "and", fs=8.4, color=GREY, italic=True)

# ---- the spine ------------------------------------------------------------
SW, SH = 0.205, 0.092
c.box("d1", 0.150, 0.268, SW, SH, "60-bar window", "#8FA3B8", tc=INK, fs=8.6,
      sub="37 features, 3 streams")
c.box("d2", 0.383, 0.268, SW, SH, "10-step horizon", "#8FA3B8", tc=INK, fs=8.6,
      sub="multi-step, not one-step")
c.box("d3", 0.616, 0.268, SW, SH, "3 random seeds", "#8FA3B8", tc=INK, fs=8.6,
      sub="9, 36 and 99")
c.box("d4", 0.849, 0.268, SW, SH, "Frozen test split", "#8FA3B8", tc=INK, fs=8.6,
      sub="most recent 15%, in time order")
for a, b in [("d1","d2"), ("d2","d3"), ("d3","d4")]:
    c.arrow(a, b)

# ---- out of scope ---------------------------------------------------------
c.band(0.035, 0.070, 0.930, 0.130, "#FDF6F0", "#F0DCC8",
       "Deliberately out of scope")
c.label(0.500, 0.118,
        "order execution and latency-sensitive high-frequency trading   ·   portfolio construction   ·   transaction costs, spread and slippage\n"
        "order-flow and depth-of-market features (no obtainable historical source)   ·   any claim of achievable trading return",
        fs=8.2, color=INK)
c.save(f"{OUT}/fig_study_scope")

# ============================================================ I2  gaps in the literature
c = Canvas(13.2, 7.1, "Section 2 — Four gaps in the reviewed literature, and the component that closes each",
           "The architecture and the evaluation protocol are both answers to specific weaknesses in prior work")
GW, GH = 0.300, 0.115
RW = 0.330
CG, CC, CE = 0.190, 0.560, 0.878
RY = [0.760, 0.585, 0.410, 0.235]

c.label(CG, 0.868, "GAP IN THE LITERATURE", fs=8.6, color=GREY, bold=True)
c.label(CC, 0.868, "COMPONENT THAT CLOSES IT", fs=8.6, color=GREY, bold=True)
c.label(CE, 0.868, "WHERE", fs=8.6, color=GREY, bold=True)

rows = [
    ("g1", RY[0], "Single-purpose pipelines —\nCNN, recurrence, attention and\nsentiment treated separately",
     "One unified dual-tower architecture:\nCNN → cross-attention → Transformer →\ngated recurrence → expert blend", "§ 3.1", TEAL),
    ("g2", RY[1], "Single-step forecasting —\nerror compounding across\nhorizons left unexamined",
     "Ten-step direct multi-horizon output,\nwith a mean and a variance emitted\nper horizon", "§ 3.1.8", GREEN),
    ("g3", RY[2], "Accuracy reported without\nthe base rate of the test\nwindow, and without a test",
     "Base-rate control on every claim, three\nseeds, block bootstrap, Diebold–Mariano\nand the Model Confidence Set", "§ 4.2, 4.4", NAVY),
    ("g4", RY[3], "Uncertainty bands never\nchecked against their\nnominal coverage",
     "Adaptive conformal inference with\nmeasured empirical coverage, deployed\nlive rather than only reported", "§ 4.6, 5.4", PURPLE),
]
for key, y, gap, comp, where, col in rows:
    c.box(f"{key}a", CG, y, GW, GH, "", "#F4F7FB", tc=INK, ec="#D6DEE7", lw=1.0)
    c.label(CG, y, gap, fs=8.0, color=INK)
    c.box(f"{key}b", CC, y, RW, GH, "", col, tc="white")
    c.label(CC, y, comp, fs=8.0, color="white", bold=True)
    c.box(f"{key}c", CE, y, 0.140, GH * 0.55, where, "#8FA3B8", tc=INK, fs=8.6)
    c.arrow(f"{key}a", f"{key}b"); c.arrow(f"{key}b", f"{key}c")

c.note("Each gap was identified during the literature review and each is answered by a specific, named component rather than by the architecture as a whole.\n"
       "Gaps three and four are methodological rather than architectural, and it is those two that produced the negative results reported in Section 5.",
       y=0.075)
c.save(f"{OUT}/fig_gaps")

print("introduction figures written (PNG + editable SVG):")
for f in sorted(os.listdir(OUT)):
    if f.startswith(("fig_study_scope", "fig_gaps")) and f.endswith(".svg"):
        print("   ", f)
