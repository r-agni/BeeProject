# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 15:03:44 2022

@author: agni_
"""

import cv2 as cv
video=cv.VideoCapture('bee1short.mp4')

fgbg= cv.createBackgroundSubtractorKNN(500,400,False) #(history, distthreahold, shadows)

while True:
    ret, frame = video.read()
    if frame is None:
        print('Doesnt Recognize File Path')
        break
    
    #applying background subtraction
    fgmask = fgbg.apply(frame)
    #fgmask= cv.GaussianBlur(fgmask, (5, 5), 0)

    #finding area after removing background
    contours, _= cv.findContours(fgmask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    totalarea=0
    for contour in contours:
      area = cv.contourArea(contour)
      if area>1100:
        cv.drawContours(frame, contour, -1, (250, 0, 0), 3)
        totalarea+=area
    BeeCount= totalarea/40000

    #shows frame number in original video
    cv.rectangle(frame, (10, 2), (200,20), (255,255,255), -1)
    #cv.putText(frame, "Frame:"+str(video.get(cv.CAP_PROP_POS_FRAMES)),(15, 15),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))
    cv.putText(frame, "Bee Count:"+str(int(BeeCount)),(15, 15),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))
    
    #cv.imshow('frame',frame)
    cv.imshow('mask',fgmask)

    #press key q to 
    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
  