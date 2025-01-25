import argparse
from rembg import remove
from PIL import Image
import io

def main():
    parser = argparse.ArgumentParser(description="Remove background from images using Rembg.")
    parser.add_argument("-i", "--input", required=True, help="Path to the input image")
    parser.add_argument("-o", "--output", required=True, help="Path to save the output image")
    args = parser.parse_args()

    input_path = args.input
    output_path = args.output

    # Open the image file
    with open(input_path, 'rb') as inp_file:
        input_image = inp_file.read()

    # Remove the background
    output_image = remove(input_image)

    # Save the new image
    with open(output_path, 'wb') as out_file:
        out_file.write(output_image)

    print(f"Background removed and saved to {output_path}")

if __name__ == "__main__":
    main()