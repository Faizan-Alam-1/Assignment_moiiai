import os
import cv2


# Read images from a folder
def read_images(image_folder):
    images = {}
    for filename in os.listdir(image_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(image_folder, filename)
            img = cv2.imread(img_path)
            if img is not None:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
                images[filename] = img
            else:
                print(f"Failed to read image {img_path}")
    return images