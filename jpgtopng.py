import sys
import os
from PIL import Image, ImageFilter

#Grab Current and New Folder
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#Check if New exist, or create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#Loop through folder, convert images to PNG
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}', 'png')   #Save to new folder


