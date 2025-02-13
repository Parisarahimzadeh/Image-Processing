import os

def rename_images(input_folder, output_folder, prefix="green"):
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
  
    counter = 738
    
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):  
            image_path = os.path.join(input_folder, filename)
            
            
            new_filename = f"{prefix}_{counter}.jpg"  
            output_path = os.path.join(output_folder, new_filename)
            
            
            os.rename(image_path, output_path)
            print(f"Renamed and moved: {filename} -> {new_filename}")
            
            
            counter += 1


input_folder = r'D:\sherkat\dataset\images\noise\output'  
output_folder = r'D:\sherkat\dataset\images\rename\output'  
prefix = "green"  

rename_images(input_folder, output_folder, prefix=prefix)
