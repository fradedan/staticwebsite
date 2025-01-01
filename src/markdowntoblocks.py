import re


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

    def check_unordered_list(block):
        nonlocal lines
        pattern1 = r'^\*\s+'
        pattern2 = r'^\-\s+'
        block_check=True
        for line in lines:
            match1 = re.match(pattern1,line)
            match2 = re.match(pattern2,line)
            if not match1 and not match2 :
                block_check=False  
        return block_check


    def check_block_quote():
        pattern = r'^\>{1}\s*'
        
        block_check = True
        for line in lines:
            match = re.match(pattern,line)
            if not match :
                block_check=False            
        
        return block_check


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
    
    if check_block_quote():                             #check quote
        return "Quote"
    
    if check_unordered_list(block):                             #check unordered list 
        return "Unordered"
    
    
    if check_ordered_list():                               #confirm ordered list
        return "Ordered"
    
    else:
        return "Paragraph"
      







