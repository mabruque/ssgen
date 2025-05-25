from textnode import TextNode, TextType
from leafnode import LeafNode
from htmlnode import HTMLNode
import re

def text_node_to_html_node(text_node:TextNode):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href":text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value="", props={"src":text_node.url, "alt":text_node.text})
    else:
        raise Exception("Invalid Text Type")

def split_nodes_delimiter(old_nodes:list[TextNode], delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        split_list = node.text.split(delimiter)
        if len(split_list) % 2 == 0:
           raise ValueError("Invalid markdown. section not closed")
        for i,item in enumerate(split_list):
            if item == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(text=item,text_type=TextType.TEXT))
            else:
                split_nodes.append(TextNode(text=item,text_type=text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text:str):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text:str):
    matches = re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)
    return matches
