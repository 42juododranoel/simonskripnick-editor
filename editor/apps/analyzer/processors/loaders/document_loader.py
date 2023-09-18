from editor.apps.analyzer.entities import (
    HttpDocument,
    HttpMark,
    HttpMarkAttrs,
    HttpParagraph,
    HttpText,
    Sentence,
    Span,
    Tree,
)
from editor.base.processors import BaseProcessor


class DocumentLoader(BaseProcessor):
    """Create a document from tree."""

    def __init__(self, tree: Tree) -> None:
        self.tree = tree

    def run(self) -> HttpDocument:
        document = HttpDocument()

        for paragraph in self.tree.paragraphs.collection:
            http_paragraph = HttpParagraph()

            for item in paragraph.sentences.collection:
                if isinstance(item, Sentence):
                    for span in item.spans.collection:
                        http_text = self.create_text_node(span, item)
                        http_paragraph.content.append(http_text)
                else:
                    http_text = self.create_text_node(item)
                    http_paragraph.content.append(http_text)

            document.content.append(http_paragraph)

        return document

    def create_text_node(self, span: Span, sentence: Sentence | None = None) -> HttpText:
        marks = []
        if sentence:
            fatigue_mark = HttpMark(
                type="fatigue",
                attrs=HttpMarkAttrs(value=span.fatigue),
            )
            marks.append(fatigue_mark)
            length_mark = HttpMark(
                type="length",
                attrs=HttpMarkAttrs(value=sentence.length_percentage),
            )
            marks.append(length_mark)

        return HttpText(
            text=span.content,
            marks=marks,
        )
