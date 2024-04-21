class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # string representing the html tag name (e.g. "p", "a", "h1")
        self.value = value # string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.children = children # list of HTMLNode objects representing the children of this node
        self.props = props # HTML attribute for tag -> Value. e.g. {"href": "https://www.google.com"}

    def to_html(self):
        raise NotImplementedError("to_html not implemented yet.")

    def props_to_html(self):
        if self.props is None:
            return ""
        result = ""
        for prop in self.props:
            result += f' {prop}="{self.props[prop]}"'
        return result

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("value is not set.")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("tag is not set")
        if self.children is None:
            raise ValueError("children not set")
        child_html = ""
        for child in self.children:
            child_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, Children: {self.children}, {self.props})"