from editor.apps.analyzer.entities import (
    Context,
    HttpDocument,
    Paragraph,
    Paragraphs,
    Sentence,
    Sentences,
    Span,
    Spans,
    SpanSubcategory,
    Tree,
)
from editor.apps.analyzer.processors import TreeExtractor


def test_tree_extractor(document: HttpDocument):
    tree_extractor = TreeExtractor(document=document)

    tree = tree_extractor()

    assert tree == Tree(
        document=document,
        context=Context(
            paragraph_count=2,
            sentence_count=3,
            word_count=16,
            sentence_lengths=[5, 3, 8],
        ),
        paragraphs=Paragraphs(
            count=2,
            collection=[
                Paragraph(
                    content="What are you doing? Move it!",
                    sentences=Sentences(
                        count=2,
                        collection=[
                            Sentence(
                                content="What are you doing?",
                                spans=Spans(
                                    count=5,
                                    collection=[
                                        Span(subcategory=SpanSubcategory.WORD, content="What"),
                                        Span(subcategory=SpanSubcategory.WHITESPACE, content=" "),
                                        Span(subcategory=SpanSubcategory.WORD, content="are"),
                                        Span(subcategory=SpanSubcategory.WHITESPACE, content=" "),
                                        Span(subcategory=SpanSubcategory.WORD, content="you"),
                                        Span(subcategory=SpanSubcategory.WHITESPACE, content=" "),
                                        Span(subcategory=SpanSubcategory.WORD, content="doing"),
                                        Span(subcategory=SpanSubcategory.WORD, content="?"),
                                    ],
                                ),
                            ),
                            Span(subcategory=SpanSubcategory.WHITESPACE, content=" "),
                            Sentence(
                                content="Move it!",
                                spans=Spans(
                                    count=3,
                                    collection=[
                                        Span(subcategory=SpanSubcategory.WORD, content="Move"),
                                        Span(subcategory=SpanSubcategory.WHITESPACE, content=" "),
                                        Span(subcategory=SpanSubcategory.WORD, content="it"),
                                        Span(subcategory=SpanSubcategory.WORD, content="!"),
                                    ],
                                ),
                            ),
                        ],
                    ),
                ),
                Paragraph(
                    content="The horn calls — we shall answer.",
                    sentences=Sentences(
                        count=1,
                        collection=[
                            Sentence(
                                content="The horn calls — we shall answer.",
                                spans=Spans(
                                    count=8,
                                    collection=[
                                        Span(subcategory=SpanSubcategory.WORD, content="The"),
                                        Span(subcategory=SpanSubcategory.WHITESPACE, content=" "),
                                        Span(subcategory=SpanSubcategory.WORD, content="horn"),
                                        Span(subcategory=SpanSubcategory.WHITESPACE, content=" "),
                                        Span(subcategory=SpanSubcategory.WORD, content="calls"),
                                        Span(subcategory=SpanSubcategory.WHITESPACE, content=" "),
                                        Span(subcategory=SpanSubcategory.WORD, content="—"),
                                        Span(subcategory=SpanSubcategory.WHITESPACE, content=" "),
                                        Span(subcategory=SpanSubcategory.WORD, content="we"),
                                        Span(subcategory=SpanSubcategory.WHITESPACE, content=" "),
                                        Span(subcategory=SpanSubcategory.WORD, content="shall"),
                                        Span(subcategory=SpanSubcategory.WHITESPACE, content=" "),
                                        Span(subcategory=SpanSubcategory.WORD, content="answer"),
                                        Span(subcategory=SpanSubcategory.WORD, content="."),
                                    ],
                                ),
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )
