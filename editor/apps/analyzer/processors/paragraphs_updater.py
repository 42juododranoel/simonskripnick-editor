from editor.apps.analyzer.entities import Context, Paragraph, SentenceCollection, Text
from editor.base.processors import BaseProcessor


class ParagraphsUpdater(BaseProcessor):
    """Update a paragraph collection from given text."""

    def __init__(self, text: Text, context: Context | None = None) -> None:
        self.text = text
        self.context = context

    def run(self) -> dict:
        paragraphs = self.text.content.splitlines()
        self.text.paragraphs.collection = [
            self.create_paragraph(content, index) for index, content in enumerate(paragraphs)
        ]
        self.text.paragraphs.count = len(self.text.paragraphs.collection)

    def create_paragraph(self, content: str, index: int) -> Paragraph:
        return Paragraph(
            index=index,
            content=content,
            sentences=SentenceCollection(),
        )
