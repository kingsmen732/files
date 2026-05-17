import os
from collections import defaultdict

BASE_DIR = "."
OUTPUT_FILE = "index.html"

files_by_folder = defaultdict(list)

for root, dirs, files in os.walk(BASE_DIR):
    if ".git" in root or "scripts" in root:
        continue

    for file in files:
        if file.endswith(".html") and file != "index.html":
            path = os.path.join(root, file)
            rel_path = os.path.relpath(path, BASE_DIR)
            folder = os.path.dirname(rel_path) or "root"
            files_by_folder[folder].append(rel_path)

html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>PPT Viewer</title>
<style>
body { font-family: sans-serif; background:#0f172a; color:#e2e8f0; padding:20px;}
h1 { margin-bottom:20px;}
.folder { margin-bottom:20px; padding:15px; background:#1e293b; border-radius:10px;}
.folder h2 { color:#38bdf8;}
a { color:#e2e8f0; text-decoration:none; display:block; padding:5px;}
a:hover { color:#38bdf8;}
</style>
</head>
<body>
<h1>📂 PPT HTML Viewer</h1>
"""

for folder in sorted(files_by_folder.keys()):
    html += f'<div class="folder"><h2>📁 {folder}</h2>'
    for file in sorted(files_by_folder[folder]):
        html += f'<a href="{file}">{os.path.basename(file)}</a>'
    html += "</div>"

html += "</body></html>"

with open(OUTPUT_FILE, "w") as f:
    f.write(html)

print("index.html generated")
