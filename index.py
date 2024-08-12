import cv2
import numpy as np
from pyzbar.pyzbar import decode
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,640)
while True:
    success,img =cap.read()

    code=decode(img)
    for qrcode in code:
        text=qrcode.data.decode('utf-8')
        pt=np.array([qrcode.polygon],np.int32)
        rectpoints=qrcode.rect
        cv2.polylines(img,[pt],True,(0,255,0),4)
        cv2.putText(img,text,(rectpoints[0],rectpoints[1]),cv2.FONT_HERSHEY_PLAIN,0.9,(0,0,0),1)
        print(text)
        
    cv2.imshow('Result image',img)
    cv2.waitKey(2)