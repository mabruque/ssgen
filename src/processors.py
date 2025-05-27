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

def split_nodes_image(old_nodes:list[TextNode]):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        images = extract_markdown_images(text=text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = text.split(f"![{image[0]}]({image[1]})")
            if len(sections) != 2 :
                raise ValueError("invalid markdown")
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0],TextType.IMAGE, image[1]))
            text = sections[1]
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes:list[TextNode]):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        links = extract_markdown_links(text=text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = text.split(f"[{link[0]}]({link[1]})")
            if len(sections) != 2 :
                raise ValueError("invalid markdown")
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0],TextType.LINK, link[1]))
            text = sections[1]
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    new_nodes = []
    full_text_node = TextNode(text=text, text_type=TextType.TEXT)
    new_nodes.extend(split_nodes_link([full_text_node]))
    new_nodes.extend(split_nodes_image(new_nodes))
    new_nodes.extend(split_nodes_delimiter(new_nodes,"**",TextType.BOLD))
    new_nodes.extend(split_nodes_delimiter(new_nodes,"`",TextType.CODE))
    new_nodes.extend(split_nodes_delimiter(new_nodes,"_",TextType.ITALIC))

    return new_nodes
