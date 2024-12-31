
from textnode import TextNode, TextType
from htmlnode import HTMLNODE,ParentNode,LeafNode
from markdowntoblocks import *
from splitnodes import *
from markdowntohtml import *

def text_import(path):
    with open(path)as f:
        return f.read()    

file_path = "src/content/text.txt"
text = text_import(file_path)


final_html = markdown_to_html(text)






