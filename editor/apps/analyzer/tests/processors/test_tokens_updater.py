from editor.apps.analyzer.entities import Sentence, Token, TokenCollection
from editor.apps.analyzer.processors import TokensUpdater


def test_tokens_updater(sentence: Sentence):
    tokens_updater = TokensUpdater(sentence=sentence)

    tokens_updater()

    assert sentence.tokens == TokenCollection(
        collection=[
            Token(content="What", index=0),
            Token(content="are", index=1),
            Token(content="you", index=2),
            Token(content="doing", index=3),
            Token(content="?", index=4),
        ],
        count=5,
    )
