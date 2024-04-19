from textnode import TextNode
from htmlnode import HTMLNode, LeafNode

a = TextNode("This is a text node", "bold", "https://www.boot.dev")
b = HTMLNode("a", "b", ["c"], {"d" : "e", "f" : "g"})
c = LeafNode("a", "Some link", {"href":"https://www.google.com"})
print(c.to_html())

