from editor.apps.spellchecker.entities import Sentence, Span, Spans, SpanSubcategory
from editor.apps.spellchecker.processors import SpansExtractor


def test_spans_extractor(sentence: Sentence):
    spans_extractor = SpansExtractor(sentence=sentence)

    spans_extractor()

    assert sentence.spans == Spans(
        collection=[
            Span(
                subcategory=SpanSubcategory.WORD,
                content="What",
            ),
            Span(
                subcategory=SpanSubcategory.WHITESPACE,
                content=" ",
            ),
            Span(
                subcategory=SpanSubcategory.WORD,
                content="are",
            ),
            Span(
                subcategory=SpanSubcategory.WHITESPACE,
                content=" ",
            ),
            Span(
                subcategory=SpanSubcategory.WORD,
                content="you",
            ),
            Span(
                subcategory=SpanSubcategory.WHITESPACE,
                content=" ",
            ),
            Span(
                subcategory=SpanSubcategory.WORD,
                content="doing",
            ),
            Span(
                subcategory=SpanSubcategory.WORD,
                content="?",
            ),
        ],
        count=5,
    )
