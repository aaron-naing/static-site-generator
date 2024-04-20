from htmlnode import LeafNode


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self, other):
        return (self.text_type == other.text_type) and (self.text == other.text) and (self.url == other.url)
    

    def __repr__(self):
        return "TextNode({}, {}, {})".format(self.text, self.text_type, self.url)


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            node = LeafNode(None, text_node.text)
        case "bold":
            node = LeafNode("b", text_node.text)
        case "italic":
            node = LeafNode("i", text_node.text)
        case "code":
            node = LeafNode("code", text_node.text)
        case "link":
            node = LeafNode("a", text_node.text, {"href":text_node.url})
        case "image":
            node = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError("Invalid text type: {}".format(text_node.text_type))
    return node
        




