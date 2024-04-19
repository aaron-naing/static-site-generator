class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # tag is string representing the HTML tag name (e.g. "p", "a", "h1", etc.) HTMLNode without tag will just render as raw text. 
        # value is string representing the value of the HTML tag (e.g. the txt inside a paragraph) HTMLNode without a value will be assumed to have childern.
        # children is a list of HTMLNode objects representing the children of this node. HTMLNode without children will be assumed to have a value
        # props is a dict of key-value pairs representing attributes of the HTML tag. HTMLNode without props won't have any attributes
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(sefl):
        raise NotImplementedError
    
    def props_to_html(self):
        html = ""
        if self.props:
            for k, v in self.props.items():
                html += " {}=\"{}\"".format(k, v)
        return html
    

    def __repr__(self):
        repr = ["HTMLNode"]
        repr.append("tag: {}".format(self.tag))
        repr.append("value: {}".format(self.value))
        repr.append("children: {}".format(",".format(self.children)))
        repr.append("props: {}".format(self.props_to_html()))
        return "\n".join(repr)


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if not self.value:
            raise ValueError("No Value!")
        
        # if no tag, return value as raw text
        if not self.tag:
            return self.value
        
        return "<{}{}>{}</{}>".format(self.tag, self.props_to_html(), self.value, self.tag)
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("No Tag!")

        if not self.children:
            raise ValueError("No children!")
        
        children_html = ""
        for node in self.children:
            children_html += node.to_html()
        html = "<{}{}>{}</{}>".format(self.tag, self.props_to_html(), children_html, self.tag)
        return html









