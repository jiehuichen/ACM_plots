import os

plot_dir = "plots"
files = sorted(os.listdir(plot_dir))

html_items = ""
for f in files:
    if f.endswith(".pdf"):
        gene_name = os.path.splitext(f)[0]
        html_items += f"""
    <div class="item">
        <span class="gene">{gene_name}</span>
        <iframe src="{plot_dir}/{f}"></iframe>
        <p><a href="{plot_dir}/{f}" download>Download</a></p>
    </div>
"""

with open("index.html", "w") as out:
    out.write(f"""<!DOCTYPE html>
<html>
<head>
<title>Searchable Gene Plots</title>
<meta charset="utf-8">
<script src="https://cdnjs.cloudflare.com/ajax/libs/list.js/2.3.1/list.min.js"></script>
<style>
body {{ font-family: sans-serif; padding: 20px; }}
.search {{ margin-bottom: 20px; width: 300px; padding: 8px; font-size: 16px; }}
.grid {{ display: flex; flex-wrap: wrap; gap: 15px; }}
.item {{ width: 250px; }}
iframe {{ width: 250px; height: 250px; border: 1px solid #ccc; }}
.gene {{ font-weight: bold; display: block; margin-bottom: 5px; }}
</style>
</head>
<body>

<h1>Search PDF Plots by Gene Name</h1>

<div id="plot-list">
  <input class="search" placeholder="Type gene name or condition..."/>
  <div class="grid list">
{html_items}
  </div>
</div>

<script>
  var options = {{ valueNames: ['gene'] }};
  var plotList = new List('plot-list', options);
</script>

</body>
</html>
""")

print(f"index.html created with {len(files)} plots.")
