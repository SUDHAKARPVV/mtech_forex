"""Per-layer architecture figures for Section 3. One uniform box size per figure,
edge-clipped arrows, PNG + editable SVG."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diagram_lib import *   # noqa

OUT = os.path.dirname(os.path.abspath(__file__)) + "/figs"

# ============================================================ L1  dilated causal CNN
c = Canvas(12.4, 7.6, "Layer 3.1.4 — Dilated causal convolution stack",
           "Left-only padding keeps the layer strictly causal; dilation 1-2-4 grows the receptive field to 15 bars without pooling")
N, X0, X1 = 15, 0.115, 0.885
xs = [X0 + i * (X1 - X0) / (N - 1) for i in range(N)]
rows = [("input  (B, T, 64)", 0.845, LIGHT),
        ("block 1 · d = 1", 0.735, TEAL),
        ("block 2 · d = 2", 0.625, TEAL),
        ("block 3 · d = 4", 0.515, TEAL)]
for name, y, col in rows:
    c.label(0.058, y, name, fs=7.4, ha="center", color=INK, bold=(col is not LIGHT))
    for x in xs:
        c.dot(x, y, r=0.0062, fc="white", ec="#B9C6D4", lw=1.0)
# Trace the receptive field of the LAST output position BACKWARDS through the
# stack: block3[t] <- block2[t, t-4, t-8] <- block1[.. -0,-2,-4] <- input[.. -0,-1,-2].
# (Row 0 is the input at the top; row 3 is the deepest block at the bottom.)
taps = {1: [0, 1, 2], 2: [0, 2, 4], 3: [0, 4, 8]}
cur = {N - 1}
for li in (3, 2, 1):                      # deepest block first, walking upward
    y_to, y_fr = rows[li][1], rows[li - 1][1]
    src = set()
    for i in sorted(cur):
        c.dot(xs[i], y_to, r=0.0068, fc=TEAL, ec=TEAL)
        for d in taps[li]:
            j = i - d
            if j >= 0:
                c.line(xs[j], y_fr, xs[i], y_to, color=TEAL, lw=1.0, z=2,
                       alpha=0.30 if li == 1 else 0.55)
                src.add(j)
    for j in sorted(src):
        c.dot(xs[j], y_fr, r=0.0068,
              fc="#7FB6BD" if li == 1 else TEAL, ec=TEAL)
    cur = src
c.label((xs[0] + xs[-1]) / 2, 0.452, "receptive field of one output position = 1 + 2(1 + 2 + 4) = 15 bars",
        fs=8.2, color=TEAL, bold=True)
c.line(xs[0], 0.478, xs[-1], 0.478, color=TEAL, lw=1.3)
for x in (xs[0], xs[-1]):
    c.line(x, 0.470, x, 0.486, color=TEAL, lw=1.3)
c.label(xs[-1], 0.878, "t", fs=7.6, color=INK, bold=True)
c.label(xs[0], 0.878, "t − 14", fs=7.6, color=INK, bold=True)

W, H = 0.165, 0.070
COL = [0.135, 0.330, 0.525, 0.720, 0.915]
RY = 0.245
c.band(0.030, 0.150, 0.945, 0.185, "#F4F7FB", "#E3EAF2", "Block chain — sequence length preserved at every step")
c.box("i",  COL[0], RY, W, H, "Input", LIGHT, tc=INK, fs=8.8, sub="(B, T, 64)")
c.box("b1", COL[1], RY, W, H, "Causal block 1", TEAL, fs=8.6, sub="k=3 · d=1 · pad 2")
c.box("b2", COL[2], RY, W, H, "Causal block 2", TEAL, fs=8.6, sub="k=3 · d=2 · pad 4")
c.box("b3", COL[3], RY, W, H, "Causal block 3", TEAL, fs=8.6, sub="k=3 · d=4 · pad 8")
c.box("o",  COL[4], RY, W, H, "Output", NAVY, fs=8.8, sub="(B, T, 128)")
for a, b in (("i","b1"),("b1","b2"),("b2","b3"),("b3","o")):
    c.arrow(a, b)
c.note("Each block is Conv1d → BatchNorm → ReLU.  Padding is applied on the LEFT only, so position t is computed from positions ≤ t —\n"
       "the layer cannot see its own future, and no pooling is used, so all 60 bars survive into the attention stage.", y=0.055)
c.save(f"{OUT}/fig_layer_cnn")

# ============================================================ L2  cross-attention fusion
c = Canvas(12.4, 7.4, "Layer 3.1.3 — Cross-attention fusion of the price and news towers",
           "The price stream asks the questions; the news stream supplies the answers — and a presence gate decides how much of the answer is used")
W, H = 0.185, 0.072
CA, CB, CC, CD = 0.135, 0.375, 0.615, 0.865
RQ, RK, RG = 0.775, 0.600, 0.425
c.box("q",   CA, RQ, W, H, "Quant local", TEAL, fs=8.8, sub="(B, T, 128) from the CNN")
c.box("wq",  CB, RQ, W, H, "Linear → Q", TEAL, fs=8.8, sub="queries")
c.box("t",   CA, RK, W, H, "Text sequence", PURPLE, fs=8.8, sub="(B, T, 128) from the GRU")
c.box("wkv", CB, RK, W, H, "Linear → K, V", PURPLE, fs=8.8, sub="keys and values")
c.box("attn",CC, 0.688, W, H, "Multi-head attention", GREEN, fs=8.4, sub="4 heads · softmax(QKᵀ/√d)·V")
c.box("raw", CA, RG, W, H, "Raw text features", "#B9C6D4", tc=INK, fs=8.6, sub="(B, T, 13)")
c.box("gate",CB, RG, W, H, "Presence gate", AMBER, fs=8.8, sub="σ(W · text) ∈ [0, 1]")
c.box("mul", CC, RG, W, H, "Scale attention", AMBER, fs=8.6, sub="gate ⊙ attention output")
c.box("add", CD, 0.560, W, H, "Residual + LayerNorm", GREEN, fs=8.0, sub="(B, T, 128) fused")
c.arrow("q","wq"); c.arrow("t","wkv"); c.arrow("raw","gate"); c.arrow("gate","mul")
c.elbow("wq","attn",  s_side="R", d_side="L", mid=0.505, d_off=+0.28, label="Q")
c.elbow("wkv","attn", s_side="R", d_side="L", mid=0.505, d_off=-0.28, label="K, V")
c.elbow("attn","mul", s_side="B", d_side="T", mid=0.560)
c.elbow("mul","add",  s_side="R", d_side="L", mid=0.745, d_off=-0.28)
c.elbow("q","add",    s_side="T", d_side="T", mid=0.865, label="residual path")
c.formula(0.500, 0.285, "fused  =  LayerNorm( local  +  σ(W·text) ⊙ CrossAttention(local, text, text) )", w=0.760, h=0.056, fs=9.4)
c.note("When a bar carries no headlines the gate closes and the fusion degrades gracefully to the price representation alone.\n"
       "During training the entire text stream is zeroed for a random 40% of samples (modality masking), so the model never becomes dependent on news.", y=0.115)
c.save(f"{OUT}/fig_layer_fusion")

# ============================================================ L3  transformer encoder layer
c = Canvas(12.4, 7.6, "Layer 3.1.5 — One causal Transformer encoder layer (×4)",
           "Pre-norm residual design; the causal mask makes training-time and inference-time computation identical")
W, H = 0.200, 0.068
CX, RX = 0.300, [0.815, 0.700, 0.585, 0.470, 0.355, 0.240]
c.box("x",   CX, RX[0], W, H, "Input sequence", LIGHT, tc=INK, fs=8.8, sub="(B, T, 256)")
c.box("n1",  CX, RX[1], W, H, "LayerNorm", "#8FA3B8", tc=INK, fs=8.8)
c.box("mha", CX, RX[2], W, H, "Masked multi-head attention", NAVY, fs=8.0, sub="8 heads · d_head = 32")
c.box("a1",  CX, RX[3], W, H, "Residual add", AMBER, fs=8.8, sub="x + attention(·)")
c.box("n2",  CX, RX[4], W, H, "LayerNorm", "#8FA3B8", tc=INK, fs=8.8)
c.box("ffn", CX, RX[5], W, H, "Feed-forward", NAVY, fs=8.8, sub="256 → 1024 → 256, GELU")
c.box("a2",  0.560, RX[5], W, H, "Residual add", AMBER, fs=8.8, sub="→ (B, T, 256)")
for a, b in (("x","n1"),("n1","mha"),("mha","a1"),("a1","n2"),("n2","ffn")):
    c.arrow(a, b, s_side="B", d_side="T")
c.arrow("ffn","a2")
c.elbow("x","a1",  s_side="R", d_side="R", mid=0.445, label="skip")
c.elbow("a1","a2", s_side="R", d_side="T", mid=0.560, label="skip")
# causal mask
c.label(0.800, 0.845, "Causal attention mask", fs=9.0, bold=True, color=NAVY)
c.matrix(0.715, 0.815, 8, 0.021, causal=True)
c.label(0.800, 0.615, "row = query position t\ncolumn = key position ≤ t", fs=7.2, color=GREY)
c.label(0.800, 0.545, "filled = attention permitted", fs=7.2, color=GREY)
c.formula(0.800, 0.430, "Attention(Q,K,V) = softmax( QKᵀ / √d_head + M ) V", w=0.360, h=0.050, fs=8.4)
c.label(0.800, 0.360, "M is 0 on and below the diagonal\nand −∞ above it", fs=7.2, color=GREY)
c.note("Four such layers are stacked. Pre-norm residuals keep a direct gradient path through the stack, and the √d_head scaling\n"
       "prevents the dot products from saturating the softmax as head width grows. The time axis is never collapsed here.", y=0.075)
c.save(f"{OUT}/fig_layer_transformer")

# ============================================================ L4  parallel recurrent
c = Canvas(12.4, 6.6, "Layer 3.1.6 — Parallel gated recurrent stage and attention pooling",
           "Two recurrent inductive biases are run in parallel and mixed by a learned scalar, rather than choosing one in advance")
W, H = 0.165, 0.070
C1, C2, C3, C4, C5 = 0.110, 0.315, 0.520, 0.725, 0.912
RT, RB, RM = 0.800, 0.615, 0.7075          # top branch, bottom branch, spine
RL = 0.430                                  # lower row
c.box("in", C1, RM, W, H, "Transformer output", NAVY, fs=8.2, sub="(B, T, 256)")
c.box("lf", C2, RT, W, H, "Bi-LSTM", NAVY, fs=8.8, sub="forward + backward, H = 128")
c.box("gf", C2, RB, W, H, "Bi-GRU", NAVY, fs=8.8, sub="forward + backward, H = 128")
c.box("lc", C3, RT, W, H, "Concatenate", "#8FA3B8", tc=INK, fs=8.6, sub="(B, T, 256)")
c.box("gc", C3, RB, W, H, "Concatenate", "#8FA3B8", tc=INK, fs=8.6, sub="(B, T, 256)")
c.box("gate", C4, RM, W, H, "Learned gate", AMBER, fs=8.6, sub="λ = σ(W·[meanL, meanG])")
c.box("mix",  C5, RM, W, H, "Convex mixture", AMBER, fs=8.2, sub="λ·LSTM + (1−λ)·GRU")
c.box("pool", C4, RL, W, H, "Attention pooling", NAVY, fs=8.4, sub="learned query over T")
c.box("ctx",  C5, RL, W, H, "Deep context", GREEN, fs=8.8, sub="(B, 256)")
c.arrow("in","lf", s_side="R", d_side="L", rad=0.10)
c.arrow("in","gf", s_side="R", d_side="L", rad=-0.10)
c.arrow("lf","lc"); c.arrow("gf","gc")
c.elbow("lc","gate", s_side="R", d_side="L", mid=0.622, d_off=+0.26)
c.elbow("gc","gate", s_side="R", d_side="L", mid=0.622, d_off=-0.26)
c.arrow("gate","mix")
c.elbow("mix","pool", s_side="B", d_side="T", mid=0.560)
c.arrow("pool","ctx")
c.formula(0.500, 0.235, "temporal = λ · BiLSTM(x) + (1 − λ) · BiGRU(x)      context = Σₜ αₜ · temporalₜ ,   α = softmax(w·temporal)",
          w=0.860, h=0.054, fs=8.8)
c.note("The gate is computed from the mean-pooled state of each branch, so the mixture adapts to the instrument and the regime.\n"
       "Attention pooling then decides which of the 60 bars matter, rather than privileging the most recent one.", y=0.085)
c.save(f"{OUT}/fig_layer_recurrent")

# ============================================================ L5  expert fusion
c = Canvas(12.4, 7.0, "Layer 3.1.7 — External expert fusion with volatility-conditioned trust gates",
           "Classical forecasters are fused into the network, not merely compared against it")
W, H = 0.180, 0.070
C1, C2, C3, C4 = 0.130, 0.350, 0.570, 0.820
RA, RB, RC = 0.790, 0.640, 0.470
c.box("xgb", C1, RA, W, H, "XGBoost expert", "#F2C14E", tc=INK, fs=8.6, sub="walk-forward · (B, k)")
c.box("gar", C1, RB, W, H, "GARCH expert", "#F2C14E", tc=INK, fs=8.6, sub="walk-forward · (B, k)")
c.box("reg", C1, RC, W, H, "Regime context", "#B9C6D4", tc=INK, fs=8.6, sub="(B, 2) vol, ATR")
c.box("nx",  C2, RA, W, H, "Norm + dropout", AMBER, fs=8.6, sub="→ Linear k → 32")
c.box("ng",  C2, RB, W, H, "Norm + dropout", AMBER, fs=8.6, sub="→ Linear k → 32")
c.box("tg",  C2, RC, W, H, "Trust gates", AMBER, fs=8.6, sub="σ(W · regime) → 2 × (B, k)")
c.box("ex",  C3, RA, W, H, "XGB embedding", AMBER, fs=8.6, sub="(B, 32), scaled by trust")
c.box("eg",  C3, RB, W, H, "GARCH embedding", AMBER, fs=8.4, sub="(B, 32), scaled by trust")
c.box("ctx", C4, 0.715, W, H, "Into context vector", GREEN, fs=8.2, sub="concatenated (B, 352)")
c.box("bl",  C4, RC, W, H, "Nested convex blend", NAVY, fs=8.2, sub="final forecast (B, k)")
c.arrow("xgb","nx"); c.arrow("gar","ng"); c.arrow("reg","tg")
c.arrow("nx","ex");  c.arrow("ng","eg")
# the trust signal rides a vertical bus in the clear gap between column 2 and 3,
# so it reaches both embeddings without crossing the two feed-forward arrows
c.elbow("tg","eg", s_side="R", d_side="L", mid=0.458, d_off=-0.30, label="trust")
c.elbow("tg","ex", s_side="R", d_side="L", mid=0.466, d_off=-0.30)
c.elbow("tg","bl", s_side="R", d_side="L", mid=0.700)
c.elbow("ex","ctx", s_side="R", d_side="L", mid=0.700, d_off=+0.26)
c.elbow("eg","ctx", s_side="R", d_side="L", mid=0.700, d_off=-0.26)
c.formula(0.500, 0.275, "inner = t_xgb · XGB + (1 − t_xgb) · deep          forecast = t_garch · GARCH + (1 − t_garch) · inner",
          w=0.820, h=0.052, fs=8.8)
c.note("Because both stages are convex combinations, the worst case is deferral to the strongest single expert — the fusion\n"
       "cannot make the model worse than its best component. A deep-supervision term keeps the deep branch independently accurate.", y=0.110)
c.save(f"{OUT}/fig_layer_experts")

# ============================================================ L6  regime-aware heads
c = Canvas(12.4, 7.2, "Layer 3.1.8 — Regime-aware probabilistic output heads",
           "Two specialised decoders are blended continuously by volatility, and each emits a mean and a variance")
W, H = 0.185, 0.072
C1, C2, C3, C4 = 0.125, 0.360, 0.605, 0.860
c.box("ctx", C1, 0.680, W, H, "Context vector", AMBER, fs=8.8, sub="(B, 352)")
c.box("reg", C1, 0.455, W, H, "Regime context", "#B9C6D4", tc=INK, fs=8.6, sub="(B, 2) vol, ATR")
c.box("hs",  C2, 0.795, W, H, "Stable-regime head", GREEN, fs=8.2, sub="MLP → μ, log σ²")
c.box("hv",  C2, 0.585, W, H, "High-volatility head", GREEN, fs=8.0, sub="MLP → μ, log σ²")
c.box("g",   C2, 0.375, W, H, "Soft regime gate", AMBER, fs=8.4, sub="g = σ(W · regime) ∈ [0,1]")
c.box("mix", C3, 0.680, W, H, "Continuous blend", AMBER, fs=8.4, sub="(1−g)·stable + g·high-vol")
c.box("mu",  C4, 0.790, W, H, "Mean μ", NAVY, fs=8.8, sub="(B, k) log-return")
c.box("sd",  C4, 0.570, W, H, "Band σ", NAVY, fs=8.8, sub="exp(½ log σ²) · (B, k)")
c.arrow("ctx","hs", s_side="R", d_side="L", rad=0.12)
c.arrow("ctx","hv", s_side="R", d_side="L", rad=-0.06)
c.arrow("reg","g")
c.elbow("hs","mix", s_side="R", d_side="L", mid=0.487, d_off=+0.28)
c.elbow("hv","mix", s_side="R", d_side="L", mid=0.487, d_off=-0.28)
c.elbow("g","mix",  s_side="T", d_side="B", mid=0.520, label="g")
c.elbow("mix","mu", s_side="R", d_side="L", mid=0.740)
c.elbow("mix","sd", s_side="R", d_side="L", mid=0.740)
c.formula(0.500, 0.245, "L_NLL  =  ½ Σₕ [ exp(−log σ²ₕ) · (yₕ − μₕ)²  +  log σ²ₕ ]", w=0.620, h=0.056, fs=9.6)
c.note("The Gaussian negative log-likelihood is what makes the model probabilistic rather than a point predictor: over-confidence is punished\n"
       "by the squared-error term and under-confidence by the log-variance term, so σ must widen when the model is genuinely uncertain.\n"
       "This σ is the quantity later re-calibrated by adaptive conformal inference in Section 5.4.", y=0.085)
c.save(f"{OUT}/fig_layer_heads")

print("layer figures written (PNG + editable SVG):")
for f in sorted(os.listdir(OUT)):
    if f.startswith("fig_layer") and f.endswith(".svg"):
        print("   ", f)
