import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_with_props(self):
        node = LeafNode("a", "Some link", {"href":"https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Some link</a>')

    def test_parent(self):
        a = LeafNode("b", "Bold text")
        b = LeafNode(None, "Normal text")
        c = LeafNode("i", "italic text", {"c1":"c1", "c2":"c2"})
        d = LeafNode(None, "Normal text")
        e = ParentNode("p", [a,b,c,d])
        self.assertEqual(e.to_html(), '<p><b>Bold text</b>Normal text<i c1="c1" c2="c2">italic text</i>Normal text</p>')

if __name__ == "__main__":
    unittest.main()
