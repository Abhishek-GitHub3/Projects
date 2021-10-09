import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
im = cv2.imread(r'C:\Users\abhis\Desktop\Python\Object Detection\Assets\itemsNew.jpeg')
bbox, label, conf = cv.detect_common_objects(im)
output_image = draw_bbox(im, bbox, label, conf)
print("Contents in the picture given are: ")
uniqueLabel = []
for i in label:
    if i not in uniqueLabel:
        uniqueLabel.append(i)
for i in uniqueLabel:
    print(i)
plt.imshow(output_image)
plt.show()
