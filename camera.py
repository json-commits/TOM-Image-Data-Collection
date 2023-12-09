import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from skimage import data, img_as_float, io
from skimage import exposure


import cv2

cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow(f'Camera {1}', frame)

        gamma_value = 1.5
        gamma_corrected = exposure.adjust_gamma(frame, gamma_value)
        cv2.imshow(f'Camera {1} ADJUSTED {gamma_value}', gamma_corrected)

        gamma_value = 2
        gamma_corrected = exposure.adjust_gamma(frame, gamma_value)
        cv2.imshow(f'Camera {1} ADJUSTED {gamma_value}', gamma_corrected)

        gamma_value = 2.5
        gamma_corrected = exposure.adjust_gamma(frame, gamma_value)
        cv2.imshow(f'Camera {1} ADJUSTED {gamma_value}', gamma_corrected)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        break
