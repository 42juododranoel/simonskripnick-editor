from editor.apps.analyzer.entities import Paragraph, Paragraphs, Sentences, Tree
from editor.apps.analyzer.processors import ParagraphsExtractor


def test_paragraphs_extractor(tree: Tree):
    paragraphs_extractor = ParagraphsExtractor(tree=tree)

    paragraphs_extractor()

    assert tree.paragraphs == Paragraphs(
        collection=[
            Paragraph(
                content="What arw you doing? Move it!",
                sentences=Sentences(),
            ),
            Paragraph(
                content="The horn calls — we shall answer.",
                sentences=Sentences(),
            ),
        ],
        count=2,
    )
