import cv2
import numpy as np 
import matplotlib.pyplot as plt 


vid = cv2.VideoCapture('raw_video_feed.mp4')

if (vid.isOpened()==False):
    print("Error opening video")


thresh = 100


while(vid.isOpened()):
    check, frame = vid.read()

    width = int(vid.get(3))

    if check == True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        sum = 0
        n = 0
        center = 0

        for i in range(width):
            pix = gray[225,i]

            if pix < thresh:
                sum = sum + i
                n = n + 1
        
        if n > 0:
            center = sum/n


        cv2.circle(frame, (int(center), 225), 20, (0,0,255), -1)

        cv2.imshow('Frame', frame)

    
        if cv2.waitKey(25) &0xFF == ord('q'):
            break

    else:
        break

vid.release()

cv2.destroyAllWindows()

    