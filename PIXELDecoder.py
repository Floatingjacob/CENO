import os
from PIL import Image


def index_to_data(index):
    return index

def decode_file():
    print(f"Welcome to PIXEL!")
    image_path = input("Enter the encoded image path: ")
    img = Image.open(image_path)
    palette = img.getpalette()
    pixel_indices = list(img.getdata())
    metadata = pixel_indices[:4]
    file_length = int.from_bytes(bytes(metadata), byteorder='big')
    print(f"Decoded file length from metadata: {file_length}")
    print(f"Total pixels in image: {len(pixel_indices)}")
    print(f"Total data pixels (excluding metadata): {len(pixel_indices) - 4}")
    data_indices = pixel_indices[4:]
    expected_data_pixels = file_length
    trimmed_data_indices = data_indices[:expected_data_pixels]
    data_bytes = bytearray([index_to_data(index) for index in trimmed_data_indices])
    if len(data_bytes) != file_length:
        print(f"Warning: Decoded data length ({len(data_bytes)}) does not match expected file length ({file_length}).")
        return
    base_name = image_path.replace(".png", "")
    with open(base_name, "wb") as f:
        f.write(data_bytes)

    print(f"File has been decoded and saved as: {base_name}")
decode_file()
