from fastapi import APIRouter

from editor.apps.analyzer.entities import HttpDocument
from editor.apps.analyzer.processors import PipelineRunner

router = APIRouter()


@router.post("/analyze-document")
async def analyze_document(document: HttpDocument) -> dict:
    """Analyze document fatigue and length."""

    pipeline_runner = PipelineRunner(document=document)
    updated_document = pipeline_runner()

    return updated_document.dict()
