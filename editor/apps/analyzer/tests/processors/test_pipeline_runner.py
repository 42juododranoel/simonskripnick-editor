from editor.apps.analyzer.entities import (
    HttpDocument,
    HttpMark,
    HttpMarkAttrs,
    HttpMarkType,
    HttpParagraph,
    HttpText,
    SentenceLength,
)
from editor.apps.analyzer.processors import PipelineRunner


def test_pipeline_runner():
    document = HttpDocument(
        type="doc",
        content=[
            HttpParagraph(
                type="paragraph",
                content=[
                    HttpText(
                        type="text",
                        text="What is it? Move it! Appple.",
                    ),
                ],
            ),
        ],
    )
    pipeline_runner = PipelineRunner(document=document)

    updated_document = pipeline_runner()
    http_paragraph = updated_document.content[0]
    http_text = http_paragraph.content[12]
    assert updated_document.type == "doc"
    assert http_paragraph.type == "paragraph"
    assert http_text.type == "text"
    assert http_text.text == "Appple"
    assert http_text.marks == [
        HttpMark(
            type=HttpMarkType.SPELLCHECK,
            attrs=HttpMarkAttrs(value=["Apple", "Supple", "Nipple"]),
        ),
        HttpMark(
            type=HttpMarkType.FATIGUE,
            attrs=HttpMarkAttrs(value=0),
        ),
        HttpMark(
            type=HttpMarkType.LENGTH,
            attrs=HttpMarkAttrs(value=SentenceLength.SHORT),
        ),
    ]
