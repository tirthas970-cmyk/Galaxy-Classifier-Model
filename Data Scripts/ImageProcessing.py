#Ensuring all images are ready for ML Pipeline

import os
from PIL import Image, ImageOps

input_dir = 'galaxyZoo2Images'
output_dir = 'galaxyZoo2ImagesCleaned'

target_size = (69, 69)

for file_name in os.listdir(input_dir):
    try:
        img = Image.open(os.path.join(input_dir, file_name))

        if img.format != 'JPEG':
            print(f'{file_name} is not a JPEG')
            continue
        
        size_bytes = os.path.getsize(os.path.join(input_dir, file_name))

        if size_bytes == 0:
            print("Size is 0 B -- Corrupted file")
            continue 

        #convert to rbg so each image has 3 color channels
        img = img.convert('RGB')


        #makes it exactly 69, 69 while keeping aspect ratio
        clean_img = ImageOps.pad(img, target_size, color=0, centering=(0.5, 0.5))
        clean_img.save(os.path.join(output_dir, file_name))
    except Exception as e:
        print(f"Skipping unopenable file {file_name}: {e}")

        

print("cleaned images now done")

   
    

