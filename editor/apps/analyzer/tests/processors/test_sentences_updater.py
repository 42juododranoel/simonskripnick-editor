from editor.apps.analyzer.entities import (
    Paragraph,
    Sentence,
    SentenceCollection,
    TokenCollection,
)
from editor.apps.analyzer.processors import SentencesUpdater


def test_sentences_updater(paragraph: Paragraph):
    sentences_updater = SentencesUpdater(paragraph=paragraph)

    sentences_updater()

    assert paragraph.sentences == SentenceCollection(
        collection=[
            Sentence(
                index=0,
                content="What are you doing?",
                tokens=TokenCollection(),
            ),
            Sentence(
                index=1,
                content="Move it!",
                tokens=TokenCollection(),
            ),
        ],
        count=2,
    )
