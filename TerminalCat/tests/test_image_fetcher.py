import pytest
from unittest.mock import patch
import requests
from image_fetcher import fetch_image, process_image
from PIL import Image
import io

def test_fetch_image_success():
    url = "https://cataas.com/cat"
    headers = {'Accept': 'image/*'}
    expected_content = b"image_data"

    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = expected_content

        image_data = fetch_image(url, headers)

        assert image_data == expected_content

def test_fetch_image_http_error():
    url = "https://cataas.com/cat"
    headers = {'Accept': 'image/*'}

    with patch('requests.get') as mock_get:
        mock_get.return_value.raise_for_status.side_effect = requests.HTTPError("404 Client Error")

        with pytest.raises(requests.HTTPError):
            fetch_image(url, headers)

def test_process_image_success():
    img = Image.new('RGB', (10, 10), color='red')
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    image_data = img_byte_arr.getvalue()

    processed_image = process_image(image_data)

    assert isinstance(processed_image, Image.Image)

def test_process_image_io_error():
    invalid_image_data = b"not_an_image"

    with pytest.raises(IOError):
        process_image(invalid_image_data)

if __name__ == "__main__":
    pytest.main()
