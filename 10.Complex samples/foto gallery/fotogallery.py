"""
Write a Python program. 
The program should load bolder from the "Photos" subdirectory and display it. 
The images should be displayed sequentially every 10 seconds.

"""

import os
import time
from PIL import Image

# --- Directory containing images ---
photos_dir = os.path.join(os.path.dirname(__file__), "Photos")

# --- Get list of image files (common formats) ---
image_files = [f for f in os.listdir(photos_dir)
               if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

# --- Sort files for consistent order ---
image_files.sort()

# --- Display each image sequentially every 10 seconds ---
for img_name in image_files:
    img_path = os.path.join(photos_dir, img_name)
    img = Image.open(img_path)
    img.show()
    print(f"Displaying: {img_name}")
    time.sleep(10)  # Wait 10 seconds before showing the next image
    img.close()