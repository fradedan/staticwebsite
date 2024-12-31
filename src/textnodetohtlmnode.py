from htmlnode import *
from textnode import *

def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case TextType.TEXT:
            new_type= LeafNode(None,text_node.text)
            return new_type
        case TextType.BOLD:
            new_type= LeafNode("b",text_node.text)
            return new_type
        case TextType.ITALIC:
            new_type= LeafNode("i",text_node.text)
            return new_type
        case TextType.CODE:
            new_type= LeafNode("code",text_node.text)
            return new_type
        case TextType.LINK:
            new_type= LeafNode("a",text_node.text,{'href' : text_node.url})
            return new_type
        case TextType.IMAGE:
            new_type= LeafNode("img","",{'src' : text_node.url, 'alt': text_node.text})
            return new_type
        case _:
            raise Exception('Not a supported Type')
