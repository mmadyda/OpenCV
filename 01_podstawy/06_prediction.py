import cv2
import imutils
import numpy as np

import tensorflow as tf

cap = cv2.VideoCapture(0)
model = tf.keras.models.load_model('techni.h5')


while True:
    ret, frame = cap.read()

    pred = model.predict
    print(f'predict: {pred}')
    cv2.imshow('predict', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break