import cv2
import numpy as np
from pyzbar.pyzbar import decode
from pygame import mixer

#This is my default camera index, but you can change it with whatever your camera index is.
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

#It opens the "database" file for valid QR_Codes
with open('/home/pi/Desktop/ProiectCraciun/ProiectCraciun/listaColinde') as f:
    myDataList = f.read().splitlines()

while True:
    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        mixer.init()
        if myData in myDataList:
            if myData == 'https://www.youtube.com/watch?v=E8gmARGvPlI':
                myOutput = 'Wham! - Last Christmas'
                myColor = (0,255,0)
                mixer.music.load('Wham - Last Christmas.mp3')
            elif myData == 'https://www.youtube.com/watch?v=yXQViqx6GMY':
                myOutput = 'Mariah Carey - All I Want For Christmas Is You'
                myColor = (0,255,0)
                mixer.music.load('Mariah Carey - All I Want For Christmas Is You (Official Video).mp3')
            elif myData == 'https://www.youtube.com/watch?v=SnA52s7qceM':
                myOutput = 'Michael Bublé - Santa Claus Is Coming To Town'
                myColor = (0,255,0)
                mixer.music.load('Michael Bublé - Santa Claus Is Coming To Town [Official Music Video].mp3')
            mixer.music.play()
        else:
            myOutput = 'Cod QR invalid :)'
            myColor = (0, 0, 255)

        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)
        pts2 = barcode.rect
        cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,myColor,2)
    

    cv2.imshow('Result',img)
    cv2.waitKey(1)