from markdowntoblocks import *
from htmlnode import *
from textnode import *
from splitnodes import *
from textnodetohtlmnode import text_node_to_html_node

def text_import(path):
    with open(path)as f:
        return f.read()    

file_path = "src/content/text.txt"
text = text_import(file_path)

blocks= markdown_to_blocks(text)
parent_nodes = []
created_node = []
for block in blocks:    
    block_type = block_to_block_type(block)
    child_nodes = []
    

    ### case for Heading typ e###
    if block_type== "Heading":
        counter = 0
        full_hash= []
        for letter in block:
            if letter == "#":
                full_hash.append(letter)
                counter +=1
        hash_count= "h"+ str(counter)
        block = block.replace("".join(full_hash)+" ","")
        text_node = text_to_textnodes(block)
        for node in text_node:
            child_nodes.append(text_node_to_html_node(node))
        parent_nodes.append(ParentNode(hash_count,child_nodes))

    ### case for Paragraph type ###
    if block_type == "Paragraph":
        text_node = text_to_textnodes(block)
        for node in text_node:
            child_nodes.append(text_node_to_html_node(node))
        parent_nodes.append(ParentNode("p",child_nodes))





created_node= ParentNode('div',parent_nodes)

  
        
        


        

print(created_node.to_html())