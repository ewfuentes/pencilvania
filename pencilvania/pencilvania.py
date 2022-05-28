
import argparse

from pencilvania import random_dot
import torch

style_from_style_name = {
    'random_dot': random_dot.RandomDot
}

def main(image_path: str, style: str):
    print(image_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create stylized images suitable for a pen plotter")
    parser.add_argument("--input_image")
    parser.add_argument("--style")
    args = parser.parse_args()

    main(input_image=args.input_image, style=args.style)
