import argparse
from PyPDF2 import PdfReader, PdfWriter
import copy

def crop_pdf(input_path, output_path):
    """
    Resizes a PDF's pages to A4 format, scaling and centering the content
    while maintaining the aspect ratio.
    """
    # A4 dimensions in points (72 dpi)
    A4_WIDTH = 595
    A4_HEIGHT = 842

    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()

        for original_page in reader.pages:
            # Create a deep copy to avoid modifying the original reader pages
            page = copy.deepcopy(original_page)

            original_width = page.mediabox.width
            original_height = page.mediabox.height

            # Determine the scaling factor
            aspect_ratio_original = float(original_width) / float(original_height)
            aspect_ratio_a4 = float(A4_WIDTH) / float(A4_HEIGHT)

            if aspect_ratio_original > aspect_ratio_a4:
                scale_factor = float(A4_WIDTH) / float(original_width)
            else:
                scale_factor = float(A4_HEIGHT) / float(original_height)

            # New dimensions after scaling
            new_width = original_width * scale_factor
            new_height = original_height * scale_factor

            # Calculate offsets to center the content
            x_offset = (A4_WIDTH - new_width) / 2
            y_offset = (A4_HEIGHT - new_height) / 2

            # Create the transformation matrix: [scale_x, 0, 0, scale_y, translate_x, translate_y]
            ctm = (scale_factor, 0, 0, scale_factor, x_offset, y_offset)

            # Apply the transformation to the page's content
            page.add_transformation(ctm)

            # Set the page's media box to A4 dimensions
            page.mediabox.lower_left = (0, 0)
            page.mediabox.upper_right = (A4_WIDTH, A4_HEIGHT)

            # Also update the crop box to match the media box
            page.cropbox.lower_left = (0, 0)
            page.cropbox.upper_right = (A4_WIDTH, A4_HEIGHT)

            writer.add_page(page)

        with open(output_path, "wb") as f:
            writer.write(f)

        print(f"Successfully cropped '{input_path}' and saved to '{output_path}'")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crop a PDF to A4 format while preserving aspect ratio.")
    parser.add_argument("input_file", help="The path to the input PDF file.")
    parser.add_argument("output_file", help="The path to save the cropped PDF file.")

    args = parser.parse_args()

    crop_pdf(args.input_file, args.output_file)
