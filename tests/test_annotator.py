import pytest
from typing import List, Callable

from nyan.annotator import Annotator
from nyan.document import Document


def test_annotator_on_snapshot(
    annotator: Annotator,
    input_docs: List[Document],
    output_docs: List[Document],
    compare_docs: Callable
):
    print(f"input_docs: {len(input_docs)}")
    print(f"output_docs: {len(output_docs)}")
    docs = annotator(input_docs)
    print(f"docs after annotator: {len(docs)}")
    docs = annotator.postprocess(docs)
    print(f"docs after annotator postprocess: {len(docs)}")

    # Sort both sets of documents by URL for consistent comparison
    sorted_docs = sorted(docs, key=lambda doc: doc.url)
    sorted_output_docs = sorted(output_docs, key=lambda doc: doc.url)
    assert len(sorted_docs) == len(sorted_output_docs), "Different number of docs"

    for predicted_doc, canonical_doc in zip(sorted_docs, sorted_output_docs):
        compare_docs(predicted_doc, canonical_doc)
