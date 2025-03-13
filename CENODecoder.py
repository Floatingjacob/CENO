import zipfile
from PIL import Image
import base64
import io
Image.MAX_IMAGE_PIXELS = None

binary_color_map = {
    (0, 0, 0): '00',
    (255, 0, 0): '01',
    (0, 255, 0): '10',
    (0, 0, 255): '11',
}

def decode(img):
    pixels = img.load()
    width, height = img.size
    binary_data = []
    
    for y in range(0, height, 5):
        for x in range(0, width, 5):
            color = pixels[x, y]
            
            if color == (255, 255, 255):
                continue
                
            if color in binary_color_map:
                binary_data.append(binary_color_map[color])
            else:
                raise ValueError(f"Unknown color found: {color}")

    binary_data = ''.join(binary_data)
    encoded_data = ''.join(chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8))
    decoded_data = base64.b64decode(encoded_data)
    
    return decoded_data

def decode_zip(zip_file_path, output_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zipf:
        zipf.extract("color_ceno.png", "/tmp")

    img = Image.open("/tmp/color_ceno.png")
    decoded_data = decode(img)

    with open(output_file_path, "wb") as f:
        f.write(decoded_data)

    print(f"File has been decoded and saved to: {output_file_path}")

zip_file_path = input("Enter the path to the ZIP file with CE,NO: ")
output_file_path = input("Enter the name of the decoded file: ")

decode_zip(zip_file_path, output_file_path)
