import cv2
import numpy as np

class ObjectDetector:
    def __init__(self, class_labels):
        self.class_labels = class_labels
        self.model = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')
        self.layer_names = self.model.getLayerNames()
        self.output_layers = [self.layer_names[i[0] - 1] for i in self.model.getUnconnectedOutLayers()]

    def detect_objects(self, image):
        height, width, channels = image.shape

        # Detecting objects
        blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.model.setInput(blob)
        outs = self.model.forward(self.output_layers)

        # Showing detected objects
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Non-maximum suppression
        indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        for i in indices:
            i = i[0]
            x, y, w, h = boxes[i]
            label = str(self.class_labels[class_ids[i]])
            confidence = str(round(confidences[i], 2))
            color = (0, 255, 0)
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            cv2.putText(image, label + " " + confidence, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        return image

def main():
    # Load names of classes
    with open('coco.names', 'r') as f:
        class_labels = [line.strip() for line in f.readlines()]

    # Create an object detector
    object_detector = ObjectDetector(class_labels)

    # Load the video
    video = cv2.VideoCapture('input.mp4')

    # Perform real-time object detection
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        frame = object_detector.detect_objects(frame)

        # Show the video
        cv2.imshow('Real-Time Object Detection', frame)

        # Exit if the user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()