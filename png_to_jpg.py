import argparse
from PIL import Image


def png2jpg(read_img_path: str, save_img_path: str) -> "jpg image":
    """
    Function to convert a png image to jpg.
    """
    png_img = Image.open(read_img_path)
    img_name = read_img_path.split("/")[-1].split(".")[0]
    jpg_img = png_img.save(save_img_path + "/" + img_name + ".jpg")

    return save_img_path + img_name + ".jpg"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_img_path", type=str, help="Path to input image.")
    parser.add_argument("output_img_path", type=str, help="Path to output folder.")

    args = parser.parse_args()
    print(png2jpg(args.input_img_path, args.output_img_path))
    # print(png2jpg("./base_images/dog1.jpg", "./jpg_images/"))
