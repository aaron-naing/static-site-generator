import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "b", ["c"], {"d": "e"})
        self.assertEqual(node.props_to_html(), ' d="e"')

    def test_to_html(self):
        node = LeafNode("p", "a paragraph")
        self.assertEqual(node.to_html(), "<p>a paragraph</p>")

    def test_to_html2(self):
        node = LeafNode(None, "no tags")
        self.assertEqual(node.to_html(), "no tags")
    
    def test_leaf_no_value(self):
        node = LeafNode(None, None)
        node.to_html()


if __name__ == "__main__":
    unittest.main()