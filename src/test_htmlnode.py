import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_initialization_defaults(self):
        print("\nTesting if initialization defaults are None")
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
        self.assertIsNone(node.value)

    def test_init_with_values(self):
        print("\nTesting init with sepcific values")
        tag = "p"
        value = "Hello world!"
        children = [HTMLNode(tag="b", value="bold text")]
        props = {"class":"paragraph"}

        node = HTMLNode(tag=tag, value=value, children=children, props=props)

        self.assertEqual(node.children, children)
        self.assertEqual(node.value, value)
        self.assertEqual(node.tag, tag)
        self.assertEqual(node.props, props)

    def test_eq_bold_tag(self):
        node = HTMLNode(tag="b", value="abcdef")
        node2 = HTMLNode(tag="b", value="abcdef")
        print(f"\nTesting equality of {node} {node2}")
        self.assertNotEqual(node, node2)

    def test_props_equal(self):
        node = HTMLNode(props= {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        print(node.props_to_html())
        node2 = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        print(node2.props_to_html())
        print(f"\nTesting equality of {node} {node2}")
        self.assertEqual(node.props_to_html(), node2.props_to_html())
