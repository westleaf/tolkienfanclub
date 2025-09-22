import converter
from block import markdown_to_blocks, block_to_block_type
from textprocessing import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextType, TextNode
from utils import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # moved to textprocessing.py
    raise NotImplementedError("split_nodes_delimiter is now in textprocessing.py")

def split_nodes_image(old_nodes):
    # moved to textprocessing.py
    raise NotImplementedError("split_nodes_image is now in textprocessing.py")

def split_nodes_link(old_nodes):
    # moved to textprocessing.py
    raise NotImplementedError("split_nodes_link is now in textprocessing.py")

def text_to_textnodes(text):
    # moved to textprocessing.py
    raise NotImplementedError("text_to_textnodes is now in textprocessing.py")
