import enchant
from textblob import Word

from editor.apps.spellchecker.entities import Spans, SpanSubcategory
from editor.base.processors import BaseProcessor

dictionary = enchant.Dict("en_US")


class SpansTransformer(BaseProcessor):
    """Spellcheck a token collection."""

    def __init__(
        self,
        spans: Spans,
    ) -> None:
        self.spans = spans

    def run(self) -> None:
        for span in self.spans.collection:
            if span.subcategory == SpanSubcategory.WORD and not dictionary.check(span.content):
                word = Word(span.content)
                candidates = word.spellcheck()[:5]
                if candidates:
                    span.spellcheck_candidates = candidates
