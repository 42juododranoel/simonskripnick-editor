from editor.apps.analyzer.entities import Context, Paragraph, Paragraphs, Sentence, Text
from editor.apps.analyzer.processors.paragraphs_creator import ParagraphsCreator
from editor.apps.analyzer.processors.sentences_creator import SentencesCreator
from editor.apps.analyzer.processors.spans_creator import SpansCreator
from editor.base.processors import BaseProcessor


class TextCreator(BaseProcessor):
    """Create a text from raw string input."""

    def __init__(self, content: str) -> None:
        self.content = content
        self.context = Context()

    def run(self) -> Text:
        text = Text(content=self.content, paragraphs=Paragraphs(), context=self.context)
        self.create_paragraphs(text)

        for paragraph in text.paragraphs.collection:
            self.create_sentences(paragraph)
            self.context.paragraph_count += 1

            sentences = filter(
                lambda item: isinstance(item, Sentence),
                paragraph.sentences.collection,
            )
            for sentence in sentences:
                self.create_spans(sentence)
                self.context.sentence_count += 1

                self.context.word_count += sentence.spans.count
                self.context.sentence_lengths.append(sentence.spans.count)

        return text

    def create_paragraphs(self, text: Text) -> None:
        paragraphs_creator = ParagraphsCreator(text, self.context)
        paragraphs_creator()

    def create_sentences(self, paragraph: Paragraph) -> None:
        sentences_creator = SentencesCreator(paragraph, self.context)
        sentences_creator()

    def create_spans(self, sentence: Sentence) -> None:
        spans_creator = SpansCreator(sentence, self.context)
        spans_creator()
