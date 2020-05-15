import cv2
import numpy as np

# VARIABLES

drawing = False
ix, iy = -1, -1
img = np.zeros((512, 512, 3))
copy_img = img.copy()

# FUNCTION

def draw_rectangle(event, x, y ,flags, params):
    global ix, iy, drawing, img, copy_img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        copy_img = img.copy()
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img = copy_img.copy()
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), thickness = 3)
            #img = copy_img.copy()
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        img = copy_img.copy()
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), thickness = 3)


# SHOWING THE IMAGE




cv2.namedWindow(winname='rysunek')
cv2.setMouseCallback('rysunek',draw_rectangle)

while True:
    cv2.imshow('rysunek', img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()