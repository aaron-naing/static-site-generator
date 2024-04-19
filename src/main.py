from textnode import TextNode
from htmlnode import HTMLNode

a = TextNode("This is a text node", "bold", "https://www.boot.dev")
b = HTMLNode("a", "b", ["c"], {"d" : "e", "f" : "g"})
print(b.props_to_html())

