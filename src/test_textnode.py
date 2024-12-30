import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    '''def test_eq2(self):
        node = TextNode("This is a not text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)'''

    '''def test_eq2(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)'''

    '''def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD,"https://bakingmonkeysg.squarespace.com/config/")
        node2 = TextNode("This is a text node", TextType.BOLD,"https://bakingmonkeysg.squarespace.com/config/")
        self.assertEqual(node, node2)'''





if __name__ == "__main__":
    unittest.main()