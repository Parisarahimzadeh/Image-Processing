import cv2
import os
import random
import numpy as np

# Function to add salt and pepper noise (brown and white)
def add_salt_pepper_noise(image, salt_prob=0.005, pepper_prob=0.005, salt_color=(255, 255, 255), pepper_color=(139, 69, 19)):
    noisy_image = image.copy()
    total_pixels = noisy_image.size
    num_salt = int(salt_prob * total_pixels)
    num_pepper = int(pepper_prob * total_pixels)

    # Add salt noise (white)
    for _ in range(num_salt):
        x = random.randint(0, noisy_image.shape[0] - 1)
        y = random.randint(0, noisy_image.shape[1] - 1)
        noisy_image[x, y] = salt_color

    # Add pepper noise (brown)
    for _ in range(num_pepper):
        x = random.randint(0, noisy_image.shape[0] - 1)
        y = random.randint(0, noisy_image.shape[1] - 1)
        noisy_image[x, y] = pepper_color

    return noisy_image

# Function to add random flip noise
def add_flip_noise(image, flip_prob=0.2):
    if random.random() < flip_prob:
        return cv2.flip(image, 1)  # Horizontal flip
    return image

# Function to add light reflection noise (tiny reflection effect)
def add_light_reflection_noise(image, reflection_prob=0.05):
    noisy_image = image.copy()
    if random.random() < reflection_prob:
        h, w, _ = noisy_image.shape
        x1, x2 = random.randint(0, w//2), random.randint(w//2, w)
        noisy_image[:, x1:x2] = 255  # Apply light reflection to a random region
    return noisy_image

# Function to randomly apply noise to an image
def apply_random_noise(image):
    # Apply salt and pepper noise with a very low probability
    image = add_salt_pepper_noise(image, salt_prob=0.005, pepper_prob=0.005)
    
    # Apply flip noise with higher probability
    image = add_flip_noise(image, flip_prob=0.15)
    
    # Apply light reflection noise with a low probability
    image = add_light_reflection_noise(image, reflection_prob=0.05)

    return image

def process_images_in_folder(input_folder, output_folder):
    # Make sure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Loop through all images in the folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # You can add other extensions if needed
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)

            # Apply random noise to the image
            noisy_image = apply_random_noise(image)

            # Save the noisy image to the output folder
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, noisy_image)
            print(f"Processed and saved: {filename}")

# Example usage
input_folder = r'D:\sherkat\dataset\images\noise\input'  # Replace with your input folder path
output_folder = r'D:\sherkat\dataset\images\noise\output'  # Replace with your output folder path

process_images_in_folder(input_folder, output_folder)
