# TLGBot - Telegram Bot Python Library

![License](https://img.shields.io/badge/license-MIT-blue.svg)

TLGBot is a Python library for creating Telegram bots with ease. This library simplifies the interaction with the Telegram Bot API, allowing you to send messages, edit group descriptions, and more.

## Installation

You can install TLGBot using pip:

```bash
pip install tlgbot
```
## Getting Started
1. Create a Telegram bot and obtain the API token. You can do this by talking to the BotFather on Telegram.

2. Import the TLGBot class and create an instance with your API token.

```python
from tlgbot import TLGBot

# Replace 'YOUR_API_TOKEN' with your actual bot API token
bot = TLGBot('YOUR_API_TOKEN')
```
Use the library's functions to interact with your bot.

## Usage
## Sending a Message
Send a text message to a chat by specifying the chat ID and message text:

```python
chat_id = 'YOUR_CHAT_ID'  # Replace with the chat ID you want to send the message to
message = 'Hello, Telegram!'
bot.send_message(chat_id, message)
```
## Sending a Photo
Send a photo to a chat by specifying the chat ID, the path to the photo file, and an optional caption:

```python
chat_id = 'YOUR_CHAT_ID'  # Replace with the chat ID you want to send the photo to
photo_path = 'path/to/your/photo.jpg'  # Replace with the actual file path
caption = 'Check out this cool photo!'
bot.send_photo(chat_id, photo_path, caption)
```

## Editing Group Description
Edit the description of a group chat by specifying the chat ID and the new description:

```python
chat_id = 'YOUR_CHAT_ID'  # Replace with the chat ID of the group
new_description = 'This is our updated group description.'
if bot.edit_about(chat_id, new_description):
    print('Group description edited successfully.')
else:
    print('Error editing group description.')
```
## Responding to Last Message
Reply to the last message in a chat by specifying the chat ID and the reply message:

```python
chat_id = 'YOUR_CHAT_ID'  # Replace with the chat ID you want to respond in
reply_message = 'Thanks for your message!'
bot.reply_last_msg(chat_id, reply_message)
```

## EXAMPLE PRODUCTION CODE
```python
from tlgbot import TLGBot

# Define tu token
token = 'Your_Bot_Token'

# Obtén el último chat ID utilizando la función last_id
chat_id = TLGBot.last_id(token)

if chat_id is not None:
    print(f'Último chat ID: {chat_id}')

    # Define un mensaje de respuesta
    response_message = 'Hello test'

    # Envia el mensaje al último chat ID
    TLGBot.send_message(TLGBot(token), chat_id, response_message)
    print('Mensaje enviado exitosamente.')
else:
    print('No se pudo obtener el chat ID.')

```

## License
This library is available under the MIT license.

## Support
If you have any questions, suggestions, or need help with this library, please create an issue on the [Github Repository](https://github.com/GDLegions/tlgbot).
