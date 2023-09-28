import pytest

from editor.apps.spellchecker.entities import (
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
from editor.apps.spellchecker.processors import DocumentLoader


@pytest.fixture
def tree(document: HttpDocument) -> Tree:
    return Tree(
        document=document,
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
                                        ),
                                    ],
                                    count=2,
                                ),
                                category="sentence",
                                length=SentenceLength.UNKNOWN,
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
                        text="Appple",
                        marks=[
                            HttpMark(
                                type=HttpMarkType.SPELLCHECK,
                                attrs=HttpMarkAttrs(value=["Apple", "Supple", "Nipple"]),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text=".",
                    ),
                ],
            ),
        ],
        type="doc",
    )
