import argparse
from PIL import Image


def jpg2png(read_img_path: str, save_img_path: str) -> "png image":
    """
    Function to convert a jpeg image to png.
    """
    jpg_img = Image.open(read_img_path)
    img_name = read_img_path.split("/")[-1].split(".")[0]
    png_img = jpg_img.save(save_img_path + "/" + img_name + ".png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_img_path", type=str, help="Path to input image.")
    parser.add_argument("output_img_path", type=str, help="Path to output folder.")

    args = parser.parse_args()
    png2jpg(args.input_img_path, args.output_img_path)
