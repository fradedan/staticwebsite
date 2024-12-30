from splitnodes import*

counter = 1


#'''
#Test 1

text= "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

split= text_to_textnodes(text)
formatted = format_nodes(split)
print(f"Test {counter} straightforward :\ninput = {text} \n\n{formatted}")
counter+=1


#Test 2
text= "This is pure text"

split= text_to_textnodes(text)
formatted = format_nodes(split)
print(f"Test {counter} pure text :\ninput = {text} \n\n{formatted}")
counter+=1

#Test 3
text= "This is *text* with a **Bold** word and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a `code block` and a [link](https://boot.dev)"

split= text_to_textnodes(text)
formatted = format_nodes(split)
print(f"Test {counter} jumbled :\ninput = {text} \n\n{formatted}")
counter+=1

#Test 4
text= "This is an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) that uses `code block` to *take you* to a **XXX** website, which is [link](https://boot.dev)"

split= text_to_textnodes(text)
formatted = format_nodes(split)
print(f"Test {counter} another jumbled :\ninput = {text}\n\n{formatted}")
counter+=1


#Test 5
text= "This one only has *italics*"

split= text_to_textnodes(text)
formatted = format_nodes(split)
print(f"Test {counter}: only italics :\ninput = {text}\n\n{formatted}")
counter+=1

#Test 6
text= "This one only has **bold**"

split= text_to_textnodes(text)
formatted = format_nodes(split)
print(f"Test {counter}: only bold :\ninput = {text}\n\n{formatted}")
counter+=1

#Test 7
text= "This one only has **bold** and *italics* and **bold again**"

split= text_to_textnodes(text)
formatted = format_nodes(split)
print(f"Test {counter}:bold and italics :\ninput = {text}\n\n{formatted}")
counter+=1

#Test 8
text= "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) image start!"

split= text_to_textnodes(text)
formatted = format_nodes(split)
print(f"Test {counter}:image start:\ninput = {text}\n\n{formatted}")
counter+=1

#Test 9
text= "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"

split= text_to_textnodes(text)
formatted = format_nodes(split)
print(f"Test {counter}:just image: \n\n{formatted}")
counter+=1

#Test 9
text= "[link](https://boot.dev)"

split= text_to_textnodes(text)
formatted = format_nodes(split)
print(f"Test {counter}:just link:\ninput = {text}\n\n{formatted}")
counter+=1
#'''

#Test 9
text= "[link](https://boot.dev) ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "

split= text_to_textnodes(text)
formatted = format_nodes(split)
print(f"Test {counter}:link image:\ninput = {text}\n\n{formatted}")
counter+=1

#Test 12
text= "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)[link](https://boot.dev)  "

split= text_to_textnodes(text)
formatted = format_nodes(split)
print(f"Test {counter}:link image:\ninput = {text}\n\n{formatted}")
counter+=1

#Test 13
text= "**bold**"

split= text_to_textnodes(text)
formatted = format_nodes(split)
print(f"Test {counter}:link image:\ninput = {text}\n\n{formatted}")
counter+=1

#Test 13
text= "*italic* not bold **bold**"

split= text_to_textnodes(text)
formatted = format_nodes(split)
print(f"Test {counter}:link image:\ninput = {text}\n\n{formatted}")
counter+=1