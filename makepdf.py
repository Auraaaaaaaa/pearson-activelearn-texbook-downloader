from PIL import Image
import os

def jpgs_to_pdf(image_folder, output_pdf):
    # Get a list of all jpg files in the folder
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]

    # Sort image files (optional, in case you want a specific order)
    image_files.sort()

    # Open images and convert them to RGB format
    images = [Image.open(os.path.join(image_folder, file)).convert('RGB') for file in image_files]

    # Save as PDF (save the first image and append the rest)
    if images:
        images[0].save(output_pdf, save_all=True, append_images=images[1:])
        print(f"PDF created successfully: {output_pdf}")
    else:
        print("No JPG images found in the folder.")

# Example usage:
image_folder = './pictures'
output_pdf = 'output_file.pdf'

jpgs_to_pdf(image_folder, output_pdf)
