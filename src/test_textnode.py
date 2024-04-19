import unittest

from textnode import TextNode


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




if __name__ == "__main__":
    unittest.main()

