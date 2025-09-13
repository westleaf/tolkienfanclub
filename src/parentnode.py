from htmlnode import HTMLNode
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, props)
        self.children = children

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag is not set")
        if len(self.children) == 0:
            raise ValueError("children are empty")
        child_html="".join(child.to_html() for child in self.children)

        return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"
