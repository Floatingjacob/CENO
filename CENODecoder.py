import zlib
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

    # Retrieve metadata (file length + compression flag)
    length = int(binary_data[:32], 2)
    compression_flag = int(binary_data[32:40], 2)
    data_bits = binary_data[40:40 + (length * 8)]

    # Convert bits to bytes
    decoded_data = bytes(int(data_bits[i:i + 8], 2) for i in range(0, len(data_bits), 8))

    # Decompress if needed
    if compression_flag:
        decoded_data = zlib.decompress(decoded_data)

    # Extract the original file name (without _encoded.png)
    base_name = image_path.replace(".png", "")
    
    # Save the decoded file with the original name (excluding .png)
    with open(base_name, "wb") as f:
        f.write(decoded_data)

    print(f"File has been decoded and saved as: {base_name}")

decode_file()
