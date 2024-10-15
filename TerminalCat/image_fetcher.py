# image_fetcher.py

import requests
from PIL import Image
import io

def fetch_image(url: str, headers: dict) -> bytes:
    """
    Fetches image data from the specified URL with given headers.

    Args:
        url (str): The URL to fetch the image from.
        headers (dict): HTTP headers to include in the request.

    Returns:
        bytes: Binary content of the fetched image.

    Raises:
        requests.HTTPError: If the HTTP request returned an unsuccessful status code.
    """
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises HTTPError for bad responses
    return response.content

def process_image(image_data: bytes) -> Image.Image:
    """
    Processes binary image data and returns a PIL Image object.

    Args:
        image_data (bytes): Binary content of the image.

    Returns:
        Image.Image: PIL Image object.

    Raises:
        IOError: If the image cannot be opened.
    """
    image_bytes = io.BytesIO(image_data)
    image = Image.open(image_bytes)
    return image

def main():
    url = "https://cataas.com/cat?position=center"
    headers = {
        'Accept': "image/*"
    }
    try:
        image_data = fetch_image(url, headers)
        image = process_image(image_data)
        image.show()
    except requests.HTTPError as http_err:
        print("An HTTP error has occurred:", http_err)
        print("Status Code:", http_err.response.status_code)
    except Exception as err:
        print("An error has occurred:", err)

if __name__ == "__main__":
    main()
