# Where Calls to open API are performed
import openai
from decouple import config

# Custom functions
from functions.database import get_recent_messages

# Retreiving ENV
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

# Open AI - Whisper
# Converting Audio To Text
def convert_audio_to_text(audio_file):
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio_file) # Using the whisper API
        message_text = transcript["text"] # Returning a text object
        return message_text
    except Exception as e:
        return

# Open API - Chat GPT
# Getting response to our messages
def get_chat_response(message_input):

    messages = get_recent_messages()
    user_message = {"role": "user", "content": message_input}  # Latest messages to chat GPT which is the decoded audio file
    messages.append(user_message)
    print(messages)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = messages
        )
        message_text = response["choices"][0]["message"]["content"] # The message we get back from Chat GPT
        return message_text
    except Exception as e:
        return