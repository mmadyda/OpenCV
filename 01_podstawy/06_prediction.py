import cv2
import imutils
import numpy as np

import tensorflow as tf

cap = cv2.VideoCapture(0)
model = tf.keras.models.load_model('techni.h5')


while True:
    ret, frame = cap.read()
    resized = np.array(cv2.resize(frame, (256, 256)), dtype='float32')
    resized = resized/255.0
    resized = np.expand_dims(resized,0)

    #print(resized.shape)


    pred = model.predict(resized)[0,0]
    text = ''
    print(f'predict: {pred}')
    if pred > 0.5:
        text = f'Tlo: {pred}'
    else:
        text = f'Marek: {pred}'
    cv2.putText(frame,text,(20,40),cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,0,255),thickness=4)
    cv2.imshow('predict', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break