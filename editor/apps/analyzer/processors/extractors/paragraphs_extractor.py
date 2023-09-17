from editor.apps.analyzer.entities import (
    Context,
    HttpParagraph,
    Paragraph,
    Sentences,
    Tree,
)
from editor.base.processors import BaseProcessor


class ParagraphsExtractor(BaseProcessor):
    """Extract paragraphs from tree by concatenating its text nodes."""

    def __init__(self, tree: Tree, context: Context | None = None) -> None:
        self.tree = tree
        self.context = context

    def run(self) -> None:
        self.extract_paragraphs()

    def extract_paragraphs(self) -> None:
        self.tree.paragraphs.collection = [
            self.create_paragraph(paragraph_node) for paragraph_node in self.tree.document.content
        ]
        self.tree.paragraphs.count = len(self.tree.paragraphs.collection)

    def create_paragraph(self, paragraph_node: HttpParagraph) -> str:
        paragraph_content = ""
        for text_node in paragraph_node.content:
            paragraph_content += text_node.text

        return Paragraph(
            content=paragraph_content,
            sentences=Sentences(),
        )
