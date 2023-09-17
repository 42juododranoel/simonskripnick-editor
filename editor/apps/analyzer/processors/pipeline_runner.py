from editor.apps.analyzer.entities import HttpDocument
from editor.apps.analyzer.processors.extractors.tree_extractor import TreeExtractor
from editor.apps.analyzer.processors.loaders.document_loader import DocumentLoader
from editor.apps.analyzer.processors.transformers.tree_transformer import (
    TreeTransformer,
)
from editor.base.processors import BaseProcessor


class PipelineRunner(BaseProcessor):
    """Run an ETL pipeline to process a document and return its updated version."""

    def __init__(self, document: HttpDocument) -> None:
        self.document = document

    def run(self) -> HttpDocument:
        tree_extractor = TreeExtractor(document=self.document)
        tree = tree_extractor()

        tree_transformer = TreeTransformer(tree=tree)
        tree_transformer()

        document_loader = DocumentLoader(tree=tree)
        return document_loader()
