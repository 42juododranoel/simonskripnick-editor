import pytest

from editor.apps.analyzer.entities import (
    Context,
    HttpDocument,
    HttpParagraph,
    HttpText,
    Paragraph,
    Paragraphs,
    Sentence,
    Sentences,
    Spans,
    Tree,
)


@pytest.fixture
def document() -> HttpDocument:
    return HttpDocument(
        type="doc",
        content=[
            HttpParagraph(
                type="paragraph",
                content=[
                    HttpText(type="text", text="What arw you doing? Move it!"),
                ],
            ),
            HttpParagraph(
                type="paragraph",
                content=[
                    HttpText(type="text", text="The horn calls — we shall answer."),
                ],
            ),
        ],
    )


@pytest.fixture
def tree(document: HttpDocument) -> Tree:
    return Tree(
        document=document,
        paragraphs=Paragraphs(),
        context=Context(sentence_lengths=[1, 2, 3]),
    )


@pytest.fixture
def paragraph() -> Paragraph:
    return Paragraph(
        content="What arw you doing? Move it!",
        sentences=Sentences(),
    )


@pytest.fixture
def sentence() -> Sentence:
    return Sentence(
        content="What arw you doing?",
        spans=Spans(),
    )
