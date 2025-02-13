from PIL import Image
import os

# Define the input and output directories
input_dir = r'D:\sherkat\dataset\images\changingFormat\input'
output_dir = r'D:\sherkat\dataset\images\changingFormat\output'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through all PNG files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.png'):
        # Open the PNG image
        img = Image.open(os.path.join(input_dir, filename))
        
        # Convert the image to RGB mode (JPEG doesn't support alpha channel)
        rgb_img = img.convert('RGB')
        
        # Save the image as JPEG
        jpg_filename = os.path.splitext(filename)[0] + '.jpg'
        rgb_img.save(os.path.join(output_dir, jpg_filename), 'JPEG')

print("Conversion complete!")