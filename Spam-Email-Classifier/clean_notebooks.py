import os
import json

def clean_notebook_metadata(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    
    if "widgets" in nb.get("metadata", {}):
        widgets = nb["metadata"]["widgets"]
        if "state" not in widgets:
            
            nb["metadata"].pop("widgets", None)
            print(f"⚡ Fixed widgets metadata in: {file_path}")

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=2)

def clean_all_ipynb(root="."):
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(".ipynb"):
                clean_notebook_metadata(os.path.join(dirpath, filename))

if __name__ == "__main__":
    clean_all_ipynb(".")  
