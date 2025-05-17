from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None,value=None, props=None) -> None:
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value
        html_render = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return html_render
