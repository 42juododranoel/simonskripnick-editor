from httpx import AsyncClient
from starlette import status


async def test_analyze_document(client: AsyncClient):
    response = await client.post(
        "/api/v1.0.0/analyzer/analyze-document",
        json={
            "type": "doc",
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "What is it? Move it! Good.",
                            "marks": [
                                {"type": "length", "attrs": {"value": 0}},
                                {"type": "fatigue", "attrs": {"value": 0}},
                            ],
                        },
                    ],
                },
            ],
        },
    )

    response_json = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert response_json == {
        "type": "doc",
        "content": [
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": "What",
                        "marks": [
                            {"type": "fatigue", "attrs": {"value": 0}},
                            {"type": "length", "attrs": {"value": "long"}},
                        ],
                    },
                    {
                        "type": "text",
                        "text": " ",
                        "marks": [
                            {"type": "fatigue", "attrs": {"value": 0}},
                            {"type": "length", "attrs": {"value": "long"}},
                        ],
                    },
                    {
                        "type": "text",
                        "text": "is",
                        "marks": [
                            {"type": "fatigue", "attrs": {"value": 0}},
                            {"type": "length", "attrs": {"value": "long"}},
                        ],
                    },
                    {
                        "type": "text",
                        "text": " ",
                        "marks": [
                            {"type": "fatigue", "attrs": {"value": 0}},
                            {"type": "length", "attrs": {"value": "long"}},
                        ],
                    },
                    {
                        "type": "text",
                        "text": "it",
                        "marks": [
                            {"type": "fatigue", "attrs": {"value": 0}},
                            {"type": "length", "attrs": {"value": "long"}},
                        ],
                    },
                    {
                        "type": "text",
                        "text": "?",
                        "marks": [
                            {"type": "fatigue", "attrs": {"value": 0}},
                            {"type": "length", "attrs": {"value": "long"}},
                        ],
                    },
                    {"type": "text", "text": " ", "marks": []},
                    {
                        "type": "text",
                        "text": "Move",
                        "marks": [
                            {"type": "fatigue", "attrs": {"value": 0}},
                            {"type": "length", "attrs": {"value": "medium"}},
                        ],
                    },
                    {
                        "type": "text",
                        "text": " ",
                        "marks": [
                            {"type": "fatigue", "attrs": {"value": 0}},
                            {"type": "length", "attrs": {"value": "medium"}},
                        ],
                    },
                    {
                        "type": "text",
                        "text": "it",
                        "marks": [
                            {"type": "fatigue", "attrs": {"value": 0}},
                            {"type": "length", "attrs": {"value": "medium"}},
                        ],
                    },
                    {
                        "type": "text",
                        "text": "!",
                        "marks": [
                            {"type": "fatigue", "attrs": {"value": 0}},
                            {"type": "length", "attrs": {"value": "medium"}},
                        ],
                    },
                    {"type": "text", "text": " ", "marks": []},
                    {
                        "type": "text",
                        "text": "Good",
                        "marks": [
                            {"type": "fatigue", "attrs": {"value": 0}},
                            {"type": "length", "attrs": {"value": "short"}},
                        ],
                    },
                    {
                        "type": "text",
                        "text": ".",
                        "marks": [
                            {"type": "fatigue", "attrs": {"value": 0}},
                            {"type": "length", "attrs": {"value": "short"}},
                        ],
                    },
                ],
            },
        ],
    }
