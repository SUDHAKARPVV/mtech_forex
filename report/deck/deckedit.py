"""Helpers for editing an existing deck without disturbing its formatting.

Rule from the pptx skill: never assign text_frame.text (it collapses the
paragraph to one unstyled run). Always write into an existing run so the run's
font, size and colour survive.
"""
import copy


def _runs_of(p):
    return p.runs


def set_para(p, text):
    """Put `text` into paragraph `p`, keeping the first run's formatting and
    dropping any surplus runs."""
    rs = _runs_of(p)
    if not rs:
        # no run to inherit from: clone nothing, leave paragraph empty
        return False
    rs[0].text = text
    for r in rs[1:]:
        r._r.getparent().remove(r._r)
    return True


def set_lines(shape, lines):
    """Rewrite a text frame to exactly `lines`, one paragraph each.

    Extra paragraphs are deleted; missing ones are cloned from the last
    paragraph so bullet level, spacing and colour carry over.

    Raises if the shape has no run to inherit formatting from — that means the
    wrong shape was targeted, and failing loudly beats writing nothing.
    """
    if not shape.has_text_frame or not any(p.runs for p in shape.text_frame.paragraphs):
        raise ValueError(
            f"shape {shape.shape_id} ({shape.name!r}) has no text run to write into "
            f"— wrong target?")
    tf = shape.text_frame
    paras = list(tf.paragraphs)
    # Grow by inserting each clone directly after the last paragraph. Appending to
    # the txBody instead would place it after <a:endParaRPr>, which must stay the
    # final child — PowerPoint silently drops any paragraph that follows it.
    while len(paras) < len(lines):
        src = paras[-1]
        new = copy.deepcopy(src._p)
        src._p.addnext(new)
        paras = list(tf.paragraphs)
    # write
    for i, text in enumerate(lines):
        set_para(paras[i], text)
    # shrink
    for p in paras[len(lines):]:
        p._p.getparent().remove(p._p)
    return shape


def find(slide, *, name=None, sid=None):
    for sh in slide.shapes:
        if sid is not None and sh.shape_id == sid:
            return sh
        if name is not None and sh.name == name:
            return sh
    raise KeyError(f"shape not found: name={name!r} id={sid!r}")


def by_text(slide, snippet, nth=0):
    """Locate a shape by a snippet of its current text — the most robust handle
    when several shapes share a name (this deck reuses 'TextBox 6' etc.)."""
    hits = [sh for sh in slide.shapes
            if sh.has_text_frame and snippet.lower() in sh.text_frame.text.lower()]
    if not hits:
        raise KeyError(f"no shape containing {snippet!r}")
    return hits[nth]


def replace_picture(slide, shape, image_path):
    """Swap a picture's image in place, keeping position, size and z-order."""
    from pptx.util import Emu
    left, top, w, h = shape.left, shape.top, shape.width, shape.height
    el = shape._element
    parent = el.getparent()
    idx = list(parent).index(el)
    parent.remove(el)
    pic = slide.shapes.add_picture(image_path, Emu(left), Emu(top), Emu(w), Emu(h))
    parent.remove(pic._element)
    parent.insert(idx, pic._element)
    return pic


def fit_picture(slide, image_path, left, top, max_w, max_h):
    """Add a picture scaled to fit inside a box, centred in it. Inches."""
    from PIL import Image
    from pptx.util import Inches
    iw, ih = Image.open(image_path).size
    scale = min(max_w / (iw / 96), max_h / (ih / 96))
    w, h = (iw / 96) * scale, (ih / 96) * scale
    return slide.shapes.add_picture(
        image_path, Inches(left + (max_w - w) / 2), Inches(top + (max_h - h) / 2),
        Inches(w), Inches(h))


def delete(shape):
    shape._element.getparent().remove(shape._element)
