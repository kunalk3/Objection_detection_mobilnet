import cv2
import numpy as np

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow",
            "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

prototxt="ssd/MobileNetSSD_deploy.prototxt.txt"
model ="ssd/MobileNetSSD_deploy.caffemodel"

def detect_object(path, filename):    
    COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
    net = cv2.dnn.readNetFromCaffe(prototxt, model)
    image = cv2.imread(path)
    image = cv2.resize(image,(480,360))
    (h, w) = image.shape[:2]
    
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.60:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # Display the prediction
            label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
            cv2.rectangle(image, (startX, startY), (endX, endY),
                COLORS[idx], 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(image, label, (startX, y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

    return image # cv2.imwrite(f"{DOWNLOAD_FOLDER}{filename}",image)
