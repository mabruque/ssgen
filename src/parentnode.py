from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    '''
    The tag and children arguments are not optional
    It doesn't take a value argument
    props is optional
    (It's the exact opposite of the LeafNode class)
    '''

    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("No tag provided")
        if not self.children:
            raise ValueError("No children provided")

        html_string = ""
        for node in self.children:
            html_string = html_string + node.to_html()

        return f"<{self.tag}>{html_string}</{self.tag}>"

    def __eq__(self, other) -> bool:
        return self.to_html() == other.to_html()
