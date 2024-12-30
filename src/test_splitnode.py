
from splitnodes import *


####################################
#Tests for Images 


#Formatting for testing
def format_nodes(nodes):
    formatted = "[\n"
    for node in nodes:
        formatted += f"    {repr(node)},\n"
    formatted += "]"
    return formatted

####################################
####################################

#Test #1 Single Image
node = TextNode(
    "This is text with an Image ![to boot dev](https://www.boot.dev)",
    TextType.TEXT,
)
new_nodes = split_nodes_image([node])
formatted_nodes = format_nodes(new_nodes)

print("Attempting Test# 1: single Image \n The Resulting list is: \n",formatted_nodes)

#Test #2 Double Image
node = TextNode(
    "This is text with an Image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
new_nodes = split_nodes_image([node])
formatted_nodes = format_nodes(new_nodes)

print("Attempting Test# 2: Double Images \n The Resulting list is: \n",formatted_nodes)
#Test #3 Multiple Images
node = TextNode(
    "This is text with an Image ![to boot dev](https://www.boot.dev) , ![to youtube](https://www.youtube.com/@bootdotdev) , ![to baking monkey](https://www.bakingmonkeysg.com) , and ![prawnhub](https://www.prawnhub.com)",
    TextType.TEXT,
)
new_nodes = split_nodes_image([node])
formatted_nodes = format_nodes(new_nodes)

print("Attempting Test# 3: Multiple Images \n The Resulting list is: \n",formatted_nodes)

#Test #4 No Image
node = TextNode(
    "This is text without an Image",
    TextType.TEXT,
)
new_nodes = split_nodes_image([node])
formatted_nodes = format_nodes(new_nodes)

print("Attempting Test# 4: No Image \n The Resulting list is: \n",formatted_nodes)

#Test #5 Mixed Content
node = TextNode(
    "This is text with an Image ![to boot dev](https://www.boot.dev) but it keeps going!",
    TextType.TEXT,
)
new_nodes = split_nodes_image([node])
formatted_nodes = format_nodes(new_nodes)

print("Attempting Test# 5: Mixed Content \n The Resulting list is: \n",formatted_nodes)


#Test #6 EdgeCase with Empty Text
node = TextNode(
    "",
    TextType.TEXT,
)
new_nodes = split_nodes_image([node])
formatted_nodes = format_nodes(new_nodes)

print("Attempting Test# 6: Edge Case no text \n The Resulting list is: \n",formatted_nodes)

#Test #6 EdgeCase with Back to Back Images
node = TextNode("This are two abck to back images ![to boot dev](https://www.boot.dev)![to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
new_nodes = split_nodes_image([node])
formatted_nodes = format_nodes(new_nodes)

print("Attempting Test# 6: Edge Case back to back images \n The Resulting list is: \n",formatted_nodes)


###################################

####################################
#Tests for Links 

#Test #1 Single Link
node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev)",
    TextType.TEXT,
)
new_nodes = split_nodes_link([node])
formatted_nodes = format_nodes(new_nodes)

print("Attempting Test# 1: single Link \n The Resulting list is: \n",formatted_nodes)

#Test #2 Double Link
node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
new_nodes = split_nodes_link([node])
formatted_nodes = format_nodes(new_nodes)

print("Attempting Test# 2: Double Link \n The Resulting list is: \n",formatted_nodes)
#Test #3 Multiple Links
node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) , [to youtube](https://www.youtube.com/@bootdotdev) , [to baking monkey](https://www.bakingmonkeysg.com) , and [prawnhub](https://www.prawnhub.com)",
    TextType.TEXT,
)
new_nodes = split_nodes_link([node])
formatted_nodes = format_nodes(new_nodes)

print("Attempting Test# 3: Multiple Links \n The Resulting list is: \n",formatted_nodes)

#Test #4 No Link
node = TextNode(
    "This is text without a link",
    TextType.TEXT,
)
new_nodes = split_nodes_link([node])
formatted_nodes = format_nodes(new_nodes)

print("Attempting Test# 4: No Link \n The Resulting list is: \n",formatted_nodes)

#Test #5 Mixed Content
node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) but it keeps going!",
    TextType.TEXT,
)
new_nodes = split_nodes_link([node])
formatted_nodes = format_nodes(new_nodes)

print("Attempting Test# 5: Mixed Content \n The Resulting list is: \n",formatted_nodes)


#Test #6 EdgeCase with Empty Text
node = TextNode(
    "",
    TextType.TEXT,
)
new_nodes = split_nodes_link([node])
formatted_nodes = format_nodes(new_nodes)

print("Attempting Test# 6: Edge Case no text \n The Resulting list is: \n",formatted_nodes)

#Test #6 EdgeCase with Back to Back Links
node = TextNode("This are two abck to back Links [to boot dev](https://www.boot.dev) [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
new_nodes = split_nodes_link([node])
formatted_nodes = format_nodes(new_nodes)

print("Attempting Test# 6: Edge Case back to back links \n The Resulting list is: \n",formatted_nodes)



###################################
