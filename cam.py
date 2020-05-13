import numpy as np
import cv2

captura = cv2.VideoCapture(0) 
while(1):
    ret, frame = captura.read()
 
    (b, g, r) = frame[200, 200]
    frame[198:202, 198:202] = (0, 0, 255)
    frame[15:90, 15:90] = (b, g, r)
    azull = (b, g, r)
    azul = azull[:3]
    # print(azull[:3])
    cv2.line(frame, (0, 0), (1280, 720), azul)
    cv2.imshow('frame',frame)
   
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
 
captura.release()
cv2.destroyAllWindows()