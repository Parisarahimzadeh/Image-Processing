import cv2
import os

def split_image(image, target_size=(640, 640)):
    h, w, _ = image.shape

    
    if w >= target_size[0] * 2:
       
        left_part = image[:, :target_size[0]]  
        right_part = image[:, target_size[0]:target_size[0]*2]  
        
        
        left_part = left_part[:target_size[1], :]
        right_part = right_part[:target_size[1], :]
        
        return left_part, right_part
    elif h >= target_size[1] * 2:
        
        top_part = image[:target_size[1], :]  
        bottom_part = image[target_size[1]:target_size[1]*2, :]  
        
        
        top_part = top_part[:, :target_size[0]]
        bottom_part = bottom_part[:, :target_size[0]]
        
        return top_part, bottom_part
    else:
        raise ValueError("Image is too small to split into two 640x640 sections.")

def split_images_in_folder(input_folder, output_folder, target_size=(640, 640)):
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):  
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)

            try:
                
                left_part, right_part = split_image(image, target_size)

                
                left_filename = f"left_{filename}"
                right_filename = f"right_{filename}"

                cv2.imwrite(os.path.join(output_folder, left_filename), left_part)
                cv2.imwrite(os.path.join(output_folder, right_filename), right_part)

                print(f"Split and saved: {left_filename}, {right_filename}")

            except ValueError as e:
                print(f"Skipping {filename}: {e}")


input_folder = r'D:\sherkat\dataset\images\circles\final'  
output_folder = r'D:\sherkat\dataset\images\circles\resize'  

split_images_in_folder(input_folder, output_folder)
