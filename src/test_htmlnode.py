import unittest
from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode
)

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            "a",
            "Click Here!",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        expected_result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_result)

    def test_eq2(self):
        node = HTMLNode(
            None,
            None,
            None,
            None,
        )
        expected_result = ""
        self.assertEqual(node.props_to_html(), expected_result)

    def test_to_html(self):
        node = LeafNode(
            "p",
            "This is a paragraph of text.",
        )
        expected_result = '<p>This is a paragraph of text.</p>'
        self.assertEqual(node.to_html(), expected_result)

    def test_to_html2(self):
        node = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.com"}
        )
        expected_result = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected_result)

    def test_parent_node(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected_result = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(), expected_result)

    def test_parent_node2(self):
        node = ParentNode(
            "div",
            [
                ParentNode("a", [LeafNode("b", "Google")], {"href": "https://www.google.com"}),
                LeafNode("i", "italic text"),
            ],
            {"class": "main"}
        )
        expected_result = '<div class="main"><a href="https://www.google.com"><b>Google</b></a><i>italic text</i></div>'
        self.assertEqual(node.to_html(), expected_result)

if __name__ == "__main__":
    unittest.main()