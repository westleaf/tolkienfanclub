from splitdelimiter import *
import unittest

class TestSplitDelimiter(unittest.TestCase):
    def test_text(self):
      node = TextNode("This is text with a `code block` word", TextType.TEXT)
      new_nodes=split_nodes_delimiter([node], "`", TextType.CODE)
      self.assertEqual(new_nodes[1].text, "code block")

    def test_delim_bold(self):
          node = TextNode("This is text with a **bolded** word", TextType.TEXT)
          new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
          self.assertListEqual(
              [
                  TextNode("This is text with a ", TextType.TEXT),
                  TextNode("bolded", TextType.BOLD),
                  TextNode(" word", TextType.TEXT),
              ],
              new_nodes,
          )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )


    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.TEXT),
            ],
            new_nodes,
        )


    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
              TextNode("This is ", TextType.TEXT),
              TextNode("text", TextType.BOLD),
              TextNode(" with an ", TextType.TEXT),
              TextNode("italic", TextType.ITALIC),
              TextNode(" word and a ", TextType.TEXT),
              TextNode("code block", TextType.CODE),
              TextNode(" and an ", TextType.TEXT),
              TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
              TextNode(" and a ", TextType.TEXT),
              TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes
        )
    def test_text_to_textnodes_plain(self):
      text = "Just a plain sentence."
      new_nodes = text_to_textnodes(text)
      self.assertListEqual(
        [TextNode("Just a plain sentence.", TextType.TEXT)],
        new_nodes
      )

    def test_text_to_textnodes_bold(self):
      text = "This is **bold** text."
      new_nodes = text_to_textnodes(text)
      self.assertListEqual(
        [
          TextNode("This is ", TextType.TEXT),
          TextNode("bold", TextType.BOLD),
          TextNode(" text.", TextType.TEXT),
        ],
        new_nodes
      )

    def test_text_to_textnodes_italic(self):
      text = "This is _italic_ text."
      new_nodes = text_to_textnodes(text)
      self.assertListEqual(
        [
          TextNode("This is ", TextType.TEXT),
          TextNode("italic", TextType.ITALIC),
          TextNode(" text.", TextType.TEXT),
        ],
        new_nodes
      )

    def test_text_to_textnodes_code(self):
      text = "Here is `code`."
      new_nodes = text_to_textnodes(text)
      self.assertListEqual(
        [
          TextNode("Here is ", TextType.TEXT),
          TextNode("code", TextType.CODE),
          TextNode(".", TextType.TEXT),
        ],
        new_nodes
      )

    def test_text_to_textnodes_image(self):
      text = "Here is an ![img](https://img.com/img.png)."
      new_nodes = text_to_textnodes(text)
      self.assertListEqual(
        [
          TextNode("Here is an ", TextType.TEXT),
          TextNode("img", TextType.IMAGE, "https://img.com/img.png"),
          TextNode(".", TextType.TEXT),
        ],
        new_nodes
      )

    def test_text_to_textnodes_link(self):
      text = "A [link](https://example.com) here."
      new_nodes = text_to_textnodes(text)
      self.assertListEqual(
        [
          TextNode("A ", TextType.TEXT),
          TextNode("link", TextType.LINK, "https://example.com"),
          TextNode(" here.", TextType.TEXT),
        ],
        new_nodes
      )

    def test_text_to_textnodes_combined(self):
      text = "Mix **bold** and _italic_ and `code` and ![img](url) and [link](url2)"
      new_nodes = text_to_textnodes(text)
      self.assertListEqual(
        [
          TextNode("Mix ", TextType.TEXT),
          TextNode("bold", TextType.BOLD),
          TextNode(" and ", TextType.TEXT),
          TextNode("italic", TextType.ITALIC),
          TextNode(" and ", TextType.TEXT),
          TextNode("code", TextType.CODE),
          TextNode(" and ", TextType.TEXT),
          TextNode("img", TextType.IMAGE, "url"),
          TextNode(" and ", TextType.TEXT),
          TextNode("link", TextType.LINK, "url2"),
        ],
        new_nodes
      )

    def test_text_to_textnodes_multiple_images_links(self):
      text = "![a](a.png) and [b](b.com) and ![c](c.png)"
      new_nodes = text_to_textnodes(text)
      self.assertListEqual(
        [
          TextNode("a", TextType.IMAGE, "a.png"),
          TextNode(" and ", TextType.TEXT),
          TextNode("b", TextType.LINK, "b.com"),
          TextNode(" and ", TextType.TEXT),
          TextNode("c", TextType.IMAGE, "c.png"),
        ],
        new_nodes
      )


    def test_markdown_to_blocks(self):
      md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
      blocks = markdown_to_blocks(md)
      self.assertEqual(
          blocks,
          [
              "This is **bolded** paragraph",
              "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
              "- This is a list\n- with items",
          ],
      )

    def test_markdown_to_blocks_empty(self):
        md = """


"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_markdown_to_blocks_single(self):
        md = """Single paragraph without double newlines."""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Single paragraph without double newlines."])
