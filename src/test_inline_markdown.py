import unittest
from inline_markdown import split_nodes_delimiter
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image
)

class TestInlineMarkdown(unittest.TestCase):
    def test_inline_markdown(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", text_type_text),TextNode("code block", text_type_code),TextNode(" word", text_type_text),])

if __name__ == "__main__":
    unittest.main()