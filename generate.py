import os
import json
import requests
from requests.structures import CaseInsensitiveDict
from dotenv import load_dotenv
from dotenv import find_dotenv
load_dotenv(find_dotenv())

# Set up the DALL-E API endpoint and authorization token
API_ENDPOINT = os.environ.get("API_ENDPOINT")
API_KEY = os.environ.get("API_KEY")

def generate_image(text, size):
    # Generate image using DALL-E API
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = f"Bearer {API_KEY}"

    data = """
    {
        """
    data += f'"prompt": "{text}",'
    data += """
        "num_images":1,
        "size":"%sx%s",
        "response_format":"url"
    }
    """ % (
        size,
        size,
    )

    # To avoid UnboundLocalError
    resp = None

    try:
        resp = requests.post(API_ENDPOINT, headers=headers, data=data, timeout=10)
        resp.raise_for_status()  # Raise an exception if the status code is not 200
    except requests.exceptions.Timeout:
        print("The server did not respond within the allotted time.")
    except requests.exceptions.HTTPError as error:
        print(f"An HTTP error occurred: {error}")
    except requests.exceptions.RequestException as error:
        print(f"An error occurred: {error}")

    if resp is not None:
        response_text = json.loads(resp.text)
        image_url = response_text["data"][0]["url"]
    else:
        image_url = None    # To avoid UnboundLocalError

    # To avoid UnboundLocalError
    response = None
    
    try:
        # Download and save the generated image
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()  # Raise an exception if the status code is not 200
    except requests.exceptions.Timeout:
        print("The server did not respond within the allotted time.")
    except requests.exceptions.HTTPError as error:
        print(f"An HTTP error occurred: {error}")
    except requests.exceptions.RequestException as error:
        print(f"An error occurred: {error}")

    with open(f"images/{text}.jpeg", "wb") as f:
        f.write(response.content)
