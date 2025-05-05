from PIL import Image, ImageEnhance, ImageFilter
import argparse
import os

def enhance_image(image_path, output_path, brightness=1.0, contrast=1.0, sharpness=1.0, filter_name=None):
    img = Image.open(image_path)

    # Apply enhancements
    img = ImageEnhance.Brightness(img).enhance(brightness)
    img = ImageEnhance.Contrast(img).enhance(contrast)
    img = ImageEnhance.Sharpness(img).enhance(sharpness)

    # Optional filter
    if filter_name == "BLUR":
        img = img.filter(ImageFilter.BLUR)
    elif filter_name == "DETAIL":
        img = img.filter(ImageFilter.DETAIL)
    elif filter_name == "EDGE_ENHANCE":
        img = img.filter(ImageFilter.EDGE_ENHANCE)

    img.save(output_path)
    print(f"Image saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enhance an image with brightness, contrast, sharpness and filters.")
    parser.add_argument("input", help="Path to the input image")
    parser.add_argument("output", help="Path to save the enhanced image")
    parser.add_argument("--brightness", type=float, default=1.0, help="Brightness factor")
    parser.add_argument("--contrast", type=float, default=1.0, help="Contrast factor")
    parser.add_argument("--sharpness", type=float, default=1.0, help="Sharpness factor")
    parser.add_argument("--filter", choices=["BLUR", "DETAIL", "EDGE_ENHANCE"], help="Apply optional filter")

    args = parser.parse_args()
    enhance_image(args.input, args.output, args.brightness, args.contrast, args.sharpness, args.filter)
