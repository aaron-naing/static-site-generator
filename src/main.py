from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

a = LeafNode(None, "valueA", {"propsa":"propsA"})
b = LeafNode("tagB", "valueB", {"d" : "e", "f" : "g"})
c = LeafNode("tagC", "valueC", {"href":"https://www.google.com"})
d = ParentNode("parenttag", [a,b,c], {"parentprops":"pprops"})
print(d.to_html())

