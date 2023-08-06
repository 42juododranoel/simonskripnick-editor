import nltk

from editor.apps.analyzer.entities import Context, Paragraph, Sentence, TokenCollection
from editor.base.processors import BaseProcessor


class SentencesUpdater(BaseProcessor):
    """Update a sentence collection from given paragraph."""

    def __init__(self, paragraph: Paragraph, context: Context | None = None) -> None:
        self.paragraph = paragraph
        self.context = context

    def run(self) -> dict:
        sentences = nltk.sent_tokenize(self.paragraph.content)
        self.paragraph.sentences.collection = [
            self.create_sentece(content, index) for index, content in enumerate(sentences)
        ]
        self.paragraph.sentences.count = len(self.paragraph.sentences.collection)

    def create_sentece(self, content: str, index: int) -> Sentence:
        return Sentence(
            index=index,
            content=content,
            tokens=TokenCollection(),
        )
