import attrs
from fastapi import APIRouter
from pydantic import BaseModel

from editor.apps.analyzer.processors import TextAnalyzer, TextCreator

router = APIRouter()


class AnalyzeTextPayload(BaseModel):
    """User sends this payload when wants their text analyzed."""

    content: str


@router.post("/analyze-content")
async def analyze_content(payload: AnalyzeTextPayload) -> dict:
    """Return analyze content ant return it as nested data structure."""

    text_creator = TextCreator(content=payload.content)
    text = text_creator()

    text_analyzer = TextAnalyzer(text=text)
    text_analyzer()

    return attrs.asdict(text)
