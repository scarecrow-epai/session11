import argparse
import jpg_to_png, png_to_jpg, img_resize


def get_input_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("op", type=str, help="Choose op type.")
    parser.add_argument("input_img_path", type=str, help="Path to input image.")
    parser.add_argument("output_img_path", type=str, help="Path to output folder.")
    parser.add_argument(
        "-resize_type", type=str, default=None, help="Resize by percent/dim."
    )
    parser.add_argument("-resize_val", default=None, help="Resize val.")

    args = parser.parse_args()
    return args


args = get_input_args()

if args.op == "j2p":
    jpg_to_png.jpg2png(args.input_img_path, args.output_img_path)
elif args.op == "p2j":
    png_to_jpg.png2jpg(args.input_img_path, args.output_img_path)
elif args.op == "resize":
    img_resize.img_resize(
        args.input_img_path,
        args.output_img_path,
        resize_type=args.resize_type,
        resize_val=args.resize_val,
    )
