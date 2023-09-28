from fastapi import APIRouter

from editor.apps.spellchecker.entities import HttpDocument
from editor.apps.spellchecker.processors import PipelineRunner

router = APIRouter()


@router.post("/spellcheck-document")
async def spellcheck_document(document: HttpDocument) -> dict:
    """Spellcheck document fatigue and length."""

    pipeline_runner = PipelineRunner(document=document)
    updated_document = pipeline_runner()

    return updated_document.dict()
