from enum import StrEnum

import attrs


class SentenceLength(StrEnum):
    """A sentence length can be short, medium, or long."""

    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"
    UNKNOWN = "unknown"

    @property
    def centroid_fatigue(self) -> int:
        return {
            self.SHORT: 2,
            self.MEDIUM: 4,
            self.LONG: 4,
        }[self.value]

    @property
    def repetition_fatigue(self) -> int:
        return {
            self.SHORT: 4,
            self.MEDIUM: 8,
            self.LONG: 12,
        }[self.value]


class SpanSubcategory(StrEnum):
    """A span can represent a word or a whitespace."""

    WORD = "word"
    WHITESPACE = "whitespace"


@attrs.define
class Context:
    """A context represents some important info on user-provided text."""

    paragraph_count: int = 0
    sentence_count: int = 0
    word_count: int = 0
    sentence_lengths: list[int] = []
    length_centroids: dict[SentenceLength, int] = {}


@attrs.define
class Span:
    """A span is a word or a punctuation mark."""

    content: str
    subcategory: SpanSubcategory

    category: str = "span"
    fatigue: int = 0


@attrs.define
class Spans:
    """Use span collection when working with multiple spans."""

    collection: list[Span] = []
    count: int = 0


@attrs.define
class Sentence:
    """A sentence is a collection of spans."""

    content: str
    spans: Spans

    category: str = "sentence"
    length: SentenceLength = SentenceLength.UNKNOWN
    length_percentage: int = 0
    length_repeat_count: int = 0
    fatigue: int = 0


@attrs.define
class Sentences:
    """Use sentence collection when working with multiple sentences."""

    collection: list[Sentence | Span] = []
    count: int = 0


@attrs.define
class Paragraph:
    """A paragraph is a collection of sentences."""

    content: str
    sentences: Sentences

    category: str = "paragraph"


@attrs.define
class Paragraphs:
    """Use paragraph collection when working with multiple paragraphs."""

    collection: list[Paragraph] = []
    count: int = 0


@attrs.define
class Text:
    """A text is a collection of paragraphs."""

    content: str
    context: Context
    paragraphs: Paragraphs

    category: str = "text"
