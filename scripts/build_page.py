"""Embed scripts/explainer_data.json into scripts/template.html and write index.html."""
import os
H = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(H, "template.html")).read()
d = open(os.path.join(H, "explainer_data.json")).read()
open(os.path.join(H, "..", "index.html"), "w").write(t.replace("__DATA__", d))
print("wrote index.html")
