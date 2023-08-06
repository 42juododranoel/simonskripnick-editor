from editor.apps.analyzer.entities import (
    Context,
    Paragraph,
    ParagraphCollection,
    Sentence,
    SentenceCollection,
    Text,
    Token,
    TokenCollection,
)
from editor.apps.analyzer.processors import ContentAnalyzer


def test_content_analyzer(content: str):
    content_analyzer = ContentAnalyzer(content=content)

    text = content_analyzer()

    assert text == Text(
        content="What are you doing? Move it!\r\nThe horn calls — we shall answer.",
        context=Context(
            paragraph_count=2,
            sentence_count=3,
            token_count=16,
            mean_sentence_length=6,
            short_sentence_length=3,
            medium_sentence_length=9,
        ),
        paragraphs=ParagraphCollection(
            count=2,
            collection=[
                Paragraph(
                    index=0,
                    content="What are you doing? Move it!",
                    sentences=SentenceCollection(
                        count=2,
                        collection=[
                            Sentence(
                                index=0,
                                content="What are you doing?",
                                tokens=TokenCollection(
                                    count=5,
                                    collection=[
                                        Token(index=0, content="What"),
                                        Token(index=1, content="are"),
                                        Token(index=2, content="you"),
                                        Token(index=3, content="doing"),
                                        Token(index=4, content="?"),
                                    ],
                                ),
                            ),
                            Sentence(
                                index=1,
                                content="Move it!",
                                tokens=TokenCollection(
                                    count=3,
                                    collection=[
                                        Token(index=0, content="Move"),
                                        Token(index=1, content="it"),
                                        Token(index=2, content="!"),
                                    ],
                                ),
                            ),
                        ],
                    ),
                ),
                Paragraph(
                    index=1,
                    content="The horn calls — we shall answer.",
                    sentences=SentenceCollection(
                        count=1,
                        collection=[
                            Sentence(
                                index=0,
                                content="The horn calls — we shall answer.",
                                tokens=TokenCollection(
                                    count=8,
                                    collection=[
                                        Token(index=0, content="The"),
                                        Token(index=1, content="horn"),
                                        Token(index=2, content="calls"),
                                        Token(index=3, content="—"),
                                        Token(index=4, content="we"),
                                        Token(index=5, content="shall"),
                                        Token(index=6, content="answer"),
                                        Token(index=7, content="."),
                                    ],
                                ),
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )
