from editor.apps.analyzer.entities import Sentence, Span, Spans, SpanSubcategory
from editor.apps.analyzer.processors import SpansCreator


def test_spans_creator(sentence: Sentence):
    spans_creator = SpansCreator(sentence=sentence)

    spans_creator()

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
