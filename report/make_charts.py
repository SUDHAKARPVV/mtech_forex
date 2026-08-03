"""Result charts for the report. Emits PNG (for the document) and SVG (editable)."""
import os, json
import numpy as np
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["svg.fonttype"] = "none"      # keep SVG text editable
matplotlib.rcParams["font.family"] = "DejaVu Sans"
import matplotlib.pyplot as plt
if os.environ.get("DIAGRAM_NO_TITLE"):        # paper figures: caption carries the title
    from matplotlib.axes import Axes
    Axes.set_title = lambda self, *a, **k: None

OUT = os.path.dirname(os.path.abspath(__file__)) + "/figs"
os.makedirs(OUT, exist_ok=True)
NAVY="#1E3A5F"; TEAL="#0E7C86"; GREEN="#0F766E"; AMBER="#B45309"
SLATE="#64748B"; LIGHT="#94A3B8"

# ---------------------------------------------------------------- FIG C: directional result, 3 pairs
res=json.load(open("results_ctx.json")) if os.path.exists("results_ctx.json") else None
pairs=["Gold\nXAU/USD","Silver\nXAG/USD","Euro\nEUR/USD"]
hyb=[0.5178,0.5145,0.4984]; hyb_sd=[0.0005,0.0018,0.0015]
garch=[0.5378,0.5237,0.5044]; arima=[0.5063,0.4925,0.4875]; base=[0.5344,0.5354,0.5037]
x=np.arange(3); w=0.22
fig,ax=plt.subplots(figsize=(9.2,4.6)); fig.patch.set_facecolor("white")
ax.bar(x-w,hyb,w,yerr=hyb_sd,capsize=3,label="Hybrid (3-seed)",color=TEAL)
ax.bar(x,garch,w,label="GARCH",color=NAVY)
ax.bar(x+w,arima,w,label="ARIMA",color=LIGHT)
for i,b in enumerate(base):
    ax.hlines(b,i-1.6*w,i+1.6*w,color=AMBER,lw=2.4,zorder=5)
    ax.text(i+1.75*w,b,f"base {b:.3f}",va="center",fontsize=8,color=AMBER,fontweight="bold")
ax.axhline(0.5,color=SLATE,ls=":",lw=1)
ax.set_xticks(x); ax.set_xticklabels(pairs); ax.set_ylim(0.46,0.56)
ax.set_ylabel("Directional accuracy (test set)")
ax.set_title("Directional accuracy vs the always-up base rate — no model clears the base rate on any pair",
             fontsize=10.5,fontweight="bold",color=NAVY)
ax.legend(frameon=False,ncol=3,loc="upper center",bbox_to_anchor=(0.5,-0.10))
ax.spines[["top","right"]].set_visible(False)
plt.tight_layout(); [plt.savefig(f"{OUT}/fig_directional.{e}", dpi=200, bbox_inches="tight", facecolor="white") for e in ("png","svg")]; plt.close()

# ---------------------------------------------------------------- FIG D: magnitude, 3 pairs
model=[0.3288,0.4178,0.2316]; atr=[0.3086,0.3771,0.0894]; gs=[0.3043,0.3463,0.1453]
fig,axs=plt.subplots(1,2,figsize=(12.4,4.5)); fig.patch.set_facecolor("white")
a=axs[0]
a.bar(x-w,model,w,label="Hybrid",color=TEAL); a.bar(x,gs,w,label="GARCH-σ",color=GREEN); a.bar(x+w,atr,w,label="ATR%",color=NAVY)
a.set_xticks(x); a.set_xticklabels(pairs); a.set_ylabel("Spearman rank skill vs |10-bar move|")
a.set_title("Move-magnitude rank skill (3-seed mean)",fontsize=10,fontweight="bold",color=NAVY)
a.legend(frameon=False,ncol=3,fontsize=8.5,loc="upper center",bbox_to_anchor=(0.5,-0.15)); a.spines[["top","right"]].set_visible(False)
b=axs[1]
macc=[0.5517,0.5520,0.5709]; aacc=[0.5406,0.5183,0.4886]; gacc=[0.5447,0.5057,0.4938]; bacc=[0.505,0.512,0.497]
b.bar(x-w,macc,w,label="Hybrid",color=TEAL); b.bar(x,gacc,w,label="GARCH-σ",color=GREEN); b.bar(x+w,aacc,w,label="ATR%",color=NAVY)
for i,bb in enumerate(bacc):
    b.hlines(bb,i-1.6*w,i+1.6*w,color=AMBER,lw=2.2,zorder=5)
b.text(2+1.7*w,0.497,"base rate",fontsize=7.5,color=AMBER,va="center")
b.set_xticks(x); b.set_xticklabels(pairs); b.set_ylim(0.46,0.60)
b.set_ylabel("Large-move classification accuracy")
b.set_title("Large-move accuracy (amber = adaptive base rate)",fontsize=10,fontweight="bold",color=NAVY)
b.legend(frameon=False,ncol=3,fontsize=8.5,loc="upper center",bbox_to_anchor=(0.5,-0.15)); b.spines[["top","right"]].set_visible(False)
plt.tight_layout(); [plt.savefig(f"{OUT}/fig_magnitude.{e}", dpi=200, bbox_inches="tight", facecolor="white") for e in ("png","svg")]; plt.close()

# ---------------------------------------------------------------- FIG E: conformal coverage
lv=["80%","90%","95%"]; gauss=[63.3,72.9,79.0]; split=[61.9,75.8,84.5]; aci=[79.9,90.0,95.0]; tgt=[80,90,95]
xx=np.arange(3)
fig,ax=plt.subplots(figsize=(8.6,4.4)); fig.patch.set_facecolor("white")
ax.bar(xx-w,gauss,w,label="Gaussian σ band",color=LIGHT)
ax.bar(xx,split,w,label="Split conformal",color=NAVY)
ax.bar(xx+w,aci,w,label="Adaptive conformal (ACI)",color=GREEN)
for i,t in enumerate(tgt):
    ax.hlines(t,i-1.6*w,i+1.6*w,color=AMBER,lw=2.4,zorder=5)
ax.text(2+1.75*w,95,"target",fontsize=8,color=AMBER,va="center",fontweight="bold")
ax.set_xticks(xx); ax.set_xticklabels(lv); ax.set_ylim(50,100)
ax.set_xlabel("Nominal coverage level"); ax.set_ylabel("Empirical test coverage (%)")
ax.set_title("Interval calibration (gold): the Gaussian band under-covers; ACI restores nominal coverage",
             fontsize=10.5,fontweight="bold",color=NAVY)
for xs, vals in ((xx-w, gauss), (xx, split), (xx+w, aci)):
    for xi, v in zip(xs, vals):
        ax.text(xi, v+0.9, f"{v:.1f}", ha="center", va="bottom", fontsize=7.6,
                fontweight="bold", color=NAVY)
ax.legend(frameon=False,ncol=3,loc="upper center",bbox_to_anchor=(0.5,-0.14),fontsize=8.5)
ax.spines[["top","right"]].set_visible(False)
plt.tight_layout(); [plt.savefig(f"{OUT}/fig_conformal.{e}", dpi=200, bbox_inches="tight", facecolor="white") for e in ("png","svg")]; plt.close()

# ---------------------------------------------------------------- FIG G: cross-currency comparison
fig,ax=plt.subplots(figsize=(9.6,4.6)); fig.patch.set_facecolor("white")
labels=["Gold","Silver","Euro"]
edge_atr=[0.0202,0.0407,0.1422]; edge_g=[0.0245,0.0716,0.0863]
ax.bar(x-0.16,edge_atr,0.32,label="edge over ATR%",color=TEAL)
ax.bar(x+0.16,edge_g,0.32,label="edge over GARCH-σ",color=GREEN)
for i,(ea,eg) in enumerate(zip(edge_atr,edge_g)):
    ax.text(i-0.16,ea+0.004,f"+{ea:.3f}",ha="center",fontsize=8,fontweight="bold",color=TEAL)
    ax.text(i+0.16,eg+0.004,f"+{eg:.3f}",ha="center",fontsize=8,fontweight="bold",color=GREEN)
sig=["not significant\n(p=0.096)","significant\n(p≤0.006)","significant\n(p<0.001)"]
for i,s in enumerate(sig):
    ax.text(i,-0.022,s,ha="center",fontsize=8,color=NAVY if i else SLATE,
            fontweight="bold" if i else "normal")
ax.set_xticks(x); ax.set_xticklabels(labels); ax.set_ylim(-0.035,0.168)
ax.axhline(0,color=SLATE,lw=1)
ax.set_ylabel("Spearman rank-skill edge")
ax.set_title("Magnitude edge over classical volatility baselines, by instrument (3-seed mean, bootstrap p)",
             fontsize=10.5,fontweight="bold",color=NAVY)
ax.legend(frameon=False,ncol=2,fontsize=8.5,loc="upper center",bbox_to_anchor=(0.5,-0.08)); ax.spines[["top","right","bottom"]].set_visible(False)
plt.tight_layout(); [plt.savefig(f"{OUT}/fig_cross_currency.{e}", dpi=200, bbox_inches="tight", facecolor="white") for e in ("png","svg")]; plt.close()

print("charts written (PNG + editable SVG) to", OUT)
for f in sorted(os.listdir(OUT)): print("  ", f)
