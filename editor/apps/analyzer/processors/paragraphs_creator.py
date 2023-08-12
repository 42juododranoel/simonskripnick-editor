from editor.apps.analyzer.entities import Context, Paragraph, Sentences, Text
from editor.base.processors import BaseProcessor


class ParagraphsCreator(BaseProcessor):
    """Create a paragraph collection for a given text."""

    def __init__(self, text: Text, context: Context | None = None) -> None:
        self.text = text
        self.context = context

    def run(self) -> dict:
        paragraphs = self.text.content.splitlines()
        self.text.paragraphs.collection = [self.create_paragraph(content) for content in paragraphs]
        self.text.paragraphs.count = len(self.text.paragraphs.collection)

    def create_paragraph(self, content: str) -> Paragraph:
        return Paragraph(
            content=content,
            sentences=Sentences(),
        )
