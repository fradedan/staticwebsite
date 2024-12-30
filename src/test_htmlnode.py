from htmlnode import HTMLNODE, LeafNode, ParentNode
# Test #1

# Test 1: Basic parent with leaf children
node1 = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
    ]
)
print("Test 1:", node1.to_html())
# Should output: <p><b>Bold text</b>Normal text<i>italic text</i></p>

# Test 2: Nested parent nodes
node2 = ParentNode(
    "div",
    [
        ParentNode("p", [LeafNode("b", "Nested bold")])
    ]
)
print("Test 2:", node2.to_html())
# Should output: <div><p><b>Nested bold</b></p></div>

# Test 3: Parent with props
node3 = ParentNode(
    "div",
    [LeafNode("p", "Hello")],
    {"class": "greeting"}
)
print("Test 3:", node3.to_html())
# Should output: <div class="greeting"><p>Hello</p></div>

# Test 4: Error cases
try:
    bad_node1 = ParentNode(None, [LeafNode("p", "test")])
    bad_node1.to_html()
except ValueError as e:
    print("Test 4.1 (No tag):", e)

try:
    bad_node2 = ParentNode("div", [])
    bad_node2.to_html()
except ValueError as e:
    print("Test 4.2 (No children):", e)

# Test 5: Complex nesting with multiple types
node5 = ParentNode(
    "div",
    [
        LeafNode("h1", "Title"),
        ParentNode(
            "p",
            [
                LeafNode("b", "Bold"),
                LeafNode(None, " and "),
                LeafNode("i", "italic"),
            ]
        )
    ]
)

print("Test 5:", node5.to_html())