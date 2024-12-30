import re
from textnode import TextNode,TextType

def extract_markdown_images(text):    
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)        

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)


def split_nodes_image(old_nodes):
    pass

def split_nodes_link(old_nodes):


    pass






