import requests
from requests.structures import CaseInsensitiveDict
import json
import os
from PIL import Image

# Set up the DALL-E API endpoint and authorization token
API_ENDPOINT = os.environ.get("API_ENDPOINT")
API_KEY = os.environ.get("API_KEY")

# Define a function to generate an image from a given string
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

    resp = requests.post(API_ENDPOINT, headers=headers, data=data)

    if resp.status_code != 200:
        raise ValueError("Failed to generate image: %s" % resp.text)

    response_text = json.loads(resp.text)
    image_url = response_text["data"][0]["url"]

    # Download and save the generated image
    response = requests.get(image_url)
    with open(f"images/{text}.jpeg", "wb") as f:
        f.write(response.content)
