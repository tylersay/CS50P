import sys
from PIL import Image, ImageOps
import os

def main():
    check_args()
    input_img = open_input()
    overlay = Image.open("shirt.png")
    fitted = ImageOps.fit(input_img, overlay.size)
    fitted.paste(overlay, overlay)
    fitted.save(sys.argv[2])



def open_input():
    try:
        input_img = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    else:
        return input_img

def check_args():
    input_file_ext = os.path.splitext(sys.argv[1])[1].lower()
    output_file_ext = os.path.splitext(sys.argv[2])[1].lower()
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif input_file_ext != ".png" and input_file_ext != ".jpg" and input_file_ext != ".jpeg":
        sys.exit("Not an image file")
    elif input_file_ext != output_file_ext:
        sys.exit("Input and output have different extensions")
    else:
        # print(input_file_ext, output_file_ext)
        return True

if __name__ == "__main__":
    main()