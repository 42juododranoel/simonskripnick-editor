

from editor.apps.spellchecker.entities import Sentence, SentenceLength, Tree
from editor.apps.spellchecker.processors.transformers.spans_transformer import (
    SpansTransformer,
)
from editor.base.processors import BaseProcessor

CENTROID_LENGTHS = {
    0: SentenceLength.SHORT,
    1: SentenceLength.MEDIUM,
    2: SentenceLength.LONG,
}


class TreeTransformer(BaseProcessor):
    """Spellcheck a tree."""

    def __init__(self, tree: Tree) -> None:
        self.tree = tree
        self.context = self.tree.context

    def run(self) -> Tree:
        for paragraph in self.tree.paragraphs.collection:
            sentences = filter(
                lambda item: isinstance(item, Sentence),
                paragraph.sentences.collection,
            )
            for sentence in sentences:
                self.spellcheck_spans(sentence)

    def spellcheck_spans(self, sentence: Sentence) -> None:
        spans_transformer = SpansTransformer(sentence.spans)
        spans_transformer()
