from editor.apps.analyzer.entities import (
    Context,
    HttpDocument,
    HttpParagraph,
    HttpText,
    Paragraph,
    Paragraphs,
    Sentence,
    SentenceLength,
    Sentences,
    Span,
    Spans,
    SpanSubcategory,
    Tree,
)
from editor.apps.analyzer.processors import TreeTransformer


def test_tree_transformer(document: HttpDocument):
    tree = Tree(
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
                    content="What arw you doing? Move it!",
                    sentences=Sentences(
                        count=2,
                        collection=[
                            Sentence(
                                content="What arw you doing?",
                                spans=Spans(
                                    count=5,
                                    collection=[
                                        Span(subcategory=SpanSubcategory.WORD, content="What"),
                                        Span(subcategory=SpanSubcategory.WHITESPACE, content=" "),
                                        Span(subcategory=SpanSubcategory.WORD, content="arw"),
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
    tree_transformer = TreeTransformer(tree=tree)

    tree_transformer()

    assert tree == Tree(
        document=HttpDocument(
            type="doc",
            content=[
                HttpParagraph(
                    type="paragraph",
                    content=[HttpText(type="text", text="What arw you doing? Move it!", marks=[])],
                ),
                HttpParagraph(
                    type="paragraph",
                    content=[
                        HttpText(type="text", text="The horn calls — we shall answer.", marks=[]),
                    ],
                ),
            ],
        ),
        context=Context(
            paragraph_count=2,
            sentence_count=3,
            word_count=16,
            sentence_lengths=[5, 3, 8],
            length_centroids={
                SentenceLength.SHORT: 3,
                SentenceLength.MEDIUM: 5,
                SentenceLength.LONG: 8,
            },
        ),
        paragraphs=Paragraphs(
            collection=[
                Paragraph(
                    content="What arw you doing? Move it!",
                    sentences=Sentences(
                        collection=[
                            Sentence(
                                content="What arw you doing?",
                                spans=Spans(
                                    collection=[
                                        Span(
                                            content="What",
                                            subcategory=SpanSubcategory.WORD,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content=" ",
                                            subcategory=SpanSubcategory.WHITESPACE,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content="arw",
                                            subcategory=SpanSubcategory.WORD,
                                            category="span",
                                            fatigue=0,
                                            spellcheck_candidates=[
                                                ("are", 0.9065934065934066),
                                                ("arm", 0.06543456543456544),
                                                ("raw", 0.014485514485514486),
                                                ("art", 0.011738261738261738),
                                                ("arc", 0.0012487512487512488),
                                            ],
                                        ),
                                        Span(
                                            content=" ",
                                            subcategory=SpanSubcategory.WHITESPACE,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content="you",
                                            subcategory=SpanSubcategory.WORD,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content=" ",
                                            subcategory=SpanSubcategory.WHITESPACE,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content="doing",
                                            subcategory=SpanSubcategory.WORD,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content="?",
                                            subcategory=SpanSubcategory.WORD,
                                            category="span",
                                            fatigue=0,
                                        ),
                                    ],
                                    count=5,
                                ),
                                category="sentence",
                                length=SentenceLength.MEDIUM,
                                length_percentage=7,
                                length_repeat_count=0,
                                fatigue=0,
                            ),
                            Span(
                                content=" ",
                                subcategory=SpanSubcategory.WHITESPACE,
                                category="span",
                                fatigue=0,
                            ),
                            Sentence(
                                content="Move it!",
                                spans=Spans(
                                    collection=[
                                        Span(
                                            content="Move",
                                            subcategory=SpanSubcategory.WORD,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content=" ",
                                            subcategory=SpanSubcategory.WHITESPACE,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content="it",
                                            subcategory=SpanSubcategory.WORD,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content="!",
                                            subcategory=SpanSubcategory.WORD,
                                            category="span",
                                            fatigue=0,
                                        ),
                                    ],
                                    count=3,
                                ),
                                category="sentence",
                                length=SentenceLength.SHORT,
                                length_percentage=4,
                                length_repeat_count=0,
                                fatigue=0,
                            ),
                        ],
                        count=2,
                    ),
                    category="paragraph",
                ),
                Paragraph(
                    content="The horn calls — we shall answer.",
                    sentences=Sentences(
                        collection=[
                            Sentence(
                                content="The horn calls — we shall answer.",
                                spans=Spans(
                                    collection=[
                                        Span(
                                            content="The",
                                            subcategory=SpanSubcategory.WORD,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content=" ",
                                            subcategory=SpanSubcategory.WHITESPACE,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content="horn",
                                            subcategory=SpanSubcategory.WORD,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content=" ",
                                            subcategory=SpanSubcategory.WHITESPACE,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content="calls",
                                            subcategory=SpanSubcategory.WORD,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content=" ",
                                            subcategory=SpanSubcategory.WHITESPACE,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content="—",
                                            subcategory=SpanSubcategory.WORD,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content=" ",
                                            subcategory=SpanSubcategory.WHITESPACE,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content="we",
                                            subcategory=SpanSubcategory.WORD,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content=" ",
                                            subcategory=SpanSubcategory.WHITESPACE,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content="shall",
                                            subcategory=SpanSubcategory.WORD,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content=" ",
                                            subcategory=SpanSubcategory.WHITESPACE,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content="answer",
                                            subcategory=SpanSubcategory.WORD,
                                            category="span",
                                            fatigue=0,
                                        ),
                                        Span(
                                            content=".",
                                            subcategory=SpanSubcategory.WORD,
                                            category="span",
                                            fatigue=0,
                                        ),
                                    ],
                                    count=8,
                                ),
                                category="sentence",
                                length=SentenceLength.LONG,
                                length_percentage=10,
                                length_repeat_count=0,
                                fatigue=0,
                            ),
                        ],
                        count=1,
                    ),
                    category="paragraph",
                ),
            ],
            count=2,
        ),
        category="text",
    )
