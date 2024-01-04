import cv2
import numpy as np

image_path='image.jpg'
min_confidence=0.2 

classes = []

net=cv2.dnn.readNet('yolov3.weights','yolov3.cfg')
