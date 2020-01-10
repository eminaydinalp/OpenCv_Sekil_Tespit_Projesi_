# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 00:42:59 2020

@author: Emin
"""

import cv2
import numpy as np

font = cv2.FONT_HERSHEY_COMPLEX


resim     = cv2.imread('resim2.jpg')
resimGrey = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
_, thrash = cv2.threshold(resimGrey, 240, 255, cv2.THRESH_BINARY) # Eşik değer ayarı 
_, contours, _  = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #Şekillerin sınırları bulundu


#cv2.imshow("resim1", thrash)
cv2.imshow("resim", resim)
for contour in contours:
    
    approx = cv2.approxPolyDP(contour,0.03* cv2.arcLength(contour, True), True) #Gürültüyü kaldırmak için hatları yaklaştırıyoruz. 
    """0.03 değerini deneyerek buluyoruz şekilden şekle değişebilir."""
    cv2.drawContours(resim, [approx], 0, (0, 0, 0), 5) # Ana resim üzerindeki tespit edilen şekiller çizildi
    x = approx.ravel()[0]  # Şekillerin üzerine yazacağımız isimler için koordinat belirliyoruz.
    y = approx.ravel()[1] - 5
    if len(approx) == 3:
        cv2.putText(resim, "Ucken", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        x1 ,y1, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
          cv2.putText(resim, "Kare", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
        else:
          cv2.putText(resim, "Dortgen", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 5:
        cv2.putText(resim, "Besgen", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 10:
        cv2.putText(resim, "Yizldiz", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:
        cv2.putText(resim, "Cember", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))


cv2.imshow("Son Hal", resim) # Ana resmi şekilleri tespit edilmiş şekilde gösteriyoruz.
cv2.waitKey(0)
cv2.destroyAllWindows()


        






