from PIL import Image
import os

def resize_images_in_folder(input_folder, output_folder, size=(640, 640)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # ساخت پوشه‌ی خروجی در صورت عدم وجود

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # بررسی فرمت‌های تصویر
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            img = Image.open(input_path)
            img.thumbnail(size, Image.LANCZOS)  # حفظ کیفیت و نسبت تصویر

            # ایجاد پس‌زمینه سفید
            canvas = Image.new("RGB", size, (255, 255, 255))
            x_offset = (size[0] - img.size[0]) // 2
            y_offset = (size[1] - img.size[1]) // 2
            canvas.paste(img, (x_offset, y_offset))

            canvas.save(output_path, quality=95)  # ذخیره تصویر با کیفیت بالا

    print("✅ تمام تصاویر با موفقیت تغییر اندازه داده شدند.")

# مسیر فولدر ورودی و خروجی
input_folder = "/home/basa/Documents/GitHub/Almond-Skin-Detection/Almond"   # فولدری که تصاویر اصلی داخل آن هستند
output_folder = "/home/basa/Documents/GitHub/Almond-Skin-Detection/test"  # فولدر ذخیره‌ی تصاویر تغییر اندازه داده‌شده

resize_images_in_folder(input_folder, output_folder)