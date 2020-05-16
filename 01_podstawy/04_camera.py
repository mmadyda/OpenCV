import cv2

cap  = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(f'width: {width} height: {height} frame count: {frame_count}')

writer = cv2.VideoWriter('MOJE_WIDEO.mp4',cv2.VideoWriter_fourcc(*'XVID'),20,(width, height))
while True:

    ret, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    writer.write(frame)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.relase()
cv2.destroyAllWindows()

