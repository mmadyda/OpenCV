import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
FPS = int(cap.get(cv2.CAP_PROP_FPS))

print(f'width {width} height: {height}, FPS = {FPS}')

## callback function
def draw_rectangle(event, x, y, flags, param):
    global pt1, pt2, clicked, up
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked = True
        pt1=(x,y)
    elif event == cv2.EVENT_LBUTTONUP:
        up=True
    elif event == cv2.EVENT_MOUSEMOVE and clicked:
        pt2 = (x, y)
    elif clicked and up:
        clicked = False
        up = False




## global variables
pt1 = (0, 0)
pt2 = (0, 0)

clicked = False
up = False


## connect to callbacks

cv2.namedWindow('Test')
cv2.setMouseCallback('Test',draw_rectangle)
while True:

    ret, frame = cap.read()
    ##draving on frame
    if clicked:
        cv2.rectangle(frame, pt1, pt2, (0,0,255),3)


    if up:
        img = frame[pt1[1]: pt2[1], pt1[0]:pt2[0], :]
        if img.shape[0] >0 and img.shape[1] >0:
            cv2.imshow('wycinek', img)
    cv2.imshow('Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()