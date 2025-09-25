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

def generate_page_recursive(from_path, template_path, dest_path):
    if os.path.isdir(from_path):
        for entry in os.listdir(from_path):
            entry_from_path = os.path.join(from_path, entry)
            entry_dest_path = os.path.join(dest_path, entry)
            if os.path.isdir(entry_from_path):
                generate_page_recursive(entry_from_path, template_path, entry_dest_path)
            elif entry.endswith(".md"):
                entry_dest_path = entry_dest_path[:-3] + ".html"
                generate_page(entry_from_path, template_path, entry_dest_path)
    elif from_path.endswith(".md"):
        generate_page(from_path, template_path, dest_path)
