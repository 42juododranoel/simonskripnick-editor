from editor.apps.analyzer.entities import SentenceLength, Spans, SpanSubcategory
from editor.base.processors import BaseProcessor


class SpansAnalyzer(BaseProcessor):
    """Analyze a token collection."""

    def __init__(
        self,
        spans: Spans,
        sentence_length: SentenceLength,
        sentence_centroid: int,
        repeated_sentence_length_count: int,
    ) -> None:
        self.spans = spans
        self.sentence_length = sentence_length
        self.sentence_centroid = sentence_centroid
        self.repeated_sentence_length_count = repeated_sentence_length_count

        self.word_index = 0
        self.accumulated_fatigue = (
            self.sentence_length.repetition_fatigue * repeated_sentence_length_count
        )
        self.previous_word_fatigue = 0

    def run(self) -> None:
        for span in self.spans.collection:
            if span.subcategory == SpanSubcategory.WORD:
                self.word_index += 1

                span.fatigue = self.accumulated_fatigue
                if self.word_index > self.sentence_centroid:
                    span.fatigue = self.accumulated_fatigue * self.sentence_length.centroid_fatigue
                    self.accumulated_fatigue += 1

                self.previous_word_fatigue = span.fatigue
            else:
                span.fatigue = self.previous_word_fatigue
