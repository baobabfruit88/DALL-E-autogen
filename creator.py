from generate import generate_image
import os
import json
import random
from os import path
import subprocess
import platform
from dotenv import load_dotenv
from dotenv import find_dotenv

def auto_create(suggestion=None):
    # Load the suggestions from a JSON file
    if suggestion is None:
        try:
            with open("suggestion_list.json") as f:
                suggestions = json.load(f)
        except:
            if platform.system() == 'windows':
                subprocess.run(["explorer", ''])
            else:
                subprocess.run(["open", ''])
            return "The json list has no values or is improperly formated, file location will be opened now so you can review."
        # Remove the selected suggestion from the list
        suggestions.remove(suggestion)

        # Generate a random suggestion
        
        suggestion = random.choice(suggestions)
        
        # Save the modified list back to the JSON file
        with open("suggestion_list.json", "w") as f:
            json.dump(suggestions, f)

        text = suggestion
    else:
        text = suggestion

    size = "1024"
    text = text.replace(" ", "_")
    # Define the path to your image file and the caption for your post
    generate_image(text, size)

    image_path = "images/" + suggestion.replace(" ", "_") + ".jpeg"
    caption = (
        "title : "
        + suggestion
        + " #opensea. #aiart #generativeart #creativecoding #digitalart #artificialintelligence #artofinstagram"
    )
    
    if platform.system() == 'windows':
        subprocess.run(["explorer", 'images'])
    else:
        subprocess.run(["open", 'images'])

    return caption

def update_entries(suggestionlist):
    newlist = suggestionlist.replace("\\", "")
    print(newlist)
    os.remove("suggestion_list.json")
    with open("suggestion_list.json", "w") as f:
        f.write(newlist)

    if os.path.exists("suggestion_list.json"):
        return "The file has been created !"
    else:
        print("File creation failure, please update manually.")


def set_api_key(api_key):
    # Read the contents of the .env file
    with open(".env", "r") as f:
        lines = f.readlines()

    # Update the API_KEY value in the lines list
    for i, line in enumerate(lines):
        if line.startswith("API_KEY="):
            lines[i] = f"API_KEY={api_key}\n"

    # Write the updated contents back to the .env file
    with open(".env", "w") as f:
        f.writelines(lines)

    # Set the new value of the API key in the environment
    os.environ["API_KEY"] = api_key

    return f"API key has been set to : {os.environ.get('API_KEY')}"


def set_dall_e_endpoint(endpoint):
    # Read the contents of the .env file
    with open(".env", "r") as f:
        lines = f.readlines()

    # Update the API_ENDPOINT value in the lines list
    for i, line in enumerate(lines):
        if line.startswith("API_ENDPOINT="):
            lines[i] = f"API_ENDPOINT={endpoint}\n"

    # Write the updated contents back to the .env file
    with open(".env", "w") as f:
        f.writelines(lines)

    # Set the new value of the endpoint key in the environment
    os.environ["API_ENDPOINT"] = endpoint

    return f"API_ENDPOINT has been set to : {os.environ.get('API_ENDPOINT')}"
