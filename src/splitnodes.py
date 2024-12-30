from textnode import TextNode,TextType
import re

def extract_markdown_images(text):    
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)        

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:   
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue

        inverted = False     
        split_list = []
        split_text= node.text.split(delimiter)
        if split_text[0]== "":
            inverted = True
        
        if split_text[-1] == "":
            split_text = split_text[:-1]
            
        for i, text in enumerate(split_text):        
           
            if i%2!=0:
                split_list.append(TextNode(text,text_type))
            else:
                split_list.append(TextNode(text,node.text_type))

        new_list.extend(split_list)
                  
    
    return new_list

def split_nodes_image(old_nodes):
    new_list = []
    for node in old_nodes:  
        inverted=False
        nodetext=node.text
        if not nodetext:
            pass
        split_list = []
        link_extract = extract_markdown_images(nodetext)

        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue

        if link_extract:
            for tup in link_extract:    
                nodetext= nodetext.split(f"![{tup[0]}]({tup[1]})")    
                nodetext= [item for item in nodetext if not item.isspace()] 

                if len(nodetext)>0:    
                    if nodetext[0]== "":
                        nodetext = nodetext[1:]
                        inverted=True

                if not inverted:
                    if nodetext and nodetext[0]!="":                  
                        split_list.append(TextNode(nodetext[0],node.text_type))
                    split_list.append(TextNode(tup[0],TextType.IMAGE,tup[1]))            
                    nodetext="".join(nodetext[1:])
                else:
                    split_list.append(TextNode(tup[0],TextType.IMAGE,tup[1]))
                    if nodetext and nodetext[0]!="":
                        split_list.append(TextNode(nodetext[0],node.text_type)) 
                    nodetext="".join(nodetext[1:])  
            inverted=False

        if nodetext != "":
            split_list.append(TextNode(nodetext,TextType.TEXT))


        new_list.extend(split_list)        

    return new_list

def split_nodes_link(old_nodes):
    new_list = []
    for node in old_nodes:  
        inverted=False
        nodetext=node.text
        if not nodetext:
            pass
        split_list = []
        link_extract = extract_markdown_links(nodetext)

        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue

        if link_extract:
            for tup in link_extract:    
                nodetext= nodetext.split(f"[{tup[0]}]({tup[1]})")   
                nodetext= [item for item in nodetext if not item.isspace()] 
                if len(nodetext)>0:
                    if nodetext[0]== "":
                        nodetext = nodetext[1:]
                        inverted=True

                if not inverted:
                    if nodetext and nodetext[0]!="":                  
                        split_list.append(TextNode(nodetext[0],node.text_type))
                    split_list.append(TextNode(tup[0],TextType.LINK,tup[1]))            
                    nodetext="".join(nodetext[1:])
                else:
                    split_list.append(TextNode(tup[0],TextType.LINK,tup[1]))
                    if nodetext and nodetext[0]!="":
                        split_list.append(TextNode(nodetext[0],node.text_type)) 
                    nodetext="".join(nodetext[1:])  
            inverted=False

        if nodetext != "":
            split_list.append(TextNode(nodetext,TextType.TEXT))


        new_list.extend(split_list)        

    return new_list



def text_to_textnodes(text):
    full = []
    full.append(TextNode(text,TextType.TEXT))
    full= split_nodes_delimiter(full,"**",TextType.BOLD)
    full= split_nodes_delimiter(full,"*",TextType.ITALIC)
    full= split_nodes_delimiter(full,"`",TextType.CODE)
    full= split_nodes_link(full)
    full= split_nodes_image(full)
    return full
    





####################################
#Tests for Images 


#Formatting for testing
def format_nodes(nodes):
    formatted = "[\n"
    for node in nodes:
        formatted += f"    {repr(node)},\n"
    formatted += "]"
    return formatted
counter =1
####################################

