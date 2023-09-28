from editor.apps.spellchecker.entities import (
    HttpDocument,
    HttpMark,
    HttpMarkAttrs,
    HttpMarkType,
    HttpParagraph,
    HttpText,
)
from editor.apps.spellchecker.processors import PipelineRunner


def test_pipeline_runner():
    document = HttpDocument(
        type="doc",
        content=[
            HttpParagraph(
                type="paragraph",
                content=[
                    HttpText(
                        type="text",
                        text="Appple.",
                    ),
                ],
            ),
        ],
    )
    pipeline_runner = PipelineRunner(document=document)

    updated_document = pipeline_runner()

    assert updated_document == HttpDocument(
        type="doc",
        content=[
            HttpParagraph(
                type="paragraph",
                content=[
                    HttpText(
                        type="text",
                        text="Appple",
                        marks=[
                            HttpMark(
                                type=HttpMarkType.SPELLCHECK,
                                attrs=HttpMarkAttrs(value=["Apple", "Supple", "Nipple"]),
                            ),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text=".",
                    ),
                ],
            ),
        ],
    )
