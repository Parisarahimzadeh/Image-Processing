import cv2
import os
import random
import numpy as np


def add_salt_pepper_noise(image, salt_prob=0.005, pepper_prob=0.005, salt_color=(255, 255, 255), pepper_color=(139, 69, 19)):
    noisy_image = image.copy()
    total_pixels = noisy_image.size
    num_salt = int(salt_prob * total_pixels)
    num_pepper = int(pepper_prob * total_pixels)

   
    for _ in range(num_salt):
        x = random.randint(0, noisy_image.shape[0] - 1)
        y = random.randint(0, noisy_image.shape[1] - 1)
        noisy_image[x, y] = salt_color

    
    for _ in range(num_pepper):
        x = random.randint(0, noisy_image.shape[0] - 1)
        y = random.randint(0, noisy_image.shape[1] - 1)
        noisy_image[x, y] = pepper_color

    return noisy_image


def add_flip_noise(image, flip_prob=0.2):
    if random.random() < flip_prob:
        return cv2.flip(image, 1)  
    return image


def add_light_reflection_noise(image, reflection_prob=0.05):
    noisy_image = image.copy()
    if random.random() < reflection_prob:
        h, w, _ = noisy_image.shape
        x1, x2 = random.randint(0, w//2), random.randint(w//2, w)
        noisy_image[:, x1:x2] = 255 
    return noisy_image


def apply_random_noise(image):
    
    image = add_salt_pepper_noise(image, salt_prob=0.005, pepper_prob=0.005)
    
    
    image = add_flip_noise(image, flip_prob=0.15)
    
    
    image = add_light_reflection_noise(image, reflection_prob=0.05)

    return image

def process_images_in_folder(input_folder, output_folder):
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
   
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):  
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)

           
            noisy_image = apply_random_noise(image)

           
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, noisy_image)
            print(f"Processed and saved: {filename}")


input_folder = r'D:\sherkat\dataset\images\noise\input'  
output_folder = r'D:\sherkat\dataset\images\noise\output'  

process_images_in_folder(input_folder, output_folder)
