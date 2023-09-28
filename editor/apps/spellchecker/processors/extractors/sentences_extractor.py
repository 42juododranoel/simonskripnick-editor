import nltk

from editor.apps.spellchecker.entities import (
    Context,
    Paragraph,
    Sentence,
    Span,
    Spans,
    SpanSubcategory,
)
from editor.base.processors import BaseProcessor


class SentencesExtractor(BaseProcessor):
    """Extract a sentence collection from a given paragraph`s content."""

    def __init__(self, paragraph: Paragraph, context: Context | None = None) -> None:
        self.paragraph = paragraph
        self.context = context
        self.sentence_count = 0

    def run(self) -> dict:
        sentences = nltk.tokenize.PunktSentenceTokenizer().span_tokenize(self.paragraph.content)

        self.paragraph.sentences.collection = []
        previous_end_index = 0
        for start_index, end_index in sentences:
            if start_index != previous_end_index:
                whitespace = self.paragraph.content[previous_end_index:start_index]
                self.create_whitespace_span(content=whitespace)

            sentence = self.paragraph.content[start_index:end_index]
            self.create_sentence_span(content=sentence)
            self.sentence_count += 1

            previous_end_index = end_index

        maybe_end_index = len(self.paragraph.content)
        if previous_end_index < maybe_end_index:
            whitespace = self.paragraph.content[previous_end_index:maybe_end_index]
            self.create_whitespace_span(content=whitespace)

        self.paragraph.sentences.count = self.sentence_count

    def create_whitespace_span(self, content: str) -> Span:
        token = Span(
            content=content,
            subcategory=SpanSubcategory.WHITESPACE,
        )
        self.paragraph.sentences.collection.append(token)

    def create_sentence_span(self, content: str) -> Sentence:
        sentence = Sentence(
            content=content,
            spans=Spans(),
        )
        self.paragraph.sentences.collection.append(sentence)
