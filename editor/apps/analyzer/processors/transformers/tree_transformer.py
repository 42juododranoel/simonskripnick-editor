from math import ceil

import kmeans1d

from editor.apps.analyzer.entities import Sentence, SentenceLength, Tree
from editor.apps.analyzer.processors.transformers.spans_transformer import (
    SpansTransformer,
)
from editor.base.processors import BaseProcessor

CENTROID_LENGTHS = {
    0: SentenceLength.SHORT,
    1: SentenceLength.MEDIUM,
    2: SentenceLength.LONG,
}


class TreeTransformer(BaseProcessor):
    """Analyze a tree."""

    def __init__(self, tree: Tree) -> None:
        self.tree = tree
        self.context = self.tree.context
        self.lengths = {}
        self.longest_sentence_length = 0

    def run(self) -> Tree:
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
        for paragraph in self.tree.paragraphs.collection:
            previous_sentence_length = ""

            sentences = filter(
                lambda item: isinstance(item, Sentence),
                paragraph.sentences.collection,
            )
            for sentence in sentences:
                sentence.length = self.lengths[sentence.spans.count]
                sentence.length_percentage = ceil(
                    (sentence.spans.count / self.longest_sentence_length) * 10,
                )
                if sentence.length == previous_sentence_length:
                    sentence.length_repeat_count += 1
                previous_sentence_length = sentence.length

                self.analyze_spans(sentence)

    def analyze_spans(self, sentence: Sentence) -> None:
        sentence_centroid = self.context.length_centroids[sentence.length]
        spans_transformer = SpansTransformer(
            sentence.spans,
            sentence.length,
            sentence_centroid,
            sentence.length_repeat_count,
        )
        spans_transformer()
