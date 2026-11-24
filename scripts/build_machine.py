"""Embed the zeta zeros into scripts/machine_template.html and write machine.html."""
import json, os
H = os.path.dirname(os.path.abspath(__file__))
z = json.load(open(os.path.join(H, "explainer_data.json")))["zeros"]
t = open(os.path.join(H, "machine_template.html")).read()
open(os.path.join(H, "..", "machine.html"), "w").write(t.replace("__ZEROS__", json.dumps(z)))
print("wrote machine.html")
