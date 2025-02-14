import os
from PIL import Image


folder_path = r'D:\sherkat\dataset\images\circles\final'
output_folder = r'D:\sherkat\dataset\images\circles\final\output'


os.makedirs(output_folder, exist_ok=True)



image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]


def crop_to_square(image_path):
    img = Image.open(image_path)
    width, height = img.size
    min_side = min(width, height)
    left = (width - min_side) // 2
    top = (height - min_side) // 2
    right = (width + min_side) // 2
    bottom = (height + min_side) // 2 
    img_cropped = img.crop((left, top, right, bottom))
    target_size = 640  
    img_resized = img_cropped.resize((target_size, target_size))

    return img_resized

for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    square_image = crop_to_square(image_path)
    square_image.save(os.path.join(output_folder, f"square_{image_file}"))

print("Processing complete!")

