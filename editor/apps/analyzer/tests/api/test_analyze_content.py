from collections.abc import Callable

from httpx import AsyncClient
from starlette import status

from editor.apps.analyzer.entities import Text
from editor.apps.analyzer.processors import TextAnalyzer, TextCreator


async def test_analyze_content(client: AsyncClient, spypatch: Callable, text: Text):
    mocked_text_creator = spypatch(TextCreator, text)
    mocked_text_analyzer = spypatch(TextAnalyzer)

    response = await client.post(
        "/api/v1.0.0/analyzer/analyze-content",
        json={"content": "What are you doing?"},
    )

    response_json = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert response_json == {
        "content": "What are you doing? Move it!\r\nThe horn calls — we shall answer.",
        "category": "text",
        "context": {
            "paragraph_count": 0,
            "sentence_count": 0,
            "word_count": 0,
            "sentence_lengths": [1, 2, 3],
            "length_centroids": {
                "long": 3,
                "medium": 2,
                "short": 1,
            },
        },
        "paragraphs": {
            "collection": [],
            "count": 0,
        },
    }
    assert mocked_text_creator.call_args.kwargs == {"content": "What are you doing?"}
    assert mocked_text_analyzer.call_args.kwargs == {"text": text}
