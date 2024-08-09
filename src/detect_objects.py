import os
import cv2
from setting import *
from read_image import * 
from load_label import *
from draw_boxes import *
from save_object_in_json import *



def create_output_folder():
     os.makedirs(os.path.join(OUTPUT_DIR), exist_ok=True)


def read_image_path():
    images = read_images(IMAGE_DIR)
    return images

def read_label_path():
     labels = load_labels(os.path.join(LABEL_DIR, 'labels.json'))
     return labels





def detect_object():

    create_output_folder()
    image_path = read_image_path()
    label_path = read_label_path()
     
    # Detect objects in each image and save results
    frame_numbers = []
    filenames = []
    num_objects = []

    for frame_number, (filename, img) in enumerate(image_path.items(), start=1):
        class_indices, confidences, bboxes = model.detect(img, confThreshold=0.5)
        num_object = len(class_indices)
        
        frame_numbers.append(frame_number)
        filenames.append(filename)
        num_objects.append(num_object)

        draw_box(img, class_indices, confidences, bboxes, label_path)
        
        # Convert image back to BGR for saving
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        # Save the image to the output folder
        output_path = os.path.join(OUTPUT_DIR, filename)
        cv2.imwrite(output_path, img)
        print(f"Saved processed image to {output_path}")

    # Save object counts to JSON file
    save_object_counts(frame_numbers, filenames, num_objects)







    
   
   
  
