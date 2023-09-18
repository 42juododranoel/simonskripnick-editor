from editor.apps.analyzer.entities import (
    HttpDocument,
    HttpMark,
    HttpMarkAttrs,
    HttpMarkType,
    HttpParagraph,
    HttpText,
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
                        text="What is it? Move it! Good.",
                        marks=[
                            HttpMark(type=HttpMarkType.LENGTH, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                        ],
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
                        text="What",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(type=HttpMarkType.LENGTH, attrs=HttpMarkAttrs(value=10)),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text=" ",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(type=HttpMarkType.LENGTH, attrs=HttpMarkAttrs(value=10)),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text="is",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(type=HttpMarkType.LENGTH, attrs=HttpMarkAttrs(value=10)),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text=" ",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(type=HttpMarkType.LENGTH, attrs=HttpMarkAttrs(value=10)),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text="it",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(type=HttpMarkType.LENGTH, attrs=HttpMarkAttrs(value=10)),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text="?",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(type=HttpMarkType.LENGTH, attrs=HttpMarkAttrs(value=10)),
                        ],
                    ),
                    HttpText(type="text", text=" ", marks=[]),
                    HttpText(
                        type="text",
                        text="Move",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(type=HttpMarkType.LENGTH, attrs=HttpMarkAttrs(value=8)),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text=" ",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(type=HttpMarkType.LENGTH, attrs=HttpMarkAttrs(value=8)),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text="it",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(type=HttpMarkType.LENGTH, attrs=HttpMarkAttrs(value=8)),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text="!",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(type=HttpMarkType.LENGTH, attrs=HttpMarkAttrs(value=8)),
                        ],
                    ),
                    HttpText(type="text", text=" ", marks=[]),
                    HttpText(
                        type="text",
                        text="Good",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(type=HttpMarkType.LENGTH, attrs=HttpMarkAttrs(value=5)),
                        ],
                    ),
                    HttpText(
                        type="text",
                        text=".",
                        marks=[
                            HttpMark(type=HttpMarkType.FATIGUE, attrs=HttpMarkAttrs(value=0)),
                            HttpMark(type=HttpMarkType.LENGTH, attrs=HttpMarkAttrs(value=5)),
                        ],
                    ),
                ],
            )
        ],
    )
