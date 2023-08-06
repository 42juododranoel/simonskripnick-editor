import pytest

from editor.apps.analyzer.entities import (
    Context,
    Paragraph,
    ParagraphCollection,
    Sentence,
    SentenceCollection,
    Text,
    TokenCollection,
)


@pytest.fixture
def content() -> str:
    return "What are you doing? Move it!\r\nThe horn calls — we shall answer."


@pytest.fixture
def text(content: str) -> Text:
    return Text(content=content, paragraphs=ParagraphCollection(), context=Context())


@pytest.fixture
def paragraph() -> Paragraph:
    return Paragraph(
        index=0,
        content="What are you doing? Move it!",
        sentences=SentenceCollection(),
    )


@pytest.fixture
def sentence() -> Sentence:
    return Sentence(
        index=0,
        content="What are you doing?",
        tokens=TokenCollection(),
    )
