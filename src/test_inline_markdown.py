from unittest import TestCase
from textnode import TextNode
from inline_markdown import (split_nodes_delimiter, 
                             extract_markdown_images, 
                             extract_markdown_links,
                             split_nodes_image,
                             split_nodes_link)


from textnode import (
    text_type_italic,
    text_type_code,
    text_type_bold,
    text_type_image,
    text_type_link,
    text_type_text
)


class Test_Inline_Markdown(TestCase):
    def test_delim_italic(self):
        node = TextNode("This is text with a *italized* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("italized", text_type_italic),
                TextNode(" word", text_type_text)
            ],
            new_nodes
        )


    def test_delim_italic_double(self):
        node = TextNode("This is a text with two *italized* *words*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertEqual(
            [
                TextNode("This is a text with two ", text_type_text),
                TextNode("italized", text_type_italic),
                TextNode(" ", text_type_text),
                TextNode("words", text_type_italic)
            ],
            new_nodes
        )


    def test_delim_bold_double_multiword(self):
        node = TextNode("One two three **four five** six.", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertEqual(
            [
                TextNode("One two three ", text_type_text),
                TextNode("four five", text_type_bold),
                TextNode(" six.", text_type_text)
            ],
            new_nodes
        )

    def test_delim_two_delim(self):
        node = TextNode("One *two* three **four**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertEqual(
            [
                TextNode("One ", text_type_text),
                TextNode("two", text_type_italic),
                TextNode(" three ", text_type_text),
                TextNode("four", text_type_bold)
            ],
            new_nodes
        )

    
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleais.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        markdown_images = extract_markdown_images(text)
        self.assertEqual([('image', 'https://storage.googleais.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png'), 
                          ('another', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png')], 
                          markdown_images)


    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        markdown_links = extract_markdown_links(text)
        self.assertEqual([('link', 'https://www.example.com'), 
                          ('another', 'https://www.example.com/another')],
                          markdown_links)



    def test_split_node_image(self):
        node = TextNode("This is text with an ![first image](https://storage.googleais.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)", 
                        text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertEqual([TextNode("This is text with an ", text_type_text, None), 
                          TextNode("first image", text_type_image, "https://storage.googleais.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                          TextNode(" and another ", text_type_text, None),
                          TextNode("second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")],
                          new_nodes)


    def test_split_node_image_2_nodes(self):
        node1 = TextNode("No image in this one.", text_type_text)
        node2 = TextNode("One ![Two](https://www.three.com) four", text_type_text)
        new_nodes = split_nodes_image([node1, node2])
        self.assertEqual([node1,
                          TextNode("One ", text_type_text, None),
                          TextNode("Two", text_type_image, "https://www.three.com"),
                          TextNode(" four", text_type_text, None)],
                          new_nodes)











