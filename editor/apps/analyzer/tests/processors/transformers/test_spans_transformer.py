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
                content="arw",
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
                fatigue=12,  # accumulated fatigue
            ),
            Span(
                subcategory=SpanSubcategory.WHITESPACE,
                content=" ",
                fatigue=12,
            ),
            Span(
                subcategory=SpanSubcategory.WORD,
                content="arw",
                fatigue=24,  # centroid fatigue
                spellcheck_candidates=[
                    ("are", 0.9065934065934066),
                    ("arm", 0.06543456543456544),
                    ("raw", 0.014485514485514486),
                    ("art", 0.011738261738261738),
                    ("arc", 0.0012487512487512488),
                ],
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
