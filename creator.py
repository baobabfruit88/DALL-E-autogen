import os
import json
import random
import subprocess
import platform
from generate import generate_image

def auto_create(suggestion=None):
    # Load the suggestions from a JSON file
    if suggestion is None:
        filename = "suggestion_list.json"
        if not os.path.isfile(filename):
            with open(filename, "w") as f:
                f.write("[]")
            if platform.system() == 'windows':
                subprocess.run(["explorer", f'{filename}'])
            else:
                subprocess.run(["open", f'{filename}'])
            return "The suggestions file did not exist, we have ceated it please fill it"
        else:
            with open("suggestion_list.json") as f:
                suggestions = json.load(f)

            suggestion = random.choice(suggestions)
            suggestions.remove(suggestion)

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


def update_entries():
    filename = "suggestion_list.json"
    if not os.path.isfile(filename):
            with open(filename, "w") as f:
                f.write("[]")
            if platform.system() == 'windows':
                subprocess.run(["explorer", f'{filename}'])
            else:
                subprocess.run(["open", f'{filename}'])
            return "The file did not exist, we have ceated it please fill it"
    else:
        if platform.system() == 'windows':
            subprocess.run(["explorer", f'{filename}'])
        else:
            subprocess.run(["open", f'{filename}'])
        return "update as you see fit"



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
