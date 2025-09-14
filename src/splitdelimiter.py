from textnode import TextType, TextNode
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
