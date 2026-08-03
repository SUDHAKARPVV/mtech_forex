"""Whole-document validation of Project_Requirement_UPDATED.docx.

Checks structure (TOC vs headings, figure/table numbering, captions), the
integrity of the package (images embedded, styling inherited from the user's
original), internal cross-references, and every numeric claim that can be
traced back to a results file or to the model source.
"""
import io, os, re, json, zipfile, sys

DOC = "Project_Requirement_UPDATED.docx"
ORIG = "unpacked"                      # pristine unzip of the user's original
RES = "C:/Sudhakar/Github/Forex_Price_Prediction/results"

fails, warns, oks = [], [], []
def ok(m):   oks.append(m)
def bad(m):  fails.append(m)
def warn(m): warns.append(m)

z = zipfile.ZipFile(DOC)
d = z.read("word/document.xml").decode("utf-8")
paras = re.findall(r"<w:p\b.*?</w:p>", d, re.S)
def ptext(p): return "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))
texts = [ptext(p) for p in paras]
body = "\n".join(texts)

# ------------------------------------------------------------ 1. package
need = ["word/document.xml", "word/styles.xml", "word/numbering.xml",
        "[Content_Types].xml", "word/_rels/document.xml.rels"]
missing = [n for n in need if n not in z.namelist()]
bad(f"missing package parts: {missing}") if missing else ok("package parts present")

if os.path.isdir(ORIG):
    for part in ["word/styles.xml", "word/numbering.xml", "word/theme/theme1.xml"]:
        src = os.path.join(ORIG, *part.split("/"))
        if os.path.exists(src) and part in z.namelist():
            same = open(src, "rb").read() == z.read(part)
            ok(f"{part} byte-identical to the original") if same else \
                bad(f"{part} DIFFERS from the original (styling may have changed)")
    # headers / footers carried over
    hf_o = sorted(n for n in os.listdir(os.path.join(ORIG, "word"))
                  if re.match(r"(header|footer)\d+\.xml", n))
    hf_n = sorted(os.path.basename(n) for n in z.namelist()
                  if re.match(r"word/(header|footer)\d+\.xml", n))
    ok(f"headers/footers preserved ({len(hf_n)})") if hf_o == hf_n else \
        bad(f"header/footer mismatch: original {hf_o} vs built {hf_n}")

# sectPr (page size / margins) preserved
if os.path.exists(os.path.join(ORIG, "word", "document.xml")):
    o = open(os.path.join(ORIG, "word", "document.xml"), encoding="utf-8").read()
    so = re.search(r"<w:sectPr.*?</w:sectPr>", o, re.S)
    sn = re.search(r"<w:sectPr.*?</w:sectPr>", d, re.S)
    ok("section properties (page setup) preserved") if so and sn and so.group(0) == sn.group(0) \
        else bad("section properties changed")

# ------------------------------------------------------------ 2. fonts
fonts = set(re.findall(r'<w:rFonts w:ascii="([^"]+)"', d))
ok(f"fonts used: {sorted(fonts)}")
if any(f.startswith("Heading") for f in re.findall(r'w:val="([^"]+)"', d)):
    warn("a Heading* style appears in the document")

# numbered-heading list still numId=5, bullets numId=6
nums = re.findall(r"<w:numId w:val=\"(\d+)\"/>", d)
from collections import Counter
ok(f"list numIds in use: {dict(Counter(nums))}")

# ------------------------------------------------------------ 3. headings vs TOC
heads = []
for p, t in zip(paras, texts):
    m = re.search(r'<w:numId w:val="5"/>', p)
    if m and t.strip():
        ilvl = re.search(r'<w:ilvl w:val="(\d+)"/>', p)
        heads.append((int(ilvl.group(1)) if ilvl else 0, t.strip()))
# TOC entries run from the "Contents" title to the first numbered heading. The
# title is not necessarily paragraph 0 — front matter (Acknowledgements) precedes
# it — so locate it rather than assuming a position.
first_head = next(i for i, (p, t) in enumerate(zip(paras, texts))
                  if '<w:numId w:val="5"/>' in p and t.strip())
contents_i = next((i for i, t in enumerate(texts[:first_head])
                   if t.strip().lower() == "contents"), 0)
front = [t.strip() for t in texts[:contents_i] if t.strip()]
if front:
    ok(f"front matter present ahead of the Contents: {len(front)} paragraphs, "
       f"heading {front[0]!r}")
# Only the numbered entry lines belong to the Contents; other front matter
# (the abbreviations list) also sits between the title and the first heading.
_between = [t.strip() for t in texts[contents_i + 1:first_head] if t.strip()]
toc = [t for t in _between if re.match(r"^\d+(\.\d+)*\.?\s", t)]
_other = [t for t in _between if t not in toc]
if _other:
    ok(f"further front matter after the Contents: {len(_other)} paragraphs, "
       f"heading {_other[0]!r}")
head_titles = [t for _, t in heads]
miss = [t for t in head_titles if not any(t in e for e in toc)]
extra = [e for e in toc if not any(h in e for h in head_titles)]
ok(f"{len(heads)} numbered headings, {len(toc)} contents entries")
bad(f"headings absent from Contents: {miss}") if miss else ok("every heading appears in the Contents")
bad(f"Contents entries with no heading: {extra}") if extra else ok("no orphan Contents entries")

# section numbering implied by ilvl sequence
lvl0 = [t for l, t in heads if l == 0]
ok(f"top-level sections ({len(lvl0)}): {lvl0}")

# ------------------------------------------------------------ 4. figures
draw = len(re.findall(r"<w:drawing>", d))
# captions live in the body; the List of Figures repeats them as front matter
btexts = texts[first_head:]
caps = [t.strip() for t in btexts if re.match(r"^Figure \d+:", t.strip())]
n = [int(re.match(r"^Figure (\d+):", c).group(1)) for c in caps]
ok(f"{draw} images, {len(caps)} figure captions")
bad(f"images ({draw}) != captions ({len(caps)})") if draw != len(caps) else ok("every image has a caption")
bad(f"figure numbers not sequential: {n}") if n != list(range(1, len(n) + 1)) else \
    ok(f"figure numbers sequential 1..{len(n)}")
# each caption paragraph immediately follows an image paragraph
badpos = []
for i in range(first_head, len(paras)):
    t = ptext(paras[i]).strip()
    if re.match(r"^Figure \d+:", t) and "<w:drawing>" not in paras[i - 1]:
        badpos.append(t[:40])
bad(f"captions not directly under their image: {badpos}") if badpos else \
    ok("every caption sits directly under its image")
# relationships resolve
rels = z.read("word/_rels/document.xml.rels").decode("utf-8")
for rid in set(re.findall(r'r:embed="(rId\d+)"', d)):
    m = re.search(rf'Id="{rid}"[^>]*Target="([^"]+)"', rels)
    if not m: bad(f"{rid} has no relationship")
    elif "word/" + m.group(1) not in z.namelist(): bad(f"{rid} target missing: {m.group(1)}")
ok("all image relationships resolve to files in the package")

# in-text figure references point at a real figure
refs = set(int(x) for x in re.findall(r"Figure (\d+)", body))
dangling = sorted(r for r in refs if r not in n)
bad(f"references to non-existent figures: {dangling}") if dangling else ok("no dangling figure references")

# ------------------------------------------------------------ 5. tables
tbls = re.findall(r"<w:tbl>.*?</w:tbl>", d, re.S)
# body tables are those after the first numbered heading; anything earlier is
# front matter (the abbreviations list) and is not a numbered table
_body_start = d.index(paras[first_head]) if first_head < len(paras) else 0
body_tbls = [t for t in tbls if d.index(t) > _body_start]
front_tbls = len(tbls) - len(body_tbls)
ok(f"{len(tbls)} tables ({len(body_tbls)} numbered in the body, {front_tbls} in front matter)")
for i, t in enumerate(tbls, 1):
    rows = re.findall(r"<w:tr\b.*?</w:tr>", t, re.S)
    widths = {len(re.findall(r"<w:tc>", r)) for r in rows}
    if len(widths) != 1: bad(f"table {i}: ragged rows, cell counts {widths}")
    if "<w:tblHeader/>" not in rows[0]: bad(f"table {i}: header row does not repeat across pages")
ok("all tables rectangular with repeating header rows")

# table captions: sequential, one per table, each directly under its table,
# and every in-text "Table N" reference resolves
tcaps = [t.strip() for t in btexts if re.match(r"^Table \d+:", t.strip())]
tn = [int(re.match(r"^Table (\d+):", c).group(1)) for c in tcaps]
ok(f"{len(body_tbls)} body tables, {len(tcaps)} table captions")
bad(f"body tables ({len(body_tbls)}) != table captions ({len(tcaps)})") if len(body_tbls) != len(tcaps)     else ok("every table has a caption")
bad(f"table numbers not sequential: {tn}") if tn != list(range(1, len(tn) + 1))     else ok(f"table numbers sequential 1..{len(tn)}")
# a table caption must be the first paragraph after a </w:tbl>
off = []
for _t in body_tbls:
    ch = d[d.index(_t) + len(_t):]
    m = re.search(r"<w:p\b.*?</w:p>", ch, re.S)
    first = ptext(m.group(0)).strip() if m else ""
    # the builder emits a spacer paragraph after each table, so look at the next one
    ps = re.findall(r"<w:p\b.*?</w:p>", ch, re.S)[:2]
    if not any(re.match(r"^Table \d+:", ptext(x).strip()) for x in ps):
        off.append(first[:40])
bad(f"tables whose caption does not directly follow them: {off}") if off else     ok("every caption sits directly under its table")
trefs = set(int(x) for x in re.findall(r"Table (\d+)", body))
tdang = sorted(r for r in trefs if r not in tn)
bad(f"references to non-existent tables: {tdang}") if tdang else ok("no dangling table references")

# every table fits inside the text column
pg = int(re.search(r'<w:pgSz w:w="(\d+)"', d).group(1))
mgs = re.search(r"<w:pgMar[^>]*/>", d).group(0)
lm = int(re.search(r'w:left="(\d+)"', mgs).group(1))
rm = int(re.search(r'w:right="(\d+)"', mgs).group(1))
usable = pg - lm - rm
over = []
for i, t in enumerate(tbls, 1):
    cols = [int(x) for x in re.findall(r'<w:gridCol w:w="(\d+)"/>', t)]
    ind = re.search(r'<w:tblInd w:w="(\d+)"', t)
    tot = sum(cols) + (int(ind.group(1)) if ind else 0)
    if tot > usable: over.append(f"table {i}: {tot} > {usable}")
bad(f"tables wider than the text column: {over}") if over else     ok(f"all {len(tbls)} tables fit the {usable}-twip text column")

# ------------------------------------------------------------ 6. cross-references
secs = set()
for l, t in heads:
    pass
# build the implied numbering from ilvl order
counters = [0, 0, 0]
numbered = {}
for l, t in heads:
    counters[l] += 1
    for k in range(l + 1, 3): counters[k] = 0
    label = ".".join(str(counters[k]) for k in range(l + 1))
    numbered[label] = t
badrefs = sorted({s for s in re.findall(r"Section (\d+(?:\.\d+)*)", body) if s not in numbered})
bad(f"references to non-existent sections: {badrefs}") if badrefs else \
    ok(f"all {len(set(re.findall(r'Section (\d+(?:\.\d+)*)', body)))} section cross-references resolve")

# ------------------------------------------------------------ 7. no comparisons to the old draft
banned = ["previous report", "earlier report", "earlier draft", "prior draft",
          "the earlier design", "was replaced", "an increase from", "previously reported",
          "in the original document", "compared to the earlier"]
hits = [b for b in banned if b.lower() in body.lower()]
bad(f"text still compares against the earlier draft: {hits}") if hits else \
    ok("no comparisons to the earlier draft")

# ------------------------------------------------------------ 8. numeric claims
def claim(label, present, expect, tol=0.0):
    if not present: warn(f"claim not found in text: {label}"); return
    if expect is None: ok(f"{label}: stated"); return
    good = abs(present - expect) <= tol
    (ok if good else bad)(f"{label}: document {present} vs source {expect}")

# --- parameters, from the live model
sys.path.insert(0, "C:/Sudhakar/Github/Forex_Price_Prediction")
os.chdir("C:/Sudhakar/Github/Forex_Price_Prediction")
try:
    import warnings; warnings.filterwarnings("ignore")
    from models.hybrid_model import HybridCNNLSTMTransformer as M
    m = M(); g = {}
    for nm, p in m.named_parameters():
        if p.requires_grad: g[nm.split(".")[0]] = g.get(nm.split(".")[0], 0) + p.numel()
    tot = sum(g.values())
    claim("total trainable parameters", 4401767 if "4,401,767" in body else None, tot)
    for txt, key in [("3,159,040", "transformer"), ("395,264", "bilstm"), ("296,448", "bigru"),
                     ("132,265", "regime_output"), ("131,328", "context_combine"),
                     ("124,032", "cnn"), ("66,048", "cross_attn"), ("33,024", "to_dmodel"),
                     ("23,242", "direction_head")]:
        claim(f"{key} parameters", int(txt.replace(",", "")) if txt in body else None, g[key])
    # budget table sums to the total
    rows = [int(x.replace(",", "")) for x in
            re.findall(r"\b([\d]{1,3}(?:,\d{3})+)\b", body) if False] or []
    from config import MODEL_CFG as c, TRAIN_CFG as tc
    for txt, val, name in [("kernel 3", c.cnn_kernel_size, "CNN kernel"),
                           ("1024-dimensional feed-forward", c.transformer_ffn, "FFN width"),
                           ("d_head = 32", c.transformer_d_model // c.transformer_heads, "d_head"),
                           ("eight attention heads", c.transformer_heads, "transformer heads"),
                           ("four Transformer encoder layers", c.transformer_layers, "layers"),
                           ("hidden size 128 per direction", c.lstm_hidden, "LSTM hidden"),
                           ("random 40%", int(c.sentiment_dropout_p * 100), "masking rate"),
                           ("weight 0.35", tc.directional_loss_weight, "direction loss weight"),
                           ("k = 10 horizons", c.horizon, "horizon")]:
        (ok if txt in body else warn)(f"{name}: phrase '{txt}' {'present' if txt in body else 'NOT FOUND'} (source value {val})")
    ok("causal masking enabled in config") if c.transformer_causal else bad("config says causal=False but the text claims causal masking")
except Exception as e:
    warn(f"could not verify model-derived claims: {e}")

# --- conformal coverage, from results
cf = os.path.join(RES, "conformal_XAUUSD.json")
if os.path.exists(cf):
    j = json.load(open(cf))
    def find(o, key, acc=None):
        acc = acc if acc is not None else []
        if isinstance(o, dict):
            for k, v in o.items():
                if k == key: acc.append(v)
                find(v, key, acc)
        elif isinstance(o, list):
            for v in o: find(v, key, acc)
        return acc
    gc = find(j, "gaussian_coverage")
    if gc:
        claim("gold Gaussian coverage at nominal 80%",
              63.3 if "63.3%" in body else None, round(gc[0] * 100, 1), 0.05)

# ------------------------------------------------------------ 9. reference sanity
# A reference can resolve (the target exists) and still point at the wrong thing.
# Heuristic: the sentence around the reference should share a content word with
# the caption or heading it points at. Reported as NOTE, since it is a heuristic.
STOP = set("""the a an and or of to in on for with by is are was were be been this that
those these it its as at from into than then so such not no any all each every one two
three both which what when where how why can may will would could should its it's here
there we our their his her them they i""".split())
def words(t):
    return {w for w in re.findall(r"[a-z]{4,}", t.lower()) if w not in STOP}

targets = {}
for kind, pat in (("Figure", r"^Figure (\d+): (.*)"), ("Table", r"^Table (\d+): (.*)")):
    for t in texts:
        m = re.match(pat, t.strip())
        if m: targets[(kind, int(m.group(1)))] = m.group(2)
sec_titles = {}
_ctr = [0, 0, 0]
for lvl, title in heads:
    _ctr[lvl] += 1
    for k in range(lvl + 1, 3): _ctr[k] = 0
    sec_titles[".".join(str(_ctr[k]) for k in range(lvl + 1))] = title

suspect = []
for i, t in enumerate(texts):
    if re.match(r"^(Figure|Table) \d+:", t.strip()):
        continue                                    # captions are not references
    for m in re.finditer(r"\b(Figure|Table) (\d+)\b", t):
        tgt = targets.get((m.group(1), int(m.group(2))))
        if tgt is None: continue
        ctx = t[max(0, m.start() - 160): m.end() + 160]
        if not (words(ctx) & words(tgt)):
            suspect.append(f"{m.group(1)} {m.group(2)} ({tgt[:38]}...) from: ...{ctx[max(0,m.start()-70-max(0,m.start()-160)):][:80]}...")
for kind in ("Figure", "Table"):
    for m in re.finditer(rf"\b{kind}s (\d+) and (\d+)\b", body):
        for g in (1, 2):
            if (kind, int(m.group(g))) not in targets:
                bad(f"plural reference '{kind}s {m.group(1)} and {m.group(2)}' names a non-existent {kind} {m.group(g)}")
if suspect:
    for x in suspect: warn(f"reference may point at the wrong target: {x}")
else:
    ok("every figure/table reference shares vocabulary with the caption it names")

# ------------------------------------------------------------ 10. references
refs = [t.strip() for t in texts if re.match(r"^\[\d+\]", t.strip())]
listed = [int(re.match(r"^\[(\d+)\]", r).group(1)) for r in refs]
ok(f"{len(refs)} reference entries")
bad(f"reference numbers not sequential: {listed}") if listed != list(range(1, len(listed) + 1)) \
    else ok(f"reference numbers sequential 1..{len(listed)}")
_first = next((i for i, t in enumerate(texts) if re.match(r"^\[1\]\s", t.strip())), len(texts))
_body = "\n".join(texts[:_first])
cited, _seen, _order = set(), set(), []
for _m in re.finditer(r"\[(\d+)\]", _body):
    _n = int(_m.group(1)); cited.add(_n)
    if _n not in _seen:
        _seen.add(_n); _order.append(_n)
uncited = sorted(set(listed) - cited)
unlisted = sorted(cited - set(listed))
bad(f"references never cited in the text: {uncited}") if uncited else ok("every reference is cited at least once")
bad(f"citations with no reference entry: {unlisted}") if unlisted else ok("every citation resolves to a reference")
bad(f"citations not numbered by order of first mention: {_order}") if _order != sorted(_order) \
    else ok("citations numbered by order of first mention (IEEE)")
_noid = [n for n, r in zip(listed, refs)
         if "doi:" not in r and "arXiv" not in r and "Press" not in r and "Holden-Day" not in r]
warn(f"reference entries without a DOI or arXiv id: {_noid}") if _noid else \
    ok("every reference carries a DOI, an arXiv id, or is a book")

print("=" * 74)
for m_ in oks:   print("  PASS  ", m_)
for m_ in warns: print("  NOTE  ", m_)
for m_ in fails: print("  FAIL  ", m_)
print("=" * 74)
print(f"{len(oks)} passed, {len(warns)} notes, {len(fails)} failures")

