from textnode import (TextNode, 
                      text_type_italic, 
                      text_type_code, 
                      text_type_text, 
                      text_type_bold)
from inline_markdown import (split_nodes_delimiter, 
                             extract_markdown_images, 
                             extract_markdown_links, 
                             split_nodes_image, 
                             split_nodes_link,
                             text_to_textnodes)
from htmlnode import (HTMLNode, 
                      LeafNode, 
                      ParentNode)

# a = LeafNode(None, "valueA", {"propsa":"propsA"})
# b = LeafNode("tagB", "valueB", {"d" : "e", "f" : "g"})
# c = LeafNode("tagC", "valueC", {"href":"https://www.google.com"})
# d = ParentNode("parenttag", [a,b,c], {"parentprops":"pprops"})
# print(d.to_html())


# node = TextNode("This is a text with *italic* and **bold** words", text_type_text)
# new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
# new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
# print(new_nodes)

# text = "This is text with an ![image](https://storage.googleais.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
# print(extract_markdown_images(text))


# text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
# print(extract_markdown_links(text))

# node = TextNode("This is text with an ![first image](https://storage.googleais.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)", text_type_text)
# split_nodes_image([node])

text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev) with some text"
print(text_to_textnodes(text))


