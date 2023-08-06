import nltk

from editor.apps.analyzer.entities import Context, Sentence, Token
from editor.base.processors import BaseProcessor


class TokensUpdater(BaseProcessor):
    """Update a token collection from given sentence."""

    def __init__(self, sentence: Sentence, context: Context | None = None) -> None:
        self.sentence = sentence
        self.context = context

    def run(self) -> dict:
        words = nltk.word_tokenize(self.sentence.content)
        self.sentence.tokens.collection = [
            self.create_token(content, index) for index, content in enumerate(words)
        ]
        self.sentence.tokens.count = len(self.sentence.tokens.collection)

    def create_token(self, content: str, index: int) -> Token:
        return Token(
            index=index,
            content=content,
        )
