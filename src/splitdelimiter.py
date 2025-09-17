from textnode import TextType, TextNode
from utils import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes=[]
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        texts = node.text.split(delimiter)
        if len(texts) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(texts)):
            if texts[i] == "":
                continue
            if i % 2 != 0:
                new_nodes.append(TextNode(texts[i], text_type))
            else:
                new_nodes.append(TextNode(texts[i], TextType.TEXT))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes=[]
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text == "":
            continue
        extracted_images=extract_markdown_images(node.text)
        sections=[]
        remaining = node.text
        for image_alt, image_link in extracted_images:
            current, remaining = remaining.split(f"![{image_alt}]({image_link})",1)
            if current != "":
              sections.append(TextNode(current, TextType.TEXT))
            sections.append(TextNode(image_alt, TextType.IMAGE, image_link))
        if remaining:
            sections.append(TextNode(remaining, TextType.TEXT))
        new_nodes.extend(sections)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes=[]
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text == "":
            continue
        extracted_images=extract_markdown_links(node.text)
        sections=[]
        remaining = node.text
        for link_text, href in extracted_images:
            current, remaining = remaining.split(f"[{link_text}]({href})",1)
            if current == "":
                continue
            sections.append(TextNode(current, TextType.TEXT))
            sections.append(TextNode(link_text, TextType.LINK, href))
        if remaining:
            sections.append(TextNode(remaining, TextType.TEXT))
        new_nodes.extend(sections)
    return new_nodes
