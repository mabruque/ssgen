

class HTMLNode:
    """

    tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
    value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
    children - A list of HTMLNode objects representing the children of this node
    props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}

    """
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        html_props_string = ""
        if self.props:
            for key in self.props:
                html_props_string = html_props_string + f' {key}="{self.props[key]}"'
        return html_props_string

    def __repr__(self) -> str:
        return(f"HTMLNode({self.tag}, {self.props}, {self.value}, {self.children})")

    def __eq__(self, other) -> bool:
        return self.props_to_html == other.props_to_html and self.value == other.value and self.tag == other.tag and self.children == other.children
