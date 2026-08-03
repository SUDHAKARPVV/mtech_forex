"""Rewrite the SmartArt text on slide 5 (Methodology).

SmartArt keeps its text twice — the data model in ppt/diagrams/data1.xml and a
cached rendering in drawing1.xml. PowerPoint draws the cache, so both must be
updated or the slide shows the old wording until the diagram is refreshed.
"""
import re, shutil, sys, zipfile

DOC = sys.argv[1] if len(sys.argv) > 1 else "work.pptx"

# index -> replacement, matching the 5 label/description pairs in order
NEW = {
 0: "Multi-Modal Feature Fusion: ",
 1: "18 technical indicators, 6 macroeconomic series and 13 FinBERT sentiment features "
    "fused into one aligned 37-feature panel over a 60-bar window",
 2: "Dilated Causal CNN: ",
 3: "Captures local volatility motifs across a 15-bar receptive field; left-only padding "
    "keeps every position blind to its own future",
 5: "Cross-Attention & Gated Recurrence: ",
 6: "Price queries retrieve news context through a presence gate; Bi-LSTM and Bi-GRU then "
    "run in parallel and are mixed by a learned scalar.",
 7: "Causal Transformer Block: ",
 8: "Four pre-norm encoder layers with eight heads model every relation longer than one "
    "trading session — 71.8% of all model parameters",
 10: "Trust-Gated Experts & Probabilistic Heads: ",
 11: "Walk-forward GARCH and XGBoost blended by volatility trust gates; dual regime heads "
     "emit a mean and a variance per horizon.",
}

def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def patch(xml):
    out, i, last = [], 0, 0
    for m in re.finditer(r"<a:t>([^<]*)</a:t>", xml):
        if i in NEW:
            out.append(xml[last:m.start()])
            out.append(f"<a:t>{esc(NEW[i])}</a:t>")
            last = m.end()
        i += 1
    out.append(xml[last:])
    return "".join(out), i

tmp = DOC + ".tmp"
zin = zipfile.ZipFile(DOC)
zout = zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED)
touched = {}
for it in zin.infolist():
    data = zin.read(it.filename)
    if it.filename in ("ppt/diagrams/data1.xml", "ppt/diagrams/drawing1.xml"):
        new, n = patch(data.decode("utf-8"))
        data = new.encode("utf-8")
        touched[it.filename] = n
    zout.writestr(it, data)
zin.close(); zout.close()
shutil.move(tmp, DOC)
print("SmartArt patched:", touched)
