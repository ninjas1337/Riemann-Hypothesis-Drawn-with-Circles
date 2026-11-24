"""Embed the zeta zeros into scripts/epicycles_template.html and write epicycles.html."""
import json, os
H = os.path.dirname(os.path.abspath(__file__))
z = json.load(open(os.path.join(H, "explainer_data.json")))["zeros"][:20]
t = open(os.path.join(H, "epicycles_template.html")).read()
open(os.path.join(H, "..", "epicycles.html"), "w").write(t.replace("__ZEROS__", json.dumps(z)))
print("wrote epicycles.html")
