from markdowntoblocks import *
from htmlnode import *
from textnode import *
from splitnodes import *
from textnodetohtlmnode import text_node_to_html_node



def markdown_to_html(text):
    blocks = wrapped_line_consolidation(markdown_to_blocks(text))    
    
    parent_nodes = []
    created_node = []
    for block in blocks:    
        block_type = block_to_block_type(block)           
        

        ### case for Heading type ###
        if block_type== "Heading":
            child_nodes = []
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
            
            child_nodes = []
            text_node = text_to_textnodes(block)
            for node in text_node:
                child_nodes.append(text_node_to_html_node(node))
            parent_nodes.append(ParentNode("p",child_nodes))
        
        ### case for ordered list ###
        if block_type == "Ordered":
            list_child_nodes = []        
            lines= block.split('\n')
            for line in lines:
                child_nodes = []
                pattern = r'(^\d+\.\s+)(.+)'
                match = re.match(pattern,line)
                text_node = text_to_textnodes(match.group(2))
                for node in text_node:
                    child_nodes.append(text_node_to_html_node(node))
                list_child_nodes.append(ParentNode('li',child_nodes))
                    
            parent_nodes.append(ParentNode(f'ol',list_child_nodes))

        ### case for unordered list ###
        if block_type == "Unordered":
            
            list_child_nodes = []        
            lines= block.split('\n')
            for line in lines:
                child_nodes = []
                if line[1]==" ":
                    line = line[2:]
                else:
                    line = line[1:]

                text_node = text_to_textnodes(line)
                for node in text_node:
                    child_nodes.append(text_node_to_html_node(node))
                list_child_nodes.append(ParentNode('li',child_nodes))
                    
            parent_nodes.append(ParentNode(f'ul',list_child_nodes))

        ### case for Code ###
        if block_type== "Code":
            child_nodes = []
            lines= block.split('\n')
            if lines[0].startswith('```'):
                lines = lines[1:]
            if lines[-1].endswith('```'):
                lines = lines[:-1]

            code_content = "\n".join(lines)

            code_node= LeafNode('code',code_content)
            pre_node = ParentNode('pre',[code_node])

            parent_nodes.append(pre_node)

        ### case for Quote ###
        if block_type == "Quote":
            child_nodes = []
            lines = block.split('\n')
            pattern = r'^(\>\s*)(.+)'
            for i, line in enumerate(lines):
                match = re.match(pattern,line)
                if match :
                    line = match.group(2)
                    lines[i] = line

            quote_content = "\n".join(lines)

            text_node = text_to_textnodes(quote_content)
            for node in text_node:
                    child_nodes.append(text_node_to_html_node(node))

            parent_nodes.append(ParentNode(f'blockquote',child_nodes))  
                    
            

    created_node= ParentNode('div',parent_nodes)
    return created_node.to_html()


def extract_title(markdown):
    blocks = wrapped_line_consolidation(markdown_to_blocks(markdown))
    for block in blocks:
        
        block_type = block_to_block_type(block)
        if block_type == "Heading":
            pattern = r'^(#(?!#)\s+)(.+)'
            match= re.match(pattern,block)
            if match:
                return (match.group(2))
        


