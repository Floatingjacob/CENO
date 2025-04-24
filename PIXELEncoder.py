import os
from PIL import Image
def create_metadata(length):
    return length.to_bytes(4, byteorder='big')
def generate_palette():
    palette = []
    for i in range(256):
        r = (i * 5) % 256
        g = (i * 7) % 256
        b = (i * 13) % 256
        palette.extend([r, g, b])
    return palette
def data_to_color_index(data_byte):
    return data_byte
def encode(data):
    metadata = create_metadata(len(data))
    binary_data = bytearray(metadata) + bytearray(data)
    palette = generate_palette()
    pixel_indices = [data_to_color_index(byte) for byte in binary_data]
    width = int(len(pixel_indices) ** 0.5) + 1
    height = (len(pixel_indices) // width) + 1
    img = Image.new('P', (width, height), 0)
    img.putpalette(palette)
    img.putdata(pixel_indices)
    return img
def save_file():
    print(f"Welcome to PIXEL!")
    input_path = input("Enter the path to the file you want to encode: ")
    with open(input_path, "rb") as f:
        file_data = f.read()
    img = encode(file_data)
    base_name, ext = os.path.splitext(input_path)
    output_path = f"{base_name}{ext}.png"
    img.save(output_path, "PNG", optimize=True)
    print(f"Encoded file saved as: {output_path}")
save_file()
