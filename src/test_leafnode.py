from unittest import TestCase
from leafnode import LeafNode

class TestLeafNode(TestCase):
    def test_init(self):
        print(f"\nLeafNode init value test")
        tag = "p"
        value = "this is a para.."

        node = LeafNode(tag=tag, value=value)
        self.assertEqual(node.tag, tag)
        self.assertEqual(node.value, value)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_node_with_props(self):
        node = LeafNode("span", "text", {"id":"a"})
        self.assertEqual(node.to_html(), '<span id="a">text</span>')
