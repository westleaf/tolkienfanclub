import unittest
from utils import *

class TestUtils(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is a text with a [link to site](https://my.cool.site) and [to youtube](https://youtube.com)"
        )
        self.assertListEqual([("link to site", "https://my.cool.site"),
                              ("to youtube","https://youtube.com")
                              ], matches)
