from PIL import Image
import os


input_dir = r'D:\sherkat\dataset\images\circles\final\output'
output_dir = r'D:\sherkat\dataset\images\circles\format'


if not os.path.exists(output_dir):
    os.makedirs(output_dir)


for filename in os.listdir(input_dir):
    if filename.endswith('.png'):
        
        img = Image.open(os.path.join(input_dir, filename))
        
        
        rgb_img = img.convert('RGB')
        
        
        jpg_filename = os.path.splitext(filename)[0] + '.jpg'
        rgb_img.save(os.path.join(output_dir, jpg_filename), 'JPEG')

print("Conversion complete!")



