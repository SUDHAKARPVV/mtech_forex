"""Update Project_Requirement.docx IN PLACE.

Starts from the user's own document.xml and reuses the formatting vocabulary
already present in it (numbered-heading list at numId=5, Aptos body runs,
their bullet/caption/figure paragraph properties), so the result keeps the
original look, fonts, numbering, headers/footers and section setup.
"""
import os, re, shutil, zipfile
from PIL import Image

HERE  = os.path.dirname(os.path.abspath(__file__))
SRC   = HERE + "/unpacked"          # pristine unzip of the user's docx
BUILD = HERE + "/build2"
FIGS  = HERE + "/figs"
OUT   = HERE + "/Project_Requirement_UPDATED.docx"

if os.path.exists(BUILD): shutil.rmtree(BUILD)
shutil.copytree(SRC, BUILD)

DOC = BUILD + "/word/document.xml"
doc = open(DOC, encoding="utf-8").read()
paras = re.findall(r"<w:p\b.*?</w:p>", doc, re.S)

def ptext(p): return "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p)).strip()

# ------------------------------------------------------------------ templates
def pPr_of(i):
    m = re.search(r"<w:pPr>.*?</w:pPr>", paras[i], re.S)
    return m.group(0) if m else ""
def rPr_of(i):
    m = re.search(r"<w:r\b[^>]*>\s*(<w:rPr>.*?</w:rPr>)", paras[i], re.S)
    return m.group(1) if m else ""

T = {
    "h0":  (pPr_of(24),  rPr_of(24)),    # 1. Introduction         (numId 5, ilvl 0)
    "h1":  (pPr_of(26),  rPr_of(26)),    # 1.1 Broad Area of Work  (ilvl 1)
    "h2":  (pPr_of(82),  rPr_of(82)),    # 3.1.1 ...               (ilvl 2)
    "body":(pPr_of(83),  rPr_of(83)),    # justified Aptos 10pt
    "sub": (pPr_of(84),  rPr_of(84)),    # bold inline sub-heading
    "cap": (pPr_of(81),  rPr_of(81)),    # centred italic caption
    "img": (pPr_of(78),  ""),            # centred figure paragraph
    "bul": (pPr_of(30),  rPr_of(30)),    # bulleted list item
    "front":(pPr_of(0),  rPr_of(0)),     # unnumbered front-matter title ("Contents")
}
DRAW = re.search(r"<w:drawing>.*?</w:drawing>", paras[78], re.S).group(0)

def esc(t): return t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def _runs(text, rpr):
    """**bold** and *italic* inline, inheriting the template run properties."""
    out = []
    for part in re.split(r"(\*\*[^*]+\*\*|\*[^*]+\*)", text):
        if not part: continue
        r = rpr
        if part.startswith("**") and part.endswith("**"):
            part = part[2:-2]
            if "<w:b/>" not in r:
                r = r.replace("<w:rPr>", "<w:rPr><w:b/><w:bCs/>") if r else "<w:rPr><w:b/><w:bCs/></w:rPr>"
        elif part.startswith("*") and part.endswith("*"):
            part = part[1:-1]
            r = r.replace("<w:rPr>", "<w:rPr><w:i/>") if r else "<w:rPr><w:i/></w:rPr>"
        out.append(f'<w:r>{r}<w:t xml:space="preserve">{esc(part)}</w:t></w:r>')
    return "".join(out)

def mk(kind, text):
    ppr, rpr = T[kind]
    return f"<w:p>{ppr}{_runs(text, rpr)}</w:p>"

H0   = lambda t: mk("h0", t)
H1   = lambda t: mk("h1", t)
H2   = lambda t: mk("h2", t)
BODY = lambda t: mk("body", t)
SUB  = lambda t: mk("sub", t)
CAP  = lambda t: mk("cap", t)
BUL  = lambda t: mk("bul", t)
FRONT= lambda t: mk("front", t)
PAGEBREAK = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'

# ------------------------------------------------------------------ images
media = BUILD + "/word/media"
rels_p = BUILD + "/word/_rels/document.xml.rels"
rels = open(rels_p, encoding="utf-8").read()
RID = {}
n = 900
for f in ["fig_study_scope","fig_gaps","fig_architecture","fig_data_layer","fig_design_overview",
          "fig_layer_fusion","fig_layer_cnn","fig_layer_transformer",
          "fig_layer_recurrent","fig_layer_experts","fig_layer_heads",
          "fig_eval_split","fig_base_rate","fig_significance","fig_conformal_protocol",
          "fig_directional","fig_magnitude","fig_conformal","fig_cross_currency",
          "fig_roadmap","fig_claims"]:
    shutil.copy(f"{FIGS}/{f}.png", f"{media}/{f}.png")
    n += 1
    RID[f] = f"rId{n}"
    rels = rels.replace("</Relationships>",
        f'<Relationship Id="rId{n}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/{f}.png"/></Relationships>')
open(rels_p, "w", encoding="utf-8").write(rels)

_docpr = [7000]
def IMG(key, width_in=6.0):
    w, h = Image.open(f"{FIGS}/{key}.png").size
    cx = int(width_in * 914400); cy = int(cx * h / w)
    _docpr[0] += 1
    d = DRAW
    d = re.sub(r'<wp:extent cx="\d+" cy="\d+"/>', f'<wp:extent cx="{cx}" cy="{cy}"/>', d)
    d = re.sub(r'<a:ext cx="\d+" cy="\d+"/>', f'<a:ext cx="{cx}" cy="{cy}"/>', d)
    d = re.sub(r'r:embed="[^"]+"', f'r:embed="{RID[key]}"', d)
    d = re.sub(r'<wp:docPr id="\d+" name="[^"]*"', f'<wp:docPr id="{_docpr[0]}" name="{key}"', d)
    d = re.sub(r'(<pic:cNvPr id=")\d+(" name=")[^"]*"', rf'\g<1>0\g<2>{key}.png"', d)
    return f'<w:p>{T["img"][0]}<w:r>{d}</w:r></w:p>'

# ------------------------------------------------------------------ tables
def TBL(rows, widths):
    grid = "".join(f'<w:gridCol w:w="{w}"/>' for w in widths)
    body = ""
    for ri, row in enumerate(rows):
        cells = ""
        for ci, c in enumerate(row):
            hdr = (ri == 0)
            shade = ('<w:shd w:val="clear" w:color="auto" w:fill="1F3759"/>' if hdr
                     else ('<w:shd w:val="clear" w:color="auto" w:fill="F2F5F9"/>' if ri % 2 == 0 else ""))
            rpr = ('<w:rPr><w:rFonts w:ascii="Aptos" w:hAnsi="Aptos"/><w:b/><w:bCs/>'
                   '<w:color w:val="FFFFFF"/><w:sz w:val="18"/><w:szCs w:val="18"/></w:rPr>' if hdr
                   else '<w:rPr><w:rFonts w:ascii="Aptos" w:hAnsi="Aptos"/><w:sz w:val="18"/><w:szCs w:val="18"/></w:rPr>')
            jc = '<w:jc w:val="center"/>' if ci > 0 else ""
            para = (f'<w:p><w:pPr><w:spacing w:before="30" w:after="30"/>{jc}</w:pPr>'
                    f'{_runs(c, rpr)}</w:p>')
            cells += (f'<w:tc><w:tcPr><w:tcW w:w="{widths[ci]}" w:type="dxa"/>{shade}'
                      f'<w:vAlign w:val="center"/></w:tcPr>{para}</w:tc>')
        body += f'<w:tr>{"<w:trPr><w:tblHeader/></w:trPr>" if ri==0 else ""}{cells}</w:tr>'
    return (f'<w:tbl><w:tblPr><w:tblW w:w="{sum(widths)}" w:type="dxa"/>'
            f'<w:tblInd w:w="720" w:type="dxa"/>'
            f'<w:tblBorders><w:top w:val="single" w:sz="4" w:color="C7CDD4"/>'
            f'<w:bottom w:val="single" w:sz="4" w:color="C7CDD4"/>'
            f'<w:insideH w:val="single" w:sz="4" w:color="E3E7EC"/></w:tblBorders>'
            f'<w:tblLayout w:type="fixed"/></w:tblPr><w:tblGrid>{grid}</w:tblGrid>{body}</w:tbl>'
            f'<w:p><w:pPr><w:spacing w:after="80"/><w:ind w:left="720"/></w:pPr></w:p>')

exec(open(HERE + "/content_inplace.py", encoding="utf-8").read())   # -> NEW (list), TOC_ITEMS
# ------------------------------------------------------------------ front lists
# Build "List of Figures" / "List of Tables" from the caption paragraphs that
# content_inplace.py just produced, bookmarking each caption so the list entries
# can carry a real PAGEREF page number.
_cap_rx = re.compile(r"<w:t[^>]*>(Figure|Table) (\d+): ([^<]*)</w:t>")

def _short(title, limit=62):
    """A readable short title: cut at the first em dash or sentence end, then
    cap the length on a word boundary for the few captions that have neither."""
    for sep in (" \u2014 ", ". "):
        i = title.find(sep)
        if i > 0:
            title = title[:i]
    title = title.rstrip(" .\u2014")
    if len(title) > limit:
        title = title[:limit].rsplit(" ", 1)[0].rstrip(" ,;:") + "\u2026"
    return title

_ENTRY_PPR = ('<w:pPr><w:tabs><w:tab w:val="right" w:leader="dot" w:pos="9000"/></w:tabs>'
              '<w:spacing w:after="60" w:line="240" w:lineRule="auto"/></w:pPr>')
_ENTRY_RPR = T["body"][1]

def _list_entry(kind, num, title, mark):
    return (f'<w:p>{_ENTRY_PPR}'
            f'<w:r>{_ENTRY_RPR}<w:t xml:space="preserve">{kind} {num}: {esc(title)}</w:t></w:r>'
            f'<w:r>{_ENTRY_RPR}<w:tab/></w:r>'
            f'<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
            f'<w:r><w:instrText xml:space="preserve"> PAGEREF {mark} \\h </w:instrText></w:r>'
            f'<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
            f'<w:r>{_ENTRY_RPR}<w:t>\u2013</w:t></w:r>'
            f'<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>')

LOF, LOT = [FRONT("List of Figures")], [FRONT("List of Tables")]
_bid = 4000
for _i, _p in enumerate(NEW):
    _m = _cap_rx.search(_p)
    if not _m:
        continue
    _kind, _num, _title = _m.group(1), _m.group(2), _m.group(3)
    _bid += 1
    _mark = f"_{_kind}{_num}"
    # bookmark the caption paragraph so PAGEREF has a target
    NEW[_i] = _p.replace("</w:p>",
        f'<w:bookmarkStart w:id="{_bid}" w:name="{_mark}"/>'
        f'<w:bookmarkEnd w:id="{_bid}"/></w:p>', 1)
    (LOF if _kind == "Figure" else LOT).append(
        _list_entry(_kind, _num, _short(_title), _mark))

print(f"   list of figures: {len(LOF)-1} entries; list of tables: {len(LOT)-1} entries")


# ------------------------------------------------------------------ splice
# Rebuild the Contents list. paras[0] is the "Contents" title and paras[1..21]
# are the entry lines; clone an entry's own formatting for every new line so the
# list keeps the original look even though it is now longer.
def set_text(p, new):
    rpr = re.search(r"<w:r\b[^>]*>\s*(<w:rPr>.*?</w:rPr>)", p, re.S)
    rpr = rpr.group(1) if rpr else ""
    ppr = re.search(r"<w:pPr>.*?</w:pPr>", p, re.S)
    ppr = ppr.group(0) if ppr else ""
    return f'<w:p>{ppr}<w:r>{rpr}<w:t xml:space="preserve">{esc(new)}</w:t></w:r></w:p>'

ENTRY = paras[1]                       # template: a single Contents line
toc_keep = (ACK + [PAGEBREAK] + [paras[0]]
            + [set_text(ENTRY, e) for e in TOC_ITEMS]
            + paras[22:24]
            + LOF + [PAGEBREAK] + LOT + [PAGEBREAK]
            + ABBR + [PAGEBREAK])

sect = re.search(r"<w:sectPr.*?</w:sectPr>", doc, re.S).group(0)
head = doc[:doc.index("<w:body>") + len("<w:body>")]
open(DOC, "w", encoding="utf-8").write(head + "".join(toc_keep) + "".join(NEW) + sect + "</w:body></w:document>")

if os.path.exists(OUT): os.remove(OUT)
z = zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED)
for root, _, files in os.walk(BUILD):
    for f in files:
        full = os.path.join(root, f)
        z.write(full, os.path.relpath(full, BUILD).replace("\\", "/"))
z.close()
print("written:", OUT, f"({os.path.getsize(OUT)/1024:.0f} KB)")
