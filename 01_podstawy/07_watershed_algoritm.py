import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

road = cv2.imread('img/water.jpg')
road_copy = np.copy(road)

print(road.shape[:2])

marker_image = np.zeros(road.shape[:2],dtype=np.int32)
segments = np.zeros(road.shape, dtype=np.uint8)
print(segments.shape)

print(cm.tab10(0))

def create_rgb(i):
    return tuple(np.array(cm.tab10(i)[:3])*255)

colors = []

for i in range(10):
    colors.append(create_rgb(i))

print(colors)

#GLOBAL VARIABLES
n_markers = 10
current_marker = 1
marks_updated = False
#CALLBACK FUNCTION
def mouse_callback(event,x,y,flags,param):
    global marks_updated, current_marker

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(marker_image,(x, y),10,(current_marker),-1)

        cv2.circle(road_copy,(x,y), 10,colors[current_marker],-1)

        marks_updated = True

#WHILE TRUE

cv2.namedWindow('img')
cv2.setMouseCallback('img',mouse_callback)
while True:
    cv2.imshow('segmenty', segments)
    cv2.imshow('img', road_copy)

    k = cv2.waitKey(1)
    if k ==27:
        break

    #czyszczenie przy przycisku C
    elif k == ord('c'):
        road_copy = road.copy()
        marker_image = np.zeros(road.shape[:2],dtype=np.int32)
        segments = np.zeros(road.shape, dtype = np.uint8)


    #UPDATE COLOR
    elif k > 0 and chr(k).isdigit():
        current_marker = int(chr(k))

    if marks_updated:
        marker_image_copy = marker_image.copy()
        cv2.watershed(road,marker_image_copy)

        segments = np.zeros(road.shape, dtype=np.uint8)

        for color_ind in range(n_markers):
            segments[marker_image_copy ==(color_ind)] = colors[color_ind]

cv2.destroyAllWindows()


