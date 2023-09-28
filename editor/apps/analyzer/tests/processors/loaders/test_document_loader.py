import pytest

from editor.apps.analyzer.entities import (
    Context,
    HttpDocument,
    HttpMark,
    HttpMarkAttrs,
    HttpMarkType,
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
from editor.apps.analyzer.processors import DocumentLoader


@pytest.fixture
def tree(document: HttpDocument) -> Tree:
    return Tree(
        document=document,
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


def test_document_loader(tree: Tree):
    document_loader = DocumentLoader(tree=tree)

    document = document_loader()

    assert document == HttpDocument(
        content=[
            HttpParagraph(
                type="paragraph",
                content=[
                    HttpText(
                        type="text",
                        text="What",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.MEDIUM),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text=" ",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.MEDIUM),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text="arw",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.MEDIUM),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text=" ",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.MEDIUM),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text="you",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.MEDIUM),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text=" ",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.MEDIUM),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text="doing",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.MEDIUM),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text="?",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.MEDIUM),
                            ),
                        ],
                    ),
                    HttpText(type="text", text=" ", marks=[]),
                    HttpText(
                        type="text",
                        text="Move",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.SHORT),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text=" ",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.SHORT),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text="it",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.SHORT),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text="!",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.SHORT),
                            ),
                        ],
                    ),
                ],
            ),
            HttpParagraph(
                type="paragraph",
                content=[
                    HttpText(
                        type="text",
                        text="The",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.LONG),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text=" ",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.LONG),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text="horn",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.LONG),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text=" ",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.LONG),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text="calls",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.LONG),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text=" ",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.LONG),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text="—",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.LONG),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text=" ",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.LONG),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text="we",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.LONG),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text=" ",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.LONG),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text="shall",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.LONG),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text=" ",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.LONG),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text="answer",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.LONG),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text=".",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(
                                type=HttpMarkType.LENGTH,
                                attrs=HttpMarkAttrs(value=SentenceLength.LONG),
                            ),
                        ],
                    ),
                ],
            ),
        ],
        type="doc",
    )
