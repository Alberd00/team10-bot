import pytest
from fixtures import mock_message, mock_router, mock_callback_query
from handlers.handlers import start, status, help, button, echo
from handlers.callbacks import button_message
from aiogram.types import InlineKeyboardMarkup

@pytest.mark.asyncio
async def test_start(mock_router, mock_message):
    await start(mock_message)
    assert mock_message.answer.called, "message.answer не был вызван"
    called_args, called_kwargs = mock_message.answer.call_args
    assert called_args[0] == f"Привет, {mock_message.from_user.full_name}"

@pytest.mark.asyncio
async def test_status(mock_router, mock_message):
    await status(mock_message)
    assert mock_message.answer.called, "message.answer не был вызван"
    called_args, called_kwargs = mock_message.answer.call_args
    assert called_args[0] == f"Username пользователя - {mock_message.from_user.username}\nId пользователя - {mock_message.from_user.id}"

@pytest.mark.asyncio
async def test_help(mock_router, mock_message):
    await help(mock_message)
    assert mock_message.answer.called, "message.answer не был вызван"
    called_args, called_kwargs = mock_message.answer.call_args
    assert called_args[0] == "Это бот для образовательных целей!)\nРазработчики - команда 10 \nСписок команд:\nstart - запуск бота\nhelp - информация о боте\nstatus - вывод Id и Username пользователя\nbutton - вывод сообщения с кнопкой"

@pytest.mark.asyncio
async def test_button(mock_router, mock_message):
    await button(mock_message)
    assert mock_message.answer.called, "message.answer не был вызван"
    called_args, called_kwargs = mock_message.answer.call_args
    assert called_kwargs['text'] == "Нажмите на кнопку !)"
    markup = called_kwargs['reply_markup']
    assert isinstance(markup, InlineKeyboardMarkup), 'reply_markup не является Inline-клавиатурой'

@pytest.mark.asyncio
async def test_echo_success(mock_message):
    chat_id = 12345
    mock_message.chat.id = chat_id
    await echo(mock_message)
    mock_message.send_copy.assert_awaited_once_with(chat_id=chat_id)


@pytest.mark.asyncio
async def test_button_message(mock_callback_query):
    await button_message(mock_callback_query)
    expected_message = f"Ты нажал на кнопку, {mock_callback_query.from_user.username}"
    mock_callback_query.message.answer.assert_awaited_once_with(expected_message)
