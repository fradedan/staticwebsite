import re

def text_import(path):
    with open(path)as f:
        return f.read()    

file_path = "src/content/text.txt"
text = text_import(file_path)

def markdown_to_blocks(markdown):

    split = re.split(r'\n\s*\n',markdown)   
    output_list= []

    for i, element in enumerate(split): #initial strip
        stripped = element.strip()
        if stripped != "":
            output_list.append(stripped)   

    return output_list

def wrapped_line_consolidation(blocks):
    new_block = []
    for block in blocks:        
        lines = block.split('\n')
        for i, line in enumerate(lines):
            pattern = r'^(\s{3,})(.+)'
            match = re.match(pattern,line)
            if match:
                line = match.group(2)
                lines[i-1] = lines[i-1]+ " "+ line
                del lines[i]
            
        new_block.append("\n".join(lines))

    return new_block
        


def block_to_block_type(block):
    lines = block.split('\n')

    def check_every_line(block,delimiter,delimiter2= None):                      #check every line function
        if delimiter2== None:
            delimiter2= delimiter

        if block.startswith(delimiter)or block.startswith(delimiter2):                             
            nonlocal lines
            line_starts_with_delimiter = True
            for item in lines:
                if not item.startswith(delimiter)and not item.startswith(delimiter2):
                    line_starts_with_delimiter= False       
                else:
                    line_starts_with_delimiter=True
            return line_starts_with_delimiter

    def check_ordered_list():                              #check ordered list
            nonlocal lines            
            for line in lines:
                if not re.match(r'^\d+\.\s+',line):
                    return False
            return True
    
    def check_heading():
        nonlocal lines
        for line in lines:
            if not re.match(r'^#{1,6}(?!#)\s*',line):        # check Heading
                return False
        return True
    
    if block.startswith('```') and block.endswith('```'):       #check Code
        return "Code"
        
    if check_heading():
        return "Heading"  
    
    if check_every_line(block,'>'):                             #check quote
        return "Quote"
    
    if check_every_line(block,'*','-'):                             #check unordered list 
        return "Unordered"
    
    
    if check_ordered_list():                               #confirm ordered list
        return "Ordered"
    
    else:
        return "Paragraph"
      







