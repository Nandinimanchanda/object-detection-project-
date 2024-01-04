import cv2
import numpy as np

image_path='image.jpg'
min_confidence=0.2 

classes = ["person",
"bicycle","car","motorbike","aeroplane","bus","train","truck","boat","traffic light","fire","hydrant","stop sign","parking meter","bench","bird","cat","dog","horse","sheep","cow","elephant","bear","zebra","giraffe","backpack","umbrella","handbag","tie","suitcase","frisbee","skis","snowboard","sports ball","kite","baseball bat","baseball glove","skateboard","surfboard","tennis racket","bottle","wine glass","cup","fork","knife","spoon","bowl","banana","apple","sandwich","orange","broccoli","carrot",
"hot dog","pizza","donut","cake","chair","sofa","pottedplant","bed","dining table","toilet","tvmonitor","laptop","mouse","remote","keyboard","cell phone","microwave","oven","toaster","sink","refrigerator","book","clock","vase","scissors","teddy bear","hair drier","toothbrush"]

np.random.seed(54321)
colors=np.random.uniform(0,255, size=(len(classes),3))


net=cv2.dnn.readNet('yolov3.weights','yolov3.cfg')

image=cv2.imread(image_path)
height, width = image.shape[0], image.shape[1]
nlob= cv2.dnn.blobFromImage(cv2.resize(image, (300,300)), 0.007, (300,300), 130)

net.setInput(blob)
detected_objects = net.forward()

for i in range(detected_objects.shape[2])
    confidence= detected_objects[0][0][i][2]
    if confidence> min_confidence:
        class_index = int(detected_objects[0,0,i,1])
        upper_left_x = int(detected_objects[0,0,i,3]*width)
        upper_left_y = int(detected_objects[0,0,i,4]*height)
        lower_left_x = int(detected_objects[0,0,i,5]*width)
        lower_left_x = int(detected_objects[0,0,i,6]*height)

        prediction_text= f"{classes[class_index]}: {confidence:.2f}%"


        cv2.rectangle(image,(upper_left_x,upper_left_y),(lower_left_x,lower_left_y),colors[class_index],3]
        cv2.putText(image, prediction_text,(uper_left_x,uper_left_y-15 ifupper_left_y>30 else upper_left_y+15),cv2.FONT_HERSHEY_SIMPLEX,0.6, colors[class_index],2)

    cv2.imshow("Detected Objects", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




