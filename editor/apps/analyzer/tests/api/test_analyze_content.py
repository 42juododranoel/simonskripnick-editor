from collections.abc import Callable

from httpx import AsyncClient
from starlette import status

from editor.apps.analyzer.processors import ContentAnalyzer


async def test_analyze_content(client: AsyncClient, spypatch: Callable, text: str):
    mocked_content_analyzer = spypatch(ContentAnalyzer, text)

    response = await client.post(
        "/api/v1.0.0/analyzer/analyze-content",
        json={"content": "What are you doing?"},
    )

    response_json = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert response_json == {
        "content": "What are you doing? Move it!\r\nThe horn calls — we shall answer.",
        "context": {
            "paragraph_count": 0,
            "sentence_count": 0,
            "token_count": 0,
            "mean_sentence_length": 0,
            "short_sentence_length": 0,
            "medium_sentence_length": 0,
        },
        "paragraphs": {
            "collection": [],
            "count": 0,
        },
    }
    assert mocked_content_analyzer.call_args.kwargs == {"content": "What are you doing?"}
