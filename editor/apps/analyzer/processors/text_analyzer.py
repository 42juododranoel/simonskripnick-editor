from math import ceil

import kmeans1d

from editor.apps.analyzer.entities import Sentence, SentenceLength, Text
from editor.apps.analyzer.processors.spans_analyzer import SpansAnalyzer
from editor.base.processors import BaseProcessor

CENTROID_LENGTHS = {
    0: SentenceLength.SHORT,
    1: SentenceLength.MEDIUM,
    2: SentenceLength.LONG,
}


class TextAnalyzer(BaseProcessor):
    """Analyze a text."""

    def __init__(self, text: Text) -> None:
        self.text = text
        self.context = self.text.context
        self.lengths = {}
        self.longest_sentence_length = 0

    def run(self) -> Text:
        self.analyze_length()
        self.analyze_paragraphs()

    def analyze_length(self) -> None:
        clusters, centroids = kmeans1d.cluster(self.context.sentence_lengths, 3)
        for sentence_index, centroid_index in enumerate(clusters):
            sentence_length = self.context.sentence_lengths[sentence_index]
            self.lengths[sentence_length] = CENTROID_LENGTHS[centroid_index]

        sentence_lengths = sorted(self.context.sentence_lengths)
        self.longest_sentence_length = sentence_lengths[-1]

        self.context.length_centroids = {
            SentenceLength.SHORT: ceil(centroids[0]),
            SentenceLength.MEDIUM: ceil(centroids[1]),
            SentenceLength.LONG: ceil(centroids[2]),
        }

    def analyze_paragraphs(self) -> None:
        for paragraph in self.text.paragraphs.collection:
            previous_sentence_length = ""

            sentences = filter(
                lambda item: isinstance(item, Sentence),
                paragraph.sentences.collection,
            )
            for sentence in sentences:
                sentence.length = self.lengths[sentence.spans.count]
                sentence.length_percentage = ceil(
                    (sentence.spans.count / self.longest_sentence_length) * 12,
                )
                if sentence.length == previous_sentence_length:
                    sentence.length_repeat_count += 1
                previous_sentence_length = sentence.length

                self.analyze_spans(sentence)

    def analyze_spans(self, sentence: Sentence) -> None:
        sentence_centroid = self.context.length_centroids[sentence.length]
        spans_analyzer = SpansAnalyzer(
            sentence.spans,
            sentence.length,
            sentence_centroid,
            sentence.length_repeat_count,
        )
        spans_analyzer()
