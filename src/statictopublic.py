from pathlib import Path
import os
import shutil
from markdowntohtml import *
import re


def copy_items(dir,dir2):

    for file in os.listdir(dir):
            source_path = os.path.join(dir,file)
            destination_path = os.path.join(dir2,file)
            if os.path.isfile(source_path):
                shutil.copy(source_path,destination_path)
            if os.path.isdir(source_path):
                os.mkdir(destination_path)
                copy_items(source_path,destination_path)


def static_to_public(static,public):

    static_dir = static
    public_dir = public

    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
       
    os.mkdir(public_dir)

    if  not os.path.exists(static_dir):
        raise Exception('No static path')
    else:
        copy_items(static_dir,public_dir)


def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path}\nto {dest_path}\nusing {template_path}')
    f = open(from_path)
    markdown= f.read()
    t= open(template_path)
    template = t.read()
    generated_string = markdown_to_html(markdown)
    title =extract_title(markdown)

    final_html = template.replace('{{ Title }}',title).replace('{{ Content }}',generated_string)

    try:
        with open(dest_path,"w") as file:
            print(f'writing generated html into {dest_path}')
            file.write(final_html)
    except FileExistsError:
        print("File already Exists")



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content):
        raise Exception("Content path does not exist")
    if not os.path.exists(template_path):
        raise Exception("Template path does not exist")
    if not os.path.exists(dest_dir_path):
        raise Exception(f"Destination path {dest_dir_path} does not exist")
    
    for file in os.listdir(dir_path_content):
        file_path = os.path.join(dir_path_content,file)
        split_dest = os.path.splitext(file)
        new_dest = "".join(split_dest[0]+".html")
       
        print(file_path)
        if os.path.isfile(file_path):
            dest_file_path = os.path.join(dest_dir_path,new_dest)
            generate_page(file_path,template_path,dest_file_path)

        else:
            dest_file_path = os.path.join(dest_dir_path,file)
            os.mkdir(dest_file_path)            
            generate_pages_recursive(file_path,template_path,dest_file_path)
    






    
    
    


            
