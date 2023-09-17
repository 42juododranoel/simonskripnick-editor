from editor.apps.analyzer.entities import (
    Paragraph,
    Sentence,
    Sentences,
    Span,
    Spans,
    SpanSubcategory,
)
from editor.apps.analyzer.processors import SentencesExtractor


def test_sentences_extractor(paragraph: Paragraph):
    sentences_extractor = SentencesExtractor(paragraph=paragraph)

    sentences_extractor()

    assert paragraph.sentences == Sentences(
        collection=[
            Sentence(
                content="What are you doing?",
                spans=Spans(),
            ),
            Span(
                content=" ",
                subcategory=SpanSubcategory.WHITESPACE,
            ),
            Sentence(
                content="Move it!",
                spans=Spans(),
            ),
        ],
        count=2,
    )
