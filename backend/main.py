# source venv/Scripts/activate
# uvicorn main:app
# uvicorn main:app --reload # similiar to yarn dev in React
# Saving these commands for command line stuff

# The main imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse # To Send an Audio file back
from fastapi.middleware.cors import CORSMiddleware # Cross origin resource sharing
from decouple import config # To get the API keys from .env
import openai


# Importing custom functions for the app
from functions.openai_requests import convert_audio_to_text, get_chat_response
from functions.database import store_messages, reset_messages
from functions.text_to_speech import convert_text_to_speech

# Initating App
app = FastAPI()


# CORS - Origins
# Domains part of the sever which it can accept and then be called by them
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
]


# CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Checking Health
# An end point requesting data
@app.get("/health")
async def check_health():
    return {"message": "healthy"}


# Reset messages (clearing the database .json file)
@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "Conversation Reset"}



# Getting Audio file
@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...))  : # Receiving an audio from frontend to backend to Fast API
    # Get Saved audio
    # audio_input = open("voice.mp3", "rb")

    # Save file from FrontEnd
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())

    audio_input = open(file.filename, "rb")

    #Decode Audio
    message_decoded = convert_audio_to_text(audio_input)
    ## print(message_decoded) to check if it decoded the emssage

    # Guard: Ensuring the message got decoded
    if not message_decoded:
        return HTTPException(status_code=400, detail="Failed to decode audio")
    
    # Get ChatGPT Response
    chat_response = get_chat_response(message_decoded)

     # Store the messages
    store_messages(message_decoded, chat_response)

     # Guard: Ensuring we got a chat response
    if not chat_response:
        return HTTPException(status_code=400, detail="Failed to get chat response")
    

    # Converting the chat response to audio, sending to eleven labs
    audio_output = convert_text_to_speech(chat_response)

    # Guard: Ensuring the messsage got converted to audio
    if not audio_output:
        return HTTPException(status_code=400, detail="Failed to get Eleven Labs audio response")
    
    # Create a generator that yields chunks of data
    def iterfile():
        yield audio_output

    # Return audio file
    return StreamingResponse(iterfile(), media_type="application/octet-stream") # Decoding in React frontEnd

   # print(chat_response) # The message which ChatGPT sends to the user

  #  return "done"



# Post end point, bot response from the REACT app
# Note: Not playing in browser when using post request