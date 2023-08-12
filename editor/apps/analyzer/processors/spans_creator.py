import nltk

from editor.apps.analyzer.entities import Context, Sentence, Span, SpanSubcategory
from editor.base.processors import BaseProcessor


class SpansCreator(BaseProcessor):
    """Create a span collection for a given sentence."""

    def __init__(self, sentence: Sentence, context: Context | None = None) -> None:
        self.sentence = sentence
        self.context = context
        self.word_count = 0

    def run(self) -> dict:
        words = nltk.tokenize.TreebankWordTokenizer().span_tokenize(self.sentence.content)

        self.sentence.spans.collection = []
        previous_end_index = 0
        for start_index, end_index in words:
            if start_index != previous_end_index:
                self.create_span(
                    content=self.sentence.content[previous_end_index:start_index],
                    subcategory=SpanSubcategory.WHITESPACE,
                )

            self.create_span(
                content=self.sentence.content[start_index:end_index],
                subcategory=SpanSubcategory.WORD,
            )
            self.word_count += 1

            previous_end_index = end_index

        maybe_end_index = len(self.sentence.content)
        if previous_end_index < maybe_end_index:
            self.create_span(
                content=self.sentence.content[previous_end_index:maybe_end_index],
                subcategory=SpanSubcategory.WHITESPACE,
            )

        self.sentence.spans.count = self.word_count

    def create_span(self, content: str, subcategory: str) -> Span:
        span = Span(
            content=content,
            subcategory=subcategory,
        )
        self.sentence.spans.collection.append(span)
