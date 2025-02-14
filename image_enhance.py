import os
from PIL import Image, ImageEnhance
import cv2
import numpy as np


folder_path = r'D:\sherkat\dataset\images\circles\input\contrast_roshan'
output_folder = r'D:\sherkat\dataset\images\circles\output\contrast_roshan'


os.makedirs(output_folder, exist_ok=True)


image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

def adjust_contrast(image_path):
    img = Image.open(image_path)
    enhancer = ImageEnhance.Contrast(img)
    return enhancer.enhance(0.5)  


def add_light_reflection(image_path):
    image = cv2.imread(image_path)
    reflection = np.zeros_like(image)
    reflection[:, :] = (255, 255, 255)  
    reflection_intensity = 0.2  
    reflected_image = cv2.addWeighted(image, 1 - reflection_intensity, reflection, reflection_intensity, 0)
    return reflected_image


for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    

    contrast_image = adjust_contrast(image_path)
    contrast_image.save(os.path.join(output_folder, f"contrast_{image_file}"))
    

    reflected_image = add_light_reflection(image_path)
    reflected_image_path = os.path.join(output_folder, f"reflected_{image_file}")
    cv2.imwrite(reflected_image_path, reflected_image)

print("Processing complete!")
