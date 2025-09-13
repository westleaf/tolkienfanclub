from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def text_node_to_html_node(textnode):
  match textnode.text_type:
    case TextType.TEXT:
        return LeafNode(None,textnode.text)
    case TextType.BOLD:
        return LeafNode("b", textnode.text)
    case TextType.ITALIC:
        return LeafNode("i", textnode.text)
    case TextType.CODE:
        return LeafNode("code", textnode.text)
    case TextType.LINK:
        return LeafNode("a", textnode.text, {"href": textnode.url})
    case TextType.IMAGE:
        return LeafNode("img", "", {"src": textnode.url, "alt": textnode.text})
    case _:
        raise ValueError(f"invalid text type: {textnode.text_type}")
