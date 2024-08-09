import cv2

# Draw bounding boxes on the image
def draw_box(img, class_indices, confidences, bboxes, labels):
    font_scale = 1
    font = cv2.FONT_HERSHEY_PLAIN
    for class_index, conf, box in zip(class_indices.flatten(), confidences.flatten(), bboxes):
        cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), (255, 0, 0), 2)
        cv2.putText(img, labels[class_index - 1], (box[0] + 10, box[1] + 40), font, fontScale=font_scale, color=(0, 255, 0), thickness=2)