from statictopublic import static_to_public, generate_page, generate_pages_recursive
import os
        

current_path= os.getcwd()

template_name= "template.html"
static_name = "static"
public_name = "public"
content = "content"
original_markdown_name = 'content/index.md'
html_name = "index.html"

template_path = os.path.join(current_path,template_name)
static_path = os.path.join(current_path,static_name)
public_path = os.path.join(current_path,public_name)
from_path = os.path.join(current_path,original_markdown_name)
dest_path = os.path.join(public_path,html_name)
content_dir_path = os.path.join(current_path,content)




static_to_public(static_path,public_path)
generate_pages_recursive(content_dir_path,template_path,public_path)

