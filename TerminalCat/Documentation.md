# Image Fetcher

This is a Python module for fetching and processing images from the internet. It provides functionality to retrieve images from a given URL and convert the binary data into a `PIL` (Pillow) image object.

## Features

- **Fetch Image**: Retrieve image data from a specified URL using HTTP GET requests.
- **Process Image**: Convert binary image data into a `PIL` image object for further manipulation.

## Requirements

- Python 3.7+
- [Requests](https://docs.python-requests.org/en/master/) - A simple library for making HTTP requests.
- [Pillow](https://pillow.readthedocs.io/en/stable/) - A popular Python Imaging Library for working with images.

## Installation

First, clone the repository and navigate to the project directory:

```
git clone https://github.com/hashaam1217/GTCInterviewPrep
cd GTCInterviewPrep/TerminalCat
```

Install the dependencies:

```
pip install -r requirements.txt
```

## Usage

You can use the `image_fetcher.py` module to fetch and display images from a URL.

Example:

```python
from image_fetcher import fetch_image, process_image

url = "https://example.com/image"
headers = {
    'Accept': "image/*"
}

try:
    image_data = fetch_image(url, headers)
    image = process_image(image_data)
    image.show()
except Exception as e:
    print("An error has occurred:", e)
```

The above code fetches an image from the specified URL and displays it.

## Running Tests

This project uses `pytest` for unit testing. To run the tests, simply execute:

```
pytest
```

### Test Cases
- **`test_fetch_image_success()`**: Tests if the `fetch_image` function successfully retrieves image data.
- **`test_fetch_image_http_error()`**: Tests if the `fetch_image` function correctly handles HTTP errors.
- **`test_process_image_success()`**: Tests if the `process_image` function successfully processes valid image data.
- **`test_process_image_io_error()`**: Tests if the `process_image` function raises an `IOError` for invalid image data.

## File Structure

- `image_fetcher.py`: Main module for fetching and processing images.
- `test_image_fetcher.py`: Unit tests for the module.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Contributing

Feel free to submit issues or pull requests if you have any improvements or bug fixes.

## Author

- [Your Name]

## Acknowledgements

- [Requests Library](https://docs.python-requests.org/en/master/)
- [Pillow (PIL) Library](https://pillow.readthedocs.io/en/stable/)
