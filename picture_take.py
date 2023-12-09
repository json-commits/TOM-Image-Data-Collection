import cv2

cap = cv2.VideoCapture(1)

#take a picture and save it
ret, frame = cap.read()
cv2.imwrite('id_lace.jpg', frame)

#release the camera
cap.release()

#show the picture
img = cv2.imread('id_lace.jpg')
cv2.imshow('tomato', img)
cv2.waitKey(0)