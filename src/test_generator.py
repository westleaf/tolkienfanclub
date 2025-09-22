import unittest

from generator import *

class TestGenerator(unittest.TestCase):
    def test_extract_title(self):
        md = """
# My Title
Some content here.
"""
        title = extract_title(md)
        self.assertEqual(title, "My Title")

    def test_extract_title_no_title(self):
        md = """
Some content here without a title.
"""
        title = extract_title(md)
        self.assertEqual(title, "Untitled")

    def test_extract_title_multiple_titles(self):
        md = """
# First Title
Some content here.
# Second Title
More content.
"""
        title = extract_title(md)
        self.assertEqual(title, "First Title")

    def test_extract_multiple_pounds(self):
        md = """
### Subtitle Here
Some content here.
"""
        title = extract_title(md)
        self.assertEqual(title, "Untitled")

if __name__ == "__main__":
    unittest.main()
