import pytest

from editor.apps.analyzer.entities import (
    Context,
    Paragraph,
    Paragraphs,
    Sentence,
    Sentences,
    Spans,
    Text,
)


@pytest.fixture
def content() -> str:
    return "What are you doing? Move it!\r\nThe horn calls — we shall answer."


@pytest.fixture
def text(content: str) -> Text:
    return Text(
        content=content,
        paragraphs=Paragraphs(),
        context=Context(sentence_lengths=[1, 2, 3]),
    )


@pytest.fixture
def paragraph() -> Paragraph:
    return Paragraph(
        content="What are you doing? Move it!",
        sentences=Sentences(),
    )


@pytest.fixture
def sentence() -> Sentence:
    return Sentence(
        content="What are you doing?",
        spans=Spans(),
    )
