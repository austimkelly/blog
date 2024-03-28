import base64
from PIL import Image
import io

def encode_image(image_path):
    # Open the image file in binary mode
    with open(image_path, 'rb') as image_file:
        # Read the image data
        image_data = image_file.read()

    # Base64 encode the image data
    encoded_image_data = base64.b64encode(image_data)

    # Convert the encoded data to a string
    encoded_image_str = encoded_image_data.decode('utf-8')

    return encoded_image_str