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
                fatigue=12,  # from repeated_sentence_length_count
            ),
            Span(
                subcategory=SpanSubcategory.WHITESPACE,
                content=" ",
                fatigue=12,
            ),
            Span(
                subcategory=SpanSubcategory.WORD,  # centroid
                content="are",
                fatigue=24,
            ),
            Span(
                subcategory=SpanSubcategory.WHITESPACE,
                content=" ",
                fatigue=24,
            ),
            Span(
                subcategory=SpanSubcategory.WORD,
                content="you",
                fatigue=26,
            ),
            Span(
                subcategory=SpanSubcategory.WHITESPACE,
                content=" ",
                fatigue=26,
            ),
            Span(
                subcategory=SpanSubcategory.WORD,
                content="doing",
                fatigue=28,
            ),
            Span(
                subcategory=SpanSubcategory.WORD,
                content="?",
                fatigue=30,
            ),
        ],
        count=5,
    )
