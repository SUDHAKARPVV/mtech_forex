"""Small diagram engine: uniform boxes on a grid, edge-clipped / orthogonally
routed arrows, one typographic scale. Emits PNG (for the report) and SVG
(editable — text is kept as real text, so Inkscape/Illustrator/Word can edit it).
"""
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["svg.fonttype"] = "none"        # keep text editable in SVG
matplotlib.rcParams["font.family"] = "DejaVu Sans"
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

# ---------------------------------------------------------------- design tokens
NAVY   = "#1E3A5F"
TEAL   = "#0E7C86"
PURPLE = "#6D४8C7".replace("४","4")
PURPLE = "#6D48C7"
AMBER  = "#B45309"
GREEN  = "#0F766E"
GREY   = "#64748B"
LIGHT  = "#CBD5E1"
INK    = "#0F172A"
EDGE   = "#94A3B8"

FS_TITLE = 13.0
FS_NODE  = 9.2
FS_SUB   = 7.3
FS_EDGE  = 7.0
FS_NOTE  = 8.0

GAP = 0.008          # clearance between an arrowhead and the box it points at


class Canvas:
    def __init__(self, w, h, title=None, subtitle=None):
        self.fig, self.ax = plt.subplots(figsize=(w, h))
        self.ax.set_xlim(0, 1); self.ax.set_ylim(0, 1); self.ax.axis("off")
        self.fig.patch.set_facecolor("white")
        self.nodes = {}
        y = 0.975
        # For journal/conference figures the caption carries the description, so
        # the in-figure title is suppressed via DIAGRAM_NO_TITLE=1.
        import os as _os
        if _os.environ.get("DIAGRAM_NO_TITLE"):
            title = subtitle = None
        if title:
            self.ax.text(0.5, y, title, ha="center", va="top",
                         fontsize=FS_TITLE, fontweight="bold", color=NAVY)
            y -= 0.038
        if subtitle:
            self.ax.text(0.5, y, subtitle, ha="center", va="top",
                         fontsize=FS_NOTE, color=GREY, style="italic")

    # -------------------------------------------------- nodes
    def box(self, key, cx, cy, w, h, label, fc, sub=None, tc="white",
            fs=None, radius=0.018, ec=None, lw=0):
        """cx, cy is the CENTRE — so every box on a row shares an axis."""
        x, y = cx - w / 2, cy - h / 2
        self.ax.add_patch(FancyBboxPatch(
            (x, y), w, h,
            boxstyle=f"round,pad=0,rounding_size={radius}",
            fc=fc, ec=ec or "none", lw=lw, zorder=2))
        fs = fs or FS_NODE
        if sub:
            self.ax.text(cx, cy + h * 0.16, label, ha="center", va="center",
                         fontsize=fs, fontweight="bold", color=tc, zorder=3)
            self.ax.text(cx, cy - h * 0.20, sub, ha="center", va="center",
                         fontsize=FS_SUB, color=tc, zorder=3, linespacing=1.45)
        else:
            self.ax.text(cx, cy, label, ha="center", va="center",
                         fontsize=fs, fontweight="bold", color=tc, zorder=3)
        self.nodes[key] = dict(cx=cx, cy=cy, w=w, h=h)
        return key

    def band(self, x, y, w, h, fc="#F1F5F9", ec="#E2E8F0", label=None):
        """A soft grouping band drawn behind the nodes."""
        self.ax.add_patch(FancyBboxPatch((x, y), w, h,
                          boxstyle="round,pad=0,rounding_size=0.014",
                          fc=fc, ec=ec, lw=1.0, zorder=0))
        if label:
            self.ax.text(x + 0.012, y + h - 0.018, label, ha="left", va="top",
                         fontsize=FS_SUB, color=GREY, fontweight="bold", zorder=1)

    # -------------------------------------------------- geometry
    def _port(self, key, side, off=0.0):
        """`off` slides the port along the edge (fraction of that edge's length),
        so several edges can enter one box in parallel instead of stacking on
        the same centre point."""
        n = self.nodes[key]
        dx, dy = n["w"] * off, n["h"] * off
        return {
            "L": (n["cx"] - n["w"] / 2, n["cy"] + dy),
            "R": (n["cx"] + n["w"] / 2, n["cy"] + dy),
            "T": (n["cx"] + dx, n["cy"] + n["h"] / 2),
            "B": (n["cx"] + dx, n["cy"] - n["h"] / 2),
        }[side]

    def _clip(self, key, px, py):
        """Push a point outward from a node's edge by GAP so the arrowhead
        never sits on (or inside) the box."""
        n = self.nodes[key]
        dx, dy = px - n["cx"], py - n["cy"]
        ax_, ay = abs(dx), abs(dy)
        if ax_ >= ay:
            return (px + GAP * (1 if dx > 0 else -1), py)
        return (px, py + GAP * (1 if dy > 0 else -1))

    # -------------------------------------------------- edges
    def arrow(self, src, dst, s_side="R", d_side="L", label=None,
              color=EDGE, style="-", lw=1.5, rad=0.0, label_dy=0.016,
              s_off=0.0, d_off=0.0):
        p1 = self._clip(src, *self._port(src, s_side, s_off))
        p2 = self._clip(dst, *self._port(dst, d_side, d_off))
        # Guard: if two boxes sit closer than the clearance, the clipped points
        # cross over and the arrow renders BACKWARDS. Fail loudly rather than
        # ship a diagram whose arrow points the wrong way.
        if (s_side, d_side) == ("R", "L") and p2[0] < p1[0]:
            raise ValueError(f"arrow {src}->{dst}: boxes overlap horizontally "
                             f"({p1[0]:.3f} -> {p2[0]:.3f}); increase the gap")
        if (s_side, d_side) == ("L", "R") and p2[0] > p1[0]:
            raise ValueError(f"arrow {src}->{dst}: boxes overlap horizontally")
        if (s_side, d_side) == ("B", "T") and p2[1] > p1[1]:
            raise ValueError(f"arrow {src}->{dst}: boxes overlap vertically")
        if (s_side, d_side) == ("T", "B") and p2[1] < p1[1]:
            raise ValueError(f"arrow {src}->{dst}: boxes overlap vertically")
        cs = f"arc3,rad={rad}" if rad else "arc3,rad=0"
        self.ax.add_patch(FancyArrowPatch(
            p1, p2, arrowstyle="-|>", mutation_scale=12, lw=lw,
            color=color, linestyle=style, connectionstyle=cs,
            shrinkA=0, shrinkB=0, zorder=1))
        if label:
            mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
            self.ax.text(mx, my + label_dy, label, ha="center", va="bottom",
                         fontsize=FS_EDGE, color="#475569", zorder=4,
                         bbox=dict(fc="white", ec="none", pad=1.2))

    def elbow(self, src, dst, s_side="R", d_side="L", label=None,
              color=EDGE, style="-", lw=1.5, mid=None, label_at=0.5,
              s_off=0.0, d_off=0.0):
        """Orthogonal 3-segment route — used whenever a straight line would
        cut across an unrelated box."""
        x1, y1 = self._clip(src, *self._port(src, s_side, s_off))
        x2, y2 = self._clip(dst, *self._port(dst, d_side, d_off))
        if s_side in "LR":
            mx = mid if mid is not None else (x1 + x2) / 2
            pts = [(x1, y1), (mx, y1), (mx, y2), (x2, y2)]
        else:
            my = mid if mid is not None else (y1 + y2) / 2
            pts = [(x1, y1), (x1, my), (x2, my), (x2, y2)]
        for i in range(len(pts) - 2):
            self.ax.plot([pts[i][0], pts[i + 1][0]], [pts[i][1], pts[i + 1][1]],
                         color=color, lw=lw, ls=style, solid_capstyle="round", zorder=1)
        self.ax.add_patch(FancyArrowPatch(
            pts[-2], pts[-1], arrowstyle="-|>", mutation_scale=12, lw=lw,
            color=color, linestyle=style, shrinkA=0, shrinkB=0, zorder=1))
        if label:
            i = int(len(pts) * label_at)
            self.ax.text(pts[1][0], (pts[1][1] + pts[2][1]) / 2, label,
                         ha="center", va="center", fontsize=FS_EDGE, color="#475569",
                         zorder=4, bbox=dict(fc="white", ec="none", pad=1.2))

    def note(self, text, y=0.022):
        self.ax.text(0.5, y, text, ha="center", va="center",
                     fontsize=FS_NOTE, color=GREY, style="italic", linespacing=1.5)


    # -------------------------------------------------- primitives for layer figures
    def dot(self, x, y, r=0.007, fc=None, ec=None, lw=1.2, z=4):
        from matplotlib.patches import Circle
        self.ax.add_patch(Circle((x, y), r, fc=fc or "white", ec=ec or GREY, lw=lw, zorder=z))

    def line(self, x1, y1, x2, y2, color=None, lw=1.1, style="-", z=2, alpha=1.0):
        self.ax.plot([x1, x2], [y1, y2], color=color or EDGE, lw=lw, ls=style,
                     zorder=z, alpha=alpha, solid_capstyle="round")

    def label(self, x, y, text, fs=None, color=None, ha="center", va="center",
              bold=False, italic=False, box=False, z=5):
        kw = dict(ha=ha, va=va, fontsize=fs or FS_SUB, color=color or INK, zorder=z,
                  fontweight="bold" if bold else "normal",
                  style="italic" if italic else "normal")
        if box:
            kw["bbox"] = dict(fc="white", ec="#D6DEE7", lw=0.8, pad=2.2,
                              boxstyle="round,pad=0.28")
        self.ax.text(x, y, text, **kw)

    def formula(self, cx, cy, text, w=0.52, h=0.052, fs=9.0):
        """A centred equation strip, used to state a layer's operation exactly."""
        self.ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                          boxstyle="round,pad=0,rounding_size=0.012",
                          fc="#FFFFFF", ec="#C7D2DD", lw=1.1, zorder=2))
        self.ax.text(cx, cy, text, ha="center", va="center", fontsize=fs,
                     color=INK, zorder=3, family="DejaVu Sans")

    def matrix(self, x0, y0, n, cell, causal=True, fc_on="#1E3A5F", fc_off="#E8EDF3"):
        """Small attention-mask grid (lower-triangular when causal)."""
        from matplotlib.patches import Rectangle as _R
        for i in range(n):
            for j in range(n):
                on = (j <= i) if causal else True
                self.ax.add_patch(_R((x0 + j * cell, y0 - (i + 1) * cell), cell, cell,
                                     fc=fc_on if on else fc_off, ec="white", lw=0.6, zorder=3))

    def save(self, path_noext):
        for ext in ("png", "svg"):
            self.fig.savefig(f"{path_noext}.{ext}", dpi=200,
                             bbox_inches="tight", facecolor="white")
        plt.close(self.fig)
