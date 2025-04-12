import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        print(f"\nTesting equality of {node} {node2}")
        self.assertEqual(node, node2)
    
    def test_eq_url(self):
        node = TextNode("This is a link text node", TextType.LINK, "www.google.com")
        node2 = TextNode("This is a link text node", TextType.LINK, "www.google.com")
        print(f"\nTesting equality of {node} {node2}")
        self.assertEqual(node, node2)
    
    def test_eq_different_url(self):
        node = TextNode("This is a link text node", TextType.LINK, "www.google.com")
        node2 = TextNode("This is a link text node", TextType.LINK, "www.yahoo.com")
        print(f"\nTesting inequality of {node} {node2}")
        self.assertNotEqual(node, node2)
    
    def test_ueq_bold_italics(self):
        node = TextNode("This is a italic text node", TextType.ITALIC)
        node2 = TextNode("This is a italic text node", TextType.BOLD)
        print(f"\nTesting inequality of {node} {node2}")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()