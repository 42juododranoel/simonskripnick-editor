from enum import StrEnum

from pydantic import BaseModel


class HttpMarkType(StrEnum):
    """A mark can be either length or fatigue."""

    LENGTH = "length"
    FATIGUE = "fatigue"


class HttpMarkAttrs(BaseModel):
    """Mark attributes store numeric or char value for mark."""

    value: int | str


class HttpMark(BaseModel):
    """A mark denotes the calculated level of fatigue and length."""

    type: HttpMarkType  # noqa: A003
    attrs: HttpMarkAttrs


class HttpText(BaseModel):
    """A text is a smallest possible node of document, containing plain text."""

    type: str = "text"  # noqa: A003
    text: str
    marks: list[HttpMark] = []


class HttpParagraph(BaseModel):
    """A paragraph contains multiple nodes of text."""

    type: str = "paragraph"  # noqa: A003
    content: list[HttpText] = []


class HttpDocument(BaseModel):
    """A document contains multiple nodes of paragraph."""

    type: str = "doc"  # noqa: A003
    content: list[HttpParagraph] = []
