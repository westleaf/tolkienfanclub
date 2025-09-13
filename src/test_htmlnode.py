import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
  def test_props_to_html_single(self):
    node = HTMLNode(tag="a", props={"href": "https://example.com"})
    self.assertEqual(node.props_to_html(), ' href="https://example.com"')

  def test_props_to_html_multiple(self):
    node = HTMLNode(tag="a", props={"href": "https://example.com", "target": "_blank"})
    expected = ' href="https://example.com" target="_blank"'
    self.assertEqual(node.props_to_html(), expected)

  def test_repr_output(self):
    node = HTMLNode(tag="p", value="Hello world", props={"class": "intro"})
    repr_str = repr(node)
    self.assertIn("HTMLNode", repr_str)
    self.assertIn("Hello world", repr_str)
    self.assertIn("intro", repr_str)

if __name__ == "__main__":
  unittest.main()
