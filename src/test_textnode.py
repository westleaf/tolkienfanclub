import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a link node", TextType.LINK)
        node2 = TextNode("This is a italics node", TextType.ITALIC)
        self.assertNotEqual(node.text_type, node2.text_type)

    def test_url_not_empty(self):
        node = TextNode("This is a link", TextType.LINK, url="localhost:1234")
        self.assertNotEqual(node.url, None)

if __name__ == "__main__":
    unittest.main()
