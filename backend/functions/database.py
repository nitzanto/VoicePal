# Setting up getting recent messages
# Latest conversations with chatGPT

import json
import random

# Get Recent messages
def get_recent_messages():
    
    # Defining the File name and learn instruction (feeding the chatGPT with roles)
    file_name = "stored_data.json"
    learn_instruction = {
        "role": "system",
        "content" : "You are interviewing the user for a job as a software developer. Ask short questions that are relevant to the Junior position. Your name is Arnold. The user is called Nitzan. Keep your answers to under 30 words."
    }

    # Initalize messages
    messages = []

    # Add a random element
    x = random.uniform(0,1)
    if x < 0.5:
        learn_instruction["content"] = learn_instruction["content"] + " Your response will include some dry humor."
    else:
         learn_instruction["content"] = learn_instruction["content"] + " Your response will include a rather challenging question."

    # Append instruction to messages
    messages.append(learn_instruction)

    # Get last messages
    try:
        with open(file_name) as user_file: # Basically opening the .json file which includes the history data
            data = json.load(user_file)

            # Append last 5 times of data, the recent context last 5 rows.
            if data:
             if len(data) < 5:
                    for item in data:
                        messages.append(item)
             else:
                for item in data[-5:]: # Appending the last five items of data
                        messages.append(item)

    except Exception as e:
        print(e)
        pass
    # Return 
    return messages


# Store Messages (Will act as the Database)
def store_messages(request_message, response_message):
    # Defining the File Name
    file_name = "stored_data.json" # The database

    # Getting the recent messages
    messages = get_recent_messages()[1:]

    # req mess - user, res message - chatGPT

    # Adding messages to data
    user_message = {"role": "user", "content": request_message}
    assistant_message = {"role": "assistant", "content": response_message}
    messages.append(user_message)
    messages.append(assistant_message)


    # Save the updated file
    with open(file_name, "w") as f:
        json.dump(messages,f) # saving the data into the json file


# Reset messages
def reset_messages():
    # Overwrite current file with nothing
        open("stored_data.json", "w")