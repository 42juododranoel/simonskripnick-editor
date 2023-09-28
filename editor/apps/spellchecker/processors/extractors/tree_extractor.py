from editor.apps.spellchecker.entities import (
    Context,
    Paragraph,
    Paragraphs,
    Sentence,
    Tree,
)
from editor.apps.spellchecker.processors.extractors.paragraphs_extractor import (
    ParagraphsExtractor,
)
from editor.apps.spellchecker.processors.extractors.sentences_extractor import (
    SentencesExtractor,
)
from editor.apps.spellchecker.processors.extractors.spans_extractor import (
    SpansExtractor,
)
from editor.base.processors import BaseProcessor


class TreeExtractor(BaseProcessor):
    """Create a tree from a document."""

    def __init__(self, document: str) -> None:
        self.document = document
        self.context = Context()

    def run(self) -> Tree:
        tree = Tree(document=self.document, paragraphs=Paragraphs(), context=self.context)
        self.extract_paragraphs(tree)

        for paragraph in tree.paragraphs.collection:
            self.extract_sentences(paragraph)
            self.context.paragraph_count += 1

            sentences = filter(
                lambda item: isinstance(item, Sentence),
                paragraph.sentences.collection,
            )
            for sentence in sentences:
                self.extract_spans(sentence)
                self.context.sentence_count += 1

                self.context.word_count += sentence.spans.count
                self.context.sentence_lengths.append(sentence.spans.count)

        return tree

    def extract_paragraphs(self, tree: Tree) -> None:
        paragraphs_extractor = ParagraphsExtractor(tree, self.context)
        paragraphs_extractor()

    def extract_sentences(self, paragraph: Paragraph) -> None:
        sentences_extractor = SentencesExtractor(paragraph, self.context)
        sentences_extractor()

    def extract_spans(self, sentence: Sentence) -> None:
        spans_extractor = SpansExtractor(sentence, self.context)
        spans_extractor()
