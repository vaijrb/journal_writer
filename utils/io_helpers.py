import os
from slugify import slugify

def save_draft(topic, content, output_dir="outputs"):
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{slugify(topic)}_draft.txt"
    path = os.path.join(output_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path
