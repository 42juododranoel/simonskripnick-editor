from editor.apps.analyzer.entities import SentenceLength, Span, Spans, SpanSubcategory
from editor.apps.analyzer.processors import SpansTransformer


def test_spans_transformer():
    spans = Spans(
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
    spans_transformer = SpansTransformer(
        spans=spans,
        sentence_length=SentenceLength.SHORT,
        sentence_centroid=1,
        repeated_sentence_length_count=2,
    )

    spans_transformer()

    assert spans == Spans(
        collection=[
            Span(
                subcategory=SpanSubcategory.WORD,
                content="What",
                fatigue=8,  # from repeated_sentence_length_count
            ),
            Span(
                subcategory=SpanSubcategory.WHITESPACE,
                content=" ",
                fatigue=8,
            ),
            Span(
                subcategory=SpanSubcategory.WORD,  # centroid
                content="are",
                fatigue=16,
            ),
            Span(
                subcategory=SpanSubcategory.WHITESPACE,
                content=" ",
                fatigue=16,
            ),
            Span(
                subcategory=SpanSubcategory.WORD,
                content="you",
                fatigue=18,
            ),
            Span(
                subcategory=SpanSubcategory.WHITESPACE,
                content=" ",
                fatigue=18,
            ),
            Span(
                subcategory=SpanSubcategory.WORD,
                content="doing",
                fatigue=20,
            ),
            Span(
                subcategory=SpanSubcategory.WORD,
                content="?",
                fatigue=22,
            ),
        ],
        count=5,
    )
