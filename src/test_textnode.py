import unittest

from textnode import TextNode, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)


    def test_eq_with_url(self):
        node = TextNode("test node", "bold", "www.google.com")
        node2 = TextNode("test node", "bold", "www.google.com")
        self.assertEqual(node, node2)

    
    def test_not_eq_text(self):
        node = TextNode("test node 1", "bold")
        node2 = TextNode("test nod 2", "bold")
        self.assertNotEqual(node, node2)


    def test_not_eq_text_type(self):
        node = TextNode("test node", "bold")
        node2 = TextNode("test node", "italic")
        self.assertNotEqual(node, node2)


    def test_not_eq_url(self):
        node = TextNode("test node", "bold", "www.google.com")
        node2 = TextNode("test node", "bold", "www.oracle.com")
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node(self):
        node1 = TextNode("bold text", "bold")
        node2 = TextNode("italic text", "italic")
        node3 = TextNode("code text", "code")
        node4 = TextNode("link text", "link", "www.google.com")
        node5 = TextNode("alt text", "image", "www.imgur.com")
        self.assertEqual(text_node_to_html_node(node1), LeafNode("b", "bold text"))
        self.assertEqual(text_node_to_html_node(node2), LeafNode("i", "italic text"))
        self.assertEqual(text_node_to_html_node(node3), LeafNode("code", "code text"))
        self.assertEqual(text_node_to_html_node(node4), LeafNode("a", "link text", {"href":"www.google.com"}))
        self.assertEqual(text_node_to_html_node(node5), LeafNode("img", "", {"alt":"alt text", "src":"www.imgur.com"}))







if __name__ == "__main__":
    unittest.main()


