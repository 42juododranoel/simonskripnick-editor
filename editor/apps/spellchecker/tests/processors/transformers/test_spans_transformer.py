from editor.apps.spellchecker.entities import Span, Spans, SpanSubcategory
from editor.apps.spellchecker.processors import SpansTransformer


def test_spans_transformer():
    spans = Spans(
        collection=[
            Span(
                subcategory=SpanSubcategory.WORD,
                content="Appple",
            ),
        ],
        count=1,
    )
    spans_transformer = SpansTransformer(spans=spans)

    spans_transformer()

    assert spans == Spans(
        collection=[
            Span(
                subcategory=SpanSubcategory.WORD,
                content="Appple",
                fatigue=0,
                spellcheck_candidates=[
                    ("Apple", 0.4583333333333333),
                    ("Supple", 0.2916666666666667),
                    ("Nipple", 0.25),
                ],
            ),
        ],
        count=1,
    )
