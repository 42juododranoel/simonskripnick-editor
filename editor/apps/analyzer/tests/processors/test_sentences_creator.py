from editor.apps.analyzer.entities import (
    Paragraph,
    Sentence,
    Sentences,
    Span,
    Spans,
    SpanSubcategory,
)
from editor.apps.analyzer.processors import SentencesCreator


def test_sentences_creator(paragraph: Paragraph):
    sentences_creator = SentencesCreator(paragraph=paragraph)

    sentences_creator()

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
