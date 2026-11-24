"""Embed the zeta zeros into scripts/tangent_template.html and write tangent.html."""
import json, os
H = os.path.dirname(os.path.abspath(__file__))
z = json.load(open(os.path.join(H, "explainer_data.json")))["zeros"]
t = open(os.path.join(H, "tangent_template.html")).read()
open(os.path.join(H, "..", "tangent.html"), "w").write(t.replace("__ZEROS__", json.dumps(z)))
print("wrote tangent.html")
