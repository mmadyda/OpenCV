import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
FPS = int(cap.get(cv2.CAP_PROP_FPS))

print(f'width {width} height: {height}, FPS = {FPS}')

## callback function
def draw_rectangle(event, x, y, flags, param):
    global pt1, pt2, clicked, up, zmiana
    if event == cv2.EVENT_LBUTTONDOWN:
        up = False
        zmiana = True
        clicked = True
        pt1=(x,y)
    elif event == cv2.EVENT_LBUTTONUP:
        up=True
        clicked = False
    elif event == cv2.EVENT_MOUSEMOVE and clicked and not up:
        pt2 = (x, y)


metody_porownania = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF',  'cv2.TM_SQDIFF_NORMED']

## global variables
pt1 = (0, 0)
pt2 = (0, 0)

clicked = False
up = False
zmiana = False
wycinek = None

## connect to callbacks

cv2.namedWindow('Test')
cv2.setMouseCallback('Test',draw_rectangle)
while True:
    ret, frame = cap.read()
    #frame = cv2.resize(frame, (int(frame.shape[1]*2), int(frame.shape[0]*2)))
    ##draving on frame
    if clicked:
        cv2.rectangle(frame, pt1, pt2, (0,0,255),3)


    if up and zmiana:
        wycinek = frame[pt1[1]: pt2[1], pt1[0]:pt2[0], :]
        if wycinek.shape[0] >0 and wycinek.shape[1] >0:
            cv2.imshow('wycinek', wycinek)
        else: wycinek = None
        zmiana = False


    if wycinek is not None:
        porownanie = cv2.matchTemplate(frame, wycinek, cv2.TM_CCOEFF_NORMED)
        cv2.imshow('mapa porownania', porownanie)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(porownanie)
        height, width, channels = wycinek.shape

        # if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        #     top_left = min_loc
        # else:
        #     top_left = max_loc

        top_left = max_loc
        bottom_right = (top_left[0]+width, top_left[1]+height)
        if max_val > 0.6:
            cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 7)
        print(f'min_val: {min_val}, max_val: {max_val}, min_loc: {min_loc}, max_loc: {max_loc}')

    cv2.imshow('Test', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()