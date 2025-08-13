import os

plot_dir = "plots"
files = sorted(os.listdir(plot_dir))

html = """<!DOCTYPE html>
<html>
<head>
<title>PDF Plots</title>
<style>
body { font-family: sans-serif; padding: 20px; }
.grid { display: flex; flex-wrap: wrap; gap: 15px; }
.item { width: 250px; }
iframe { width: 250px; height: 250px; border: 1px solid #ccc; }
</style>
</head>
<body>
<h1>PDF Plots</h1>
<div class="grid">
"""

for f in files:
    if f.endswith(".pdf"):
        html += f"""
<div class="item">
    <iframe src="{plot_dir}/{f}"></iframe>
    <p><a href="{plot_dir}/{f}" download>Download</a></p>
</div>
"""

html += """
</div>
</body>
</html>
"""

with open("index.html", "w") as out:
    out.write(html)

print("index.html created with", len(files), "plots.")
