from math import ceil
from statistics import mean

from editor.apps.analyzer.entities import (
    Context,
    Paragraph,
    ParagraphCollection,
    Sentence,
    Text,
)
from editor.apps.analyzer.processors.paragraphs_updater import ParagraphsUpdater
from editor.apps.analyzer.processors.sentences_updater import SentencesUpdater
from editor.apps.analyzer.processors.tokens_updater import TokensUpdater
from editor.base.processors import BaseProcessor


class ContentAnalyzer(BaseProcessor):
    """Analyze string of text and return it as a nested structure."""

    def __init__(self, content: str) -> None:
        self.content = content
        self.context = Context()

        self.sentence_lengths = []

    def run(self) -> Text:
        text = self.get_text()

        mean_sentence_length = ceil(mean(self.sentence_lengths))
        half_mean_length = mean_sentence_length / 2

        self.context.short_sentence_length = ceil(mean_sentence_length - half_mean_length)
        self.context.medium_sentence_length = ceil(mean_sentence_length + half_mean_length)
        self.context.mean_sentence_length = mean_sentence_length

        return text

    def get_text(self) -> Text:
        text = Text(content=self.content, paragraphs=ParagraphCollection(), context=self.context)
        self.update_paragraphs(text)

        for paragraph in text.paragraphs.collection:
            self.update_sentences(paragraph)
            self.context.paragraph_count += 1

            for sentence in paragraph.sentences.collection:
                self.update_tokens(sentence)
                self.context.sentence_count += 1

                self.context.token_count += sentence.tokens.count
                self.sentence_lengths.append(sentence.tokens.count)

        return text

    def update_paragraphs(self, text: Text) -> None:
        paragraphs_updater = ParagraphsUpdater(text, self.context)
        paragraphs_updater()

    def update_sentences(self, paragraph: Paragraph) -> None:
        sentences_updater = SentencesUpdater(paragraph, self.context)
        sentences_updater()

    def update_tokens(self, sentence: Sentence) -> None:
        tokens_updater = TokensUpdater(sentence, self.context)
        tokens_updater()
