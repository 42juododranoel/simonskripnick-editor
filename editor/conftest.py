from collections.abc import AsyncGenerator, Callable
from typing import Any

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from pytest_mock.plugin import MockerFixture

from editor.app import get_app
from editor.base.processors import BaseProcessor

NOT_PROVIDED = object()


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    """Anyio pytest plugin backend."""
    return "asyncio"


@pytest.fixture
def app() -> FastAPI:
    """FastAPI app."""
    return get_app()


@pytest.fixture
async def client(
    app: FastAPI,
    anyio_backend: str,  # noqa: ARG001
) -> AsyncGenerator[AsyncClient, None]:
    """Test client."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture
def spypatch(mocker: MockerFixture) -> Callable:
    def _spypatch(
        processor: type[BaseProcessor],
        return_value: Any = NOT_PROVIDED,  # noqa: ANN401
    ) -> Callable:
        mocked_init = mocker.spy(processor, "__init__")

        if return_value != NOT_PROVIDED:
            mocker.patch.object(processor, "__call__", return_value=return_value)

        return mocked_init

    return _spypatch
