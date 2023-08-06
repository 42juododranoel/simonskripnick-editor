import attrs


@attrs.define
class Context:
    """A context represents some important info on user-provided text."""

    paragraph_count: int = 0
    sentence_count: int = 0
    token_count: int = 0

    mean_sentence_length: int = 0

    short_sentence_length: int = 0
    medium_sentence_length: int = 0


@attrs.define
class Token:
    """A token is a word or a punctuation mark."""

    content: str
    index: int


@attrs.define
class TokenCollection:
    """Use token collection when working with multiple tokens."""

    collection: list[Token] = []
    count: int = 0


@attrs.define
class Sentence:
    """A sentence is a collection of tokens."""

    content: str
    tokens: TokenCollection
    index: int


@attrs.define
class SentenceCollection:
    """Use sentence collection when working with multiple sentences."""

    collection: list[Sentence] = []
    count: int = 0


@attrs.define
class Paragraph:
    """A paragraph is a collection of sentences."""

    content: str
    sentences: SentenceCollection
    index: int


@attrs.define
class ParagraphCollection:
    """Use paragraph collection when working with multiple paragraphs."""

    collection: list[Paragraph] = []
    count: int = 0


@attrs.define
class Text:
    """A text is a collection of paragraphs."""

    content: str
    context: Context
    paragraphs: ParagraphCollection
