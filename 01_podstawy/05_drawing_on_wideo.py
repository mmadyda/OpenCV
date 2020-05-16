import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
FPS = int(cap.get(cv2.CAP_PROP_FPS))

print(f'width {width} height: {height}, FPS = {FPS}')

## callback function
def draw_rectangle(event, x, y, flags, param):
    global pt1, pt2, topLeft_clicked, botRight_clicked

    if event == cv2.EVENT_LBUTTONDOWN:

        if topLeft_clicked and botRight_clicked:
            pt1 = (0, 0)
            pt2 = (0, 0)
            topLeft_clicked = False
            botRight_clicked = False

        if topLeft_clicked == False:
            pt1 = (x, y)
            topLeft_clicked = True
        elif botRight_clicked == False:
            pt2 = (x, y)
            botRight_clicked = True

## global variables
pt1 = (0, 0)
pt2 = (0, 0)

topLeft_clicked = False
botRight_clicked = False
## connect to callbacks

cv2.namedWindow('Test')
cv2.setMouseCallback('Test',draw_rectangle)
while True:

    ret, frame = cap.read()
    ##draving on frame
    if topLeft_clicked == True:
        cv2.circle(frame,center=pt1, radius=5,color=(0,0,255), thickness=-1)
    if topLeft_clicked and botRight_clicked:
        cv2.rectangle(frame, pt1, pt2, (0,0,255),3)

    cv2.imshow('Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()