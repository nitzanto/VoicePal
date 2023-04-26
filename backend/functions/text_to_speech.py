import requests # requests from elevenlabs api
from decouple import config

ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY") # The API key from .env

# Eleven Labs
# Converting Text To Speech
def convert_text_to_speech(message):

    # Define voic settings, Data.
    body = {
        "text":message,
        "voice_settings": {
            "stability": 0,
            "similarity_boost":0
        }
    }
    
    # Define voice
    voice_arnold = "VR6AewLTigWG4xSOukaG"

    # Constructing Headers and Endpoint
    headers = { "xi-api-key" : ELEVEN_LABS_API_KEY, "Content-Type": "application/json", "accept": "audio/mpeg"}
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_arnold}"

    # Sending the request
    try:
        response = requests.post(endpoint, json=body, headers=headers)
    except Exception as e:
        return

    # Handle Response
    if response.status_code == 200:
        return response.content # Returning the audio file
    else:
        return