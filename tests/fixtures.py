import pytest
from aiogram import Router
from aiogram.types import Message, CallbackQuery
from unittest.mock import AsyncMock, MagicMock

@pytest.fixture
def mock_message():
    mock_msg = AsyncMock(spec=Message)
    mock_msg.answer = AsyncMock()
    mock_msg.chat= AsyncMock()
    mock_msg.send_copy = AsyncMock()
    mock_msg.from_user = AsyncMock()
    mock_msg.from_user.id = AsyncMock()
    mock_msg.from_user.username = AsyncMock()
    return mock_msg

@pytest.fixture
def mock_router():
    router = Router()
    return router

@pytest.fixture
def mock_callback_query():
    mock = MagicMock(spec=CallbackQuery)
    mock.message = MagicMock()
    mock.message.answer = AsyncMock()
    mock.from_user = MagicMock()
    mock.data = "button_callback"
    mock.from_user.username = "test_user"
    return mock
