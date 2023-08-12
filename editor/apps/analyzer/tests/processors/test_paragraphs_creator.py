from editor.apps.analyzer.entities import Paragraph, Paragraphs, Sentences, Text
from editor.apps.analyzer.processors import ParagraphsCreator


def test_paragraphs_creator(text: Text):
    paragraphs_creator = ParagraphsCreator(text=text)

    paragraphs_creator()

    assert text.paragraphs == Paragraphs(
        collection=[
            Paragraph(
                content="What are you doing? Move it!",
                sentences=Sentences(),
            ),
            Paragraph(
                content="The horn calls — we shall answer.",
                sentences=Sentences(),
            ),
        ],
        count=2,
    )
