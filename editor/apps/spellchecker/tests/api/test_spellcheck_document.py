from httpx import AsyncClient
from starlette import status


async def test_spellcheck_document(client: AsyncClient):
    response = await client.post(
        "/api/v1.0.0/spellchecker/spellcheck-document",
        json={
            "type": "doc",
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "What iz it? Move ti! Goood.",
                            "marks": [],
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
                    {"type": "text", "text": "What", "marks": []},
                    {"type": "text", "text": " ", "marks": []},
                    {
                        "type": "text",
                        "text": "iz",
                        "marks": [
                            {
                                "type": "spellcheck",
                                "attrs": {"value": ["in", "it", "is", "i", "if"]},
                            },
                        ],
                    },
                    {"type": "text", "text": " ", "marks": []},
                    {"type": "text", "text": "it", "marks": []},
                    {"type": "text", "text": "?", "marks": []},
                    {"type": "text", "text": " ", "marks": []},
                    {"type": "text", "text": "Move", "marks": []},
                    {"type": "text", "text": " ", "marks": []},
                    {"type": "text", "text": "ti", "marks": []},  # This here needs improvement
                    {"type": "text", "text": "!", "marks": []},
                    {"type": "text", "text": " ", "marks": []},
                    {
                        "type": "text",
                        "text": "Goood",
                        "marks": [
                            {
                                "type": "spellcheck",
                                "attrs": {"value": ["Good", "Blood", "Stood", "Wood", "Food"]},
                            },
                        ],
                    },
                    {"type": "text", "text": ".", "marks": []},
                ],
            },
        ],
    }
