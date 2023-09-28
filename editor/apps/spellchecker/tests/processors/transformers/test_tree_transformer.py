from editor.apps.spellchecker.entities import (
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
from editor.apps.spellchecker.processors import TreeTransformer


def test_tree_transformer(document: HttpDocument):
    tree = Tree(
        document=document,
        context=Context(
            paragraph_count=1,
            sentence_count=1,
            word_count=1,
            sentence_lengths=[1],
            length_centroids={},
        ),
        paragraphs=Paragraphs(
            count=1,
            collection=[
                Paragraph(
                    content="Appple.",
                    sentences=Sentences(
                        count=1,
                        collection=[
                            Sentence(
                                content="Appple.",
                                spans=Spans(
                                    count=2,
                                    collection=[
                                        Span(subcategory=SpanSubcategory.WORD, content="Appple"),
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
                    content=[HttpText(type="text", text="What are you doing? Move it!")],
                ),
                HttpParagraph(
                    type="paragraph",
                    content=[HttpText(type="text", text="The horn calls — we shall answer.")],
                ),
            ],
        ),
        context=Context(
            paragraph_count=1,
            sentence_count=1,
            word_count=1,
            sentence_lengths=[1],
            length_centroids={},
        ),
        paragraphs=Paragraphs(
            collection=[
                Paragraph(
                    content="Appple.",
                    sentences=Sentences(
                        collection=[
                            Sentence(
                                content="Appple.",
                                spans=Spans(
                                    collection=[
                                        Span(
                                            content="Appple",
                                            subcategory=SpanSubcategory.WORD,
                                            category="span",
                                            fatigue=0,
                                            spellcheck_candidates=[
                                                ("Apple", 0.4583333333333333),
                                                ("Supple", 0.2916666666666667),
                                                ("Nipple", 0.25),
                                            ],
                                        ),
                                        Span(
                                            content=".",
                                            subcategory=SpanSubcategory.WORD,
                                            category="span",
                                            fatigue=0,
                                            spellcheck_candidates=[],
                                        ),
                                    ],
                                    count=2,
                                ),
                                category="sentence",
                                length=SentenceLength.UNKNOWN,
                                length_repeat_count=0,
                                fatigue=0,
                            ),
                        ],
                        count=1,
                    ),
                    category="paragraph",
                ),
            ],
            count=1,
        ),
        category="text",
    )
