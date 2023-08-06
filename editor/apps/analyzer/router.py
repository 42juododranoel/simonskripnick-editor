import attrs
from fastapi import APIRouter
from pydantic import BaseModel

from editor.apps.analyzer.processors import ContentAnalyzer

router = APIRouter()


class AnalyzeTextPayload(BaseModel):
    """User sends this payload when wants their text analyzed."""

    content: str


@router.post("/analyze-content")
async def analyze_content(payload: AnalyzeTextPayload) -> dict:
    """Return test message."""

    content_analyzer = ContentAnalyzer(content=payload.content)
    tree = content_analyzer()

    return attrs.asdict(tree)
