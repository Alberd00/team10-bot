import pytest
from main import main
from unittest.mock import patch, AsyncMock, MagicMock
import asyncio
from fixtures import mock_bot, mock_set_command_list, mock_dispatcher, mock_router, mock_callbacks_router,mock_handlers_router, mock_setup_logger

@pytest.mark.asyncio
async def test_main_initialization(mock_bot, mock_dispatcher, mock_handlers_router, mock_callbacks_router, mock_set_command_list, mock_setup_logger):
    with patch("main.Bot", return_value=mock_bot), \
         patch("main.Dispatcher", return_value=mock_dispatcher), \
         patch("handlers.handlers.r", mock_handlers_router), \
         patch("handlers.callbacks.r", mock_callbacks_router):
        await main()

        mock_dispatcher.include_router.assert_any_call(mock_handlers_router)
        mock_dispatcher.include_router.assert_any_call(mock_callbacks_router)
        mock_dispatcher.startup.register.assert_called_once_with(mock_set_command_list)
        mock_dispatcher.start_polling.assert_awaited_once_with(mock_bot)
        mock_setup_logger.assert_called_once()


@pytest.mark.asyncio
async def test_set_command_list(mock_bot):
    from handlers.bot_commands import set_command_list, command_list
    await set_command_list(mock_bot)
    mock_bot.set_my_commands.assert_awaited_once_with(command_list)
