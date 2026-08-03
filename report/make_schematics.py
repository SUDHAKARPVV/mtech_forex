"""Redraw the schematic figures on a strict grid. Outputs PNG + editable SVG."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diagram_lib import *   # noqa

OUT = os.path.dirname(os.path.abspath(__file__)) + "/figs"
os.makedirs(OUT, exist_ok=True)

# ==================================================================== FIG 1 architecture
c = Canvas(13.6, 9.6,
           "Hybrid CNN–LSTM–Transformer: dual-tower fusion, expert blending and regime-aware heads",
           "Every box shows its output tensor · B = batch · T = 60 hourly bars · k = 10 forecast horizons")

# ---- ONE box size for every node; wide bars are exact multiples of it -------
W, H  = 0.160, 0.068                       # the only node size in this figure
COL   = [0.100, 0.300, 0.500, 0.700, 0.900]   # 5 columns, 0.040 clear between boxes
R1, R2, R3 = 0.842, 0.732, 0.622           # stage-1 rows  (0.042 clear for arrows)
R4, R5, R6 = 0.505, 0.385, 0.275           # stage-2 rows
R7         = 0.130                         # stage-3 row

c.band(0.020, 0.582, 0.960, 0.342, "#F4F7FB", "#E3EAF2", "Stage 1 · dual-tower encoding and fusion")
c.band(0.020, 0.230, 0.960, 0.345, "#F6F4FC", "#E7E2F5", "Stage 2 · global context")
c.band(0.020, 0.055, 0.960, 0.150, "#FFF8F0", "#F3E4D2", "Stage 3 · expert blending and probabilistic output")

# ---- stage 1 --------------------------------------------------------------
c.box("qin",   COL[0], R1, W, H, "Quant stream",        "#8FA3B8", tc=INK, fs=8.6, sub="(B, T, 24)")
c.box("qproj", COL[1], R1, W, H, "Linear projection",   TEAL,  fs=8.6, sub="24 → 64")
c.box("cnn",   COL[2], R1, W, H, "Dilated causal CNN",  TEAL,  fs=8.4, sub="3 blocks · d = 1, 2, 4")
c.box("fuse",  COL[3], R1, W, H, "Cross-attention",     GREEN, fs=8.6, sub="Q = quant · K,V = text")
c.box("dmod",  COL[4], R1, W, H, "LayerNorm",           GREEN, fs=8.6, sub="128 → 256")

c.box("rin",   COL[0], R2, W, H, "Regime context",      "#B9C6D4", tc=INK, fs=8.6, sub="(B, 2) vol, ATR")
c.box("remb",  COL[2], R2, W, H, "Regime embedding",    "#8FA3B8", tc=INK, fs=8.4, sub="2 → 128")

c.box("tin",   COL[0], R3, W, H, "Sentiment stream",    "#8FA3B8", tc=INK, fs=8.6, sub="(B, T, 13)")
c.box("tgru",  COL[1], R3, W, H, "Sentiment GRU",       PURPLE, fs=8.6, sub="13 → 64")
c.box("tproj", COL[2], R3, W, H, "Projection",          PURPLE, fs=8.6, sub="64 → 128")

# ---- stage 2 --------------------------------------------------------------
c.box("trf",  COL[2], R4, 0.560, H, "Causal Transformer encoder", NAVY, fs=9.4,
      sub="4 layers · 8 heads · FFN 1024 · (B, T, 256)")
c.box("lstm", COL[1], R5, W, H, "Bi-LSTM",           NAVY,  fs=8.6, sub="H = 128 / direction")
c.box("gru2", COL[3], R5, W, H, "Bi-GRU",            NAVY,  fs=8.6, sub="H = 128 / direction")
c.box("gate", COL[2], R6, W, H, "Learned gate",      AMBER, fs=8.6, sub="λ·LSTM + (1−λ)·GRU")
c.box("pool", COL[4], R6, W, H, "Attention pooling", NAVY,  fs=8.4, sub="→ (B, 256)")

# ---- stage 3 --------------------------------------------------------------
c.box("exp",   COL[0], R7, W, H, "External experts",   "#F2C14E", tc=INK, fs=8.4, sub="XGBoost · GARCH")
c.box("trust", COL[1], R7, W, H, "Trust gates",        AMBER, fs=8.6, sub="σ(W · regime)")
c.box("ctx",   COL[2], R7, W, H, "Context vector",     AMBER, fs=8.6, sub="(B, 352)")
c.box("heads", COL[3], R7, W, H, "Regime-aware heads", GREEN, fs=8.2, sub="stable ∥ high-vol")
c.box("out",   COL[4], R7, W, H, "μ and σ per horizon", GREEN, fs=8.2, sub="Gaussian NLL · (B, k)")

# ---- edges ---------------------------------------------------------------
c.arrow("qin","qproj");  c.arrow("qproj","cnn")
c.arrow("cnn","fuse");   c.arrow("fuse","dmod")
c.arrow("rin","remb", label="regime state")
c.arrow("remb","cnn", s_side="T", d_side="B")
c.ax.text(COL[2] + 0.052, (R1 + R2) / 2, "⊕", fontsize=11, color=INK,
          ha="center", va="center", fontweight="bold")
c.arrow("tin","tgru");   c.arrow("tgru","tproj")
c.elbow("tproj","fuse", s_side="R", d_side="L", mid=0.600, d_off=-0.32, label="K, V")
c.elbow("dmod","trf",   s_side="B", d_side="R", mid=0.560)
c.arrow("trf","lstm", s_side="B", d_side="T", s_off=-0.357)
c.arrow("trf","gru2", s_side="B", d_side="T", s_off=+0.357)
c.arrow("lstm","gate", s_side="B", d_side="T", d_off=-0.35)
c.arrow("gru2","gate", s_side="B", d_side="T", d_off=+0.35)
c.arrow("gate","pool")
c.elbow("pool","ctx", s_side="B", d_side="T", mid=0.220, label="deep context (B, 256)")
c.arrow("exp","trust"); c.arrow("trust","ctx")
c.arrow("ctx","heads"); c.arrow("heads","out")
c.note("Context vector = deep context (256) + raw macro/sentiment skip (32) + XGBoost embedding (32) + GARCH embedding (32)\n"
       "Nested convex blend:  GARCH ∘ (XGBoost ∘ deep)   ·   4,401,767 trainable parameters   ·   no pooling until the final attention pool",
       y=0.018)
c.save(f"{OUT}/fig_architecture")

# ==================================================================== FIG 2 data layer
c = Canvas(12.6, 7.0,
           "Data Layer: acquisition, scoring and leak-free alignment of three streams",
           "Each row is one independent stream; all three converge on a single aligned panel")
BW, BH = 0.200, 0.108
CX = [0.135, 0.395, 0.655]
RY = [0.735, 0.505, 0.275]

c.box("mt5",  CX[0], RY[0] + 0.055, BW, 0.082, "MetaTrader 5 terminal", TEAL, sub="read-only attach · live H1")
c.box("csv",  CX[0], RY[0] - 0.055, BW, 0.082, "MT5 CSV export", TEAL, sub="genuine H1, 2010 → present")
c.box("route",CX[1], RY[0], BW, BH, "Price source router", TEAL, sub="csv | live | auto")
c.box("tech", CX[2], RY[0], BW, BH, "18 technical features", TEAL,
      sub="RSI · MACD · Bollinger\nATR% · envelope · drift t-stat")

c.box("news", CX[0], RY[1], BW, BH, "GDELT · Google News · RSS", PURPLE, fs=8.5,
      sub="historical depth + fresh headlines")
c.box("fin",  CX[1], RY[1], BW, BH, "FinBERT scorer", PURPLE,
      sub="per-headline polarity\n+ confidence, cached")
c.box("sent", CX[2], RY[1], BW, BH, "13 sentiment features", PURPLE,
      sub="rolling stats · diffusion\nbreadth · 4 signal one-hots")

c.box("macro",CX[0], RY[2], BW, BH, "Yahoo Finance · US BLS", AMBER, sub="^IRX · ^TNX · DXY · CPI")
c.box("stat", CX[1], RY[2], BW, BH, "Stationary transforms", AMBER, sub="z-score · Δ · log returns")
c.box("mac6", CX[2], RY[2], BW, BH, "6 macro features", AMBER, sub="shifted +1 day\n(no look-ahead)")

c.box("panel",0.900, RY[1], 0.165, 0.230, "Aligned\nfeature panel", NAVY, fs=9.6,
      sub="\n37 features × 60-bar window\nchronological 70 / 15 / 15 split\ntrain-only normalisation")

c.elbow("mt5","route", s_side="R", d_side="L", mid=0.262)
c.elbow("csv","route", s_side="R", d_side="L", mid=0.262)
c.arrow("route","tech")
c.arrow("news","fin");   c.arrow("fin","sent")
c.arrow("macro","stat"); c.arrow("stat","mac6")
# all three streams enter the panel's LEFT edge in parallel, at three heights
c.elbow("tech","panel", s_side="R", d_side="L", mid=0.800, d_off=+0.33)
c.arrow("sent","panel", s_side="R", d_side="L")
c.elbow("mac6","panel", s_side="R", d_side="L", mid=0.800, d_off=-0.33)
c.note("Leak controls:  macro releases shifted +1 day before touching a bar  ·  news aligned on publication timestamp only\n"
       "normalisation statistics computed on the training split alone  ·  walk-forward re-fitting for every classical baseline",
       y=0.045)
c.save(f"{OUT}/fig_data_layer")

# ==================================================================== FIG 3 design overview
c = Canvas(11.8, 6.4, "Layered system design",
           "Each layer consumes only the layer below it")
LW, LH = 0.215, 0.115
BX, BW2 = 0.285, 0.690
rows = [("Presentation Layer", 0.800, GREEN,
         "Streamlit dashboard · live forecast with adaptive-conformal band ·\ndata-lineage view · per-stage timing breakdown"),
        ("Evaluation Layer",   0.630, NAVY,
         "base-rate control · 3-seed stability · block bootstrap ·\nDiebold–Mariano · Hansen MCS · conformal coverage"),
        ("Modelling Layer",    0.460, TEAL,
         "dual-tower Hybrid CNN–LSTM–Transformer · XGBoost and GARCH\nexperts · regime-aware Gaussian heads"),
        ("Processing Layer",   0.290, PURPLE,
         "technical indicators · FinBERT scoring and caching ·\nstationary macro transforms · leak-free alignment"),
        ("Data Layer",         0.120, AMBER,
         "MetaTrader 5 (live + CSV export) · GDELT / Google News / RSS ·\nYahoo Finance · US BLS CPI")]
for i, (name, y, col, desc) in enumerate(rows):
    c.box(f"L{i}", 0.145, y, LW, LH, name, col, fs=9.8)
    c.ax.add_patch(FancyBboxPatch((BX, y - LH / 2), BW2, LH,
                   boxstyle="round,pad=0,rounding_size=0.014",
                   fc="#F8FAFC", ec=col, lw=1.3, zorder=2))
    c.ax.text(BX + 0.022, y, desc, ha="left", va="center",
              fontsize=FS_SUB + 0.4, color=INK, zorder=3, linespacing=1.55)
for i in range(len(rows) - 1):
    c.arrow(f"L{i+1}", f"L{i}", s_side="T", d_side="B", color="#A9B6C6")
c.save(f"{OUT}/fig_design_overview")

print("schematics rewritten (PNG + editable SVG):")
for f in sorted(os.listdir(OUT)):
    if f.endswith(".svg"): print("   ", f)
