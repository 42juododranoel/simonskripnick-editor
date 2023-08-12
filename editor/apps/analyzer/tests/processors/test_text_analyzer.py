from editor.apps.analyzer.entities import (
    Context,
    Paragraph,
    Paragraphs,
    Sentence,
    SentenceLength,
    Sentences,
    Span,
    Spans,
    SpanSubcategory,
    Text,
)
from editor.apps.analyzer.processors import TextAnalyzer


def test_text_analyzer():
    text = Text(
        content="What are you doing? Move it!\r\nThe horn calls — we shall answer.",
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
    text_analyzer = TextAnalyzer(text=text)

    text_analyzer()

    assert text == Text(
        content="What are you doing? Move it!\r\nThe horn calls — we shall answer.",
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
                    content="What are you doing? Move it!",
                    sentences=Sentences(
                        collection=[
                            Sentence(
                                content="What are you doing?",
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
                                            content="are",
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
                                length_percentage=8,
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
                                length_percentage=5,
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
                                length_percentage=12,
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
