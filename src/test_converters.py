from unittest import TestCase
from htmlnode import HTMLNode
from textnode import TextNode, TextType
from converters import text_node_to_html_node

class TestConverters(TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_a_href(self):
        node = TextNode(text="Google", text_type=TextType.LINK, url="www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"a")
        self.assertEqual(html_node.props, {"href":"www.google.com"})

    def text_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertIsNone(html_node.props)
