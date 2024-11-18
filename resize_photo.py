import os
from PIL import Image

# Paths to the folders
input_folder = '/Users/brendonshuke/Downloads/photos'
output_folder = '/Users/brendonshuke/Downloads/photos/resized'

# Make sure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Desired width and height
new_width = 250
new_height = 250

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # Add more extensions if needed
        img_path = os.path.join(input_folder, filename)

        with Image.open(img_path) as img:
            # Resize image while maintaining aspect ratio
            # aspect_ratio = img.width / img.height
            # adjusted_height = int(new_width / aspect_ratio)
            resized_img = img.resize((new_width, new_height))

            # Save resized image to the output folder
            output_path = os.path.join(output_folder, filename)
            resized_img.save(output_path)

print("All images have been resized and saved to the output folder.")
