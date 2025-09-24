import converter
import os
import block

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled"

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")
    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()
    title = extract_title(markdown)
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    html_node = block.markdown_to_html_node(markdown)
    html_content = html_node.to_html()
    final_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)
