"""Repack unpacked/ into a .pptx (zip from inside the directory)."""
import os, sys, zipfile

src = sys.argv[1] if len(sys.argv) > 1 else "unpacked"
out = sys.argv[2] if len(sys.argv) > 2 else "work.pptx"
if os.path.exists(out):
    os.remove(out)
z = zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED)
for root, _, files in os.walk(src):
    for f in files:
        full = os.path.join(root, f)
        z.write(full, os.path.relpath(full, src).replace(os.sep, "/"))
z.close()
print(f"packed {out} ({os.path.getsize(out)/1024:.0f} KB)")
