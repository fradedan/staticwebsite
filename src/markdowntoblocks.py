import re


def text_import(path):
    with open(path)as f:
        return f.read()
    



def markdown_to_blocks(markdown):

    split = re.split(r'\n\s*\n',markdown)   
    output_list= []

    for i, element in enumerate(split): #initial strip
        stripped = element.strip()
        if stripped != "":
            output_list.append(stripped)   

    return output_list

    

 
    


                



              






file_path = "src/content/text.txt"
text = text_import(file_path)

