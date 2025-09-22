from enum import Enum
import re
from htmlnode import *
from textnode import TextNode, TextType
import converter
from textprocessing import text_to_textnodes, split_nodes_delimiter, split_nodes_image, split_nodes_link

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.CODE:
            code_content = "\n".join(block.split("\n")[1:-1])
            if not code_content.endswith("\n"):
                code_content += "\n"
            from textnode import TextNode, TextType
            code_node = converter.text_node_to_html_node(TextNode(code_content, TextType.CODE))
            # Wrap code in <pre><code>...</code></pre>
            code_html = f"<code>{code_node.value}</code>"
            children.append(LeafNode("pre", code_html))
        else:
            children.extend(text_to_children(block, block_type))
    return ParentNode("div", children)

def text_to_children(text, block_type):
    # For all block types except code, parse inline markdown and wrap in appropriate block
    from textprocessing import text_to_textnodes
    from htmlnode import ParentNode, LeafNode
    from textnode import TextType
    nodes = text_to_textnodes(text)
    html_nodes = [converter.text_node_to_html_node(node) for node in nodes]
    if block_type == BlockType.PARAGRAPH:
        # Join lines for paragraphs
        joined = " ".join([line.strip() for line in text.split("\n") if line.strip()])
        nodes = text_to_textnodes(joined)
        html_nodes = [converter.text_node_to_html_node(node) for node in nodes]
        return [ParentNode("p", html_nodes)]
    elif block_type == BlockType.HEADING:
        level = len(re.match(r'#{1,6}', text).group(0))
        content = text[level+1:].strip()
        nodes = text_to_textnodes(content)
        html_nodes = [converter.text_node_to_html_node(node) for node in nodes]
        return [ParentNode(f"h{level}", html_nodes)]
    elif block_type == BlockType.QUOTE:
        # Remove '> ' from the start of every line, join lines with spaces
        quote_lines = [line[2:] if line.startswith('> ') else line for line in text.split('\n') if line.strip()]
        quote_content = ' '.join(quote_lines).strip()
        nodes = text_to_textnodes(quote_content)
        html_nodes = [converter.text_node_to_html_node(node) for node in nodes]
        return [ParentNode("blockquote", html_nodes)]
    elif block_type == BlockType.UNORDERED_LIST:
        items = [item[2:].strip() for item in text.split("\n") if item.startswith("- ")]
        children = [ParentNode("li", [converter.text_node_to_html_node(node) for node in text_to_textnodes(item)]) for item in items]
        return [ParentNode("ul", children)]
    elif block_type == BlockType.ORDERED_LIST:
        items = [item.split(". ", 1)[1].strip() for item in text.split("\n") if item.split(". ")[0].isdigit()]
        children = [ParentNode("li", [converter.text_node_to_html_node(node) for node in text_to_textnodes(item)]) for item in items]
        return [ParentNode("ol", children)]
    else:
        return []

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if re.match(r'#{1,6} ', block):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif block.startswith("> "):
        return BlockType.QUOTE
    elif block.startswith("- "):
        return BlockType.UNORDERED_LIST
    elif block.split(". ")[0].isdigit():
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    nodes = markdown.split("\n\n")
    blocks = []
    for node in nodes:
        if node.strip() == "":
            continue
        blocks.append(node.strip())
    return blocks

def block_to_html_node(block, block_type: BlockType):
    match block_type:
        case BlockType.PARAGRAPH:
            return ParentNode("p", text_to_textnodes(block))
        case BlockType.HEADING:
            level = len(re.match(r'#{1,6}', block).group(0))
            content = block[level+1:].strip()
            return ParentNode(f"h{level}", text_to_textnodes(content))
        case BlockType.CODE:
            code_content = "\n".join(block.split("\n")[1:-1])
            return LeafNode("pre", code_content)
        case BlockType.QUOTE:
            quote_content = block[2:].strip()
            return ParentNode("blockquote", text_to_textnodes(quote_content))
        case BlockType.UNORDERED_LIST:
            items = [item[2:].strip() for item in block.split("\n") if item.startswith("- ")]
            children = [ParentNode("li", text_to_textnodes(item)) for item in items]
            return ParentNode("ul", children)
        case BlockType.ORDERED_LIST:
            items = [item.split(". ", 1)[1].strip() for item in block.split("\n") if re.match(r'\d+\. ', item)]
            children = [ParentNode("li", text_to_textnodes(item)) for item in items]
            return ParentNode("ol", children)
        case _:
            raise ValueError(f"Unsupported block type: {block_type}")
