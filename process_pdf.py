from PIL import Image
import os
from pdf2image import convert_from_path


class ProcessPDF:
    def __init__(self, path, output_path):
        self.path = path
        self.output_path = output_path

    # Convert to image
    def convert_to_image(self):
        pages = convert_from_path(self.path, 250)
        for i in range(len(pages)):
            pages[i].save(f'pdf_image/out-{i}.jpg', 'JPEG')

    # Cut the images
    def cut_images(self, min_y, max_y):
        input_folder = self.output_path
        output_folder = self.output_path
        for filename in os.listdir(input_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # Check if the file is an image
                input_image_path = os.path.join(input_folder, filename)
                output_image_path = os.path.join(output_folder, filename)

                # Load the image
                img = Image.open(input_image_path)

                # Get image dimensions
                width, height = img.size

                # Ensure the constraints are within the image dimensions
                if min_y < 0:
                    min_y = 0
                if max_y > height:
                    max_y = height

                # Crop the image
                cropped_img = img.crop((0, min_y, width, max_y))

                # Save the cropped image
                cropped_img.save(output_image_path)
