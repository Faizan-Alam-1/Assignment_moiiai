
import os
import cv2


# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Configuration directories
CONFIG_DIR = os.path.join(BASE_DIR, 'config')
MODEL_DIR = os.path.join(BASE_DIR,  'model')
LABEL_DIR = os.path.join(BASE_DIR, 'coco_dataset_label')
IMAGE_DIR = os.path.join(BASE_DIR, '../images')
OUTPUT_DIR = os.path.join(BASE_DIR, '../output_images')
OUTPUT_JSON = os.path.join(BASE_DIR, '../')

# Configuration files
config_file = os.path.join(CONFIG_DIR, 'ssd_config.pbtxt')
frozen_model = os.path.join(MODEL_DIR, 'frozen_model.pb')

# Load the model
model = cv2.dnn_DetectionModel(frozen_model, config_file)
model.setInputSize(320, 320)
model.setInputScale(1.0 / 127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)