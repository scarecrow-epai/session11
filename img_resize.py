import argparse
from PIL import Image


def calc_percent_change(w: int, h: int, p: int) -> "New H/W":
    """
    Calculate new height and width based on percent change.
    """
    new_w = w * (1 + p / 100)
    new_h = h * (1 + p / 100)

    return int(new_w), int(new_h)


def img_resize(input_img_path: str, output_img_path: str, **kwargs) -> "Resized Image":
    """
    Function to resize image based on parameters provided.
    Percent based, height based, width based.
    """
    img = Image.open(input_img_path)
    width, height = img.size
    if kwargs["resize_type"] == "res_p":
        new_width, new_height = calc_percent_change(
            width, height, int(kwargs["resize_val"])
        )

    elif kwargs["resize_type"] == "res_h":
        new_width, new_height = width, int(kwargs["resize_val"])

    elif kwargs["resize_type"] == "res_w":
        new_width, new_height = int(kwargs["resize_val"]), height

    elif kwargs["resize_type"] == None:
        new_width, new_height = width, height

    else:
        raise ValueError("Incorrect resize type.")

    new_img = img.resize((new_width, new_height))
    new_image_name = (
        output_img_path
        + input_img_path.split(".")[-2].split("/")[-1]
        + "_resized."
        + input_img_path.split(".")[-1]
    )
    new_img.save(new_image_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_img_path", type=str, help="Path to input image.")
    parser.add_argument("output_img_path", type=str, help="Path to output folder.")
    parser.add_argument("-resize_type", type=str, help="Resize by percent/dim.")
    parser.add_argument("-resize_val", help="Resize val.")

    args = parser.parse_args()

    img_resize(
        args.input_img_path,
        args.output_img_path,
        resize_type=args.resize_type,
        resize_val=args.resize_val,
    )
