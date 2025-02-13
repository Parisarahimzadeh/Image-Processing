import os
from PIL import Image, ImageEnhance
import cv2
import numpy as np

# Folder path
folder_path = 'your_folder_path_here'

# List all files in the folder
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Function to adjust contrast using Pillow
def adjust_contrast(image_path):
    img = Image.open(image_path)
    enhancer = ImageEnhance.Contrast(img)
    return enhancer.enhance(2.0)  # Adjust contrast factor as needed

# Function to add light reflection using OpenCV
def add_light_reflection(image_path):
    image = cv2.imread(image_path)
    reflection = np.zeros_like(image)
    reflection[:, :] = (255, 255, 255)  # White light reflection
    reflection_intensity = 0.2  # Adjust intensity of the reflection
    reflected_image = cv2.addWeighted(image, 1 - reflection_intensity, reflection, reflection_intensity, 0)
    return reflected_image

# Process all images in the folder
for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    
    # Apply contrast adjustment
    contrast_image = adjust_contrast(image_path)
    contrast_image.save(os.path.join(folder_path, f"contrast_{image_file}"))
    
    # Apply light reflection effect
    reflected_image = add_light_reflection(image_path)
    reflected_image_path = os.path.join(folder_path, f"reflected_{image_file}")
    cv2.imwrite(reflected_image_path, reflected_image)

print("Processing complete!")
