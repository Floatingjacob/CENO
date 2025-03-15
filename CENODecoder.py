import os
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

# Helper: Extract 18-bit data from a pixel
def pixel_to_bits(pixel):
    r, g, b = pixel
    return f"{r:06b}{g:06b}{b:06b}"

# Decode the image to original data
def decode_file():
    image_path = input("Enter the encoded image path: ")
    img = Image.open(image_path)
    pixels = list(img.getdata())

    # Extract binary data from image
    binary_data = ''.join(pixel_to_bits(p) for p in pixels)

    # Retrieve metadata (file length)
    length = int(binary_data[:32], 2)  # Read first 32 bits for length
    data_bits = binary_data[32:32 + (length * 8)]  # Extract raw data bits

    # Convert bits to bytes
    decoded_data = bytes(int(data_bits[i:i + 8], 2) for i in range(0, len(data_bits), 8))

    # Extract the original file name (without .png)
    base_name = image_path.replace(".png", "")

    # Save the decoded file with the original name (excluding .png)
    with open(base_name, "wb") as f:
        f.write(decoded_data)

    print(f"File has been decoded and saved as: {base_name}")

decode_file()
