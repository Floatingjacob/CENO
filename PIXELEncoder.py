import os
from PIL import Image

# Helper: Pack 18 bits into a pixel (6 bits per channel)
def bits_to_pixel(bits):
    r = int(bits[:6], 2) if len(bits) >= 6 else 0
    g = int(bits[6:12], 2) if len(bits) >= 12 else 0
    b = int(bits[12:18], 2) if len(bits) >= 18 else 0
    return (r, g, b)

# Helper: Metadata (file length only, no compression flag)
def create_metadata(length):
    return f"{length:032b}"  # Store file length in the first 32 bits

# Encode the data into pixels
def encode(data):
    binary_data = ''.join(format(byte, '08b') for byte in data)

    # Add metadata (file length only)
    metadata = create_metadata(len(data))
    binary_data = metadata + binary_data

    # Pack binary data into 18-bit chunks
    pixels = [bits_to_pixel(binary_data[i:i + 18]) for i in range(0, len(binary_data), 18)]
    return pixels

# Save the encoded image
def save_file():
    print(f"Welcome to PIXEL!")
    input_path = input("Enter the path to the file you want to encode: ")
    with open(input_path, "rb") as f:
        file_data = f.read()

    # Encode the file
    pixels = encode(file_data)

    # Image dimensions (closest to square)
    width = int(len(pixels) ** 0.5) + 1
    height = (len(pixels) // width) + 1

    img = Image.new('RGB', (width, height), (255, 255, 255))
    img.putdata(pixels)

    # Save the image with the original file name and extension before .png
    base_name, ext = os.path.splitext(input_path)
    output_path = f"{base_name}{ext}.png"
    img.save(output_path, "PNG", optimize=True)
    print(f"Encoded file saved as: {output_path}")

save_file()
