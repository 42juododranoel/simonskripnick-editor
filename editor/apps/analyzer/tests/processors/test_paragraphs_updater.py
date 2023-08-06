from editor.apps.analyzer.entities import (
    Paragraph,
    ParagraphCollection,
    SentenceCollection,
    Text,
)
from editor.apps.analyzer.processors import ParagraphsUpdater


def test_paragraphs_updater(text: Text):
    paragraphs_updater = ParagraphsUpdater(text=text)

    paragraphs_updater()

    assert text.paragraphs == ParagraphCollection(
        collection=[
            Paragraph(
                index=0,
                content="What are you doing? Move it!",
                sentences=SentenceCollection(),
            ),
            Paragraph(
                index=1,
                content="The horn calls — we shall answer.",
                sentences=SentenceCollection(),
            ),
        ],
        count=2,
    )
