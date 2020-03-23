import os
import numpy as np
import biblio
import cv2
import pylab as pl
from matplotlib import pyplot as plt
import math





#--------------------------Lectura------------------------------------------------------------------------------------
imge = cv2.imread("10_DC_1667.jpg")
#imge = cv2.imread("IR_1684.jpg")
#imge = cv2.imread("IR_1670.jpg")
img = imge[453:1169, 513:1465]
cv2.imshow('Corte',img)
#img = imge[405:1211, 598:1435]
img= cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
a=img

h,s,v = cv2.split(a)
#a=crop_img
#b,g,r = cv2.split(a)

img=s
#img1=h
#img2=v
#crop_img = img[405:1211, 598:1435]
#crop_img1 = img1[405:1211, 598:1435]
#crop_img2= img2[405:1211, 598:1435]
im=img
#img1=crop_img1
#img2=crop_img2

#im=biblio.Hist(img)
cv2.imshow('Canal S',im)
cv2.imshow('original',imge)
 
hist,bins = np.histogram(im.flatten(),256,[0,256])
#Genera la función de distribución acumulada (cdf por sus siglas en inglés)
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
#Genera los gráficos del histograma y de la función de distribución acumulada
plt.plot(cdf_normalized, color = 'b')
plt.hist(im.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histograma'), loc = 'upper right')
#plt.show()

#Enmascara los valores iguales a cero
cdf_m = np.ma.masked_equal(cdf,0) 
#Aplica la transformación de ecualización
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
#Rellena los valores previamente enmascarados con ceros
cdf = np.ma.filled(cdf_m,0).astype('uint8')
#Aplica la ecualización a los píxeles de la imagen original
img2 = cdf[im]
#Grafica la imagen resultante de aplicar la ecualización del histograma
#cv2.imshow('ECUALIZACION',img2)



img=biblio.binarizan(img2,155)
cv2.imshow('Binarizacion',img)

kernel = np.ones((3,3),np.uint8)
bordes = cv2.erode(img,kernel,iterations = 3)
cv2.imshow('EROSION', bordes)
kernel = np.ones((3,3),np.uint8)
bordes= cv2.dilate(bordes ,kernel,iterations =2 )
cv2.imshow('DILATACION', bordes)




bordes = cv2.Canny(bordes,60,100 )
cv2.imshow('BORDES', bordes)

contours ,_ = cv2.findContours(bordes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(bordes, contours, -1, (0,0,255), 0, cv2.LINE_AA)



p=0
for c in contours:
	area= cv2.contourArea(c)
	if area > 8000 and area < 140000:
		p=p+1
		x,y,n,m = cv2.boundingRect(c)
		cv2.rectangle(img , (x,y), (x+n,y+m), (0,255,0), 2)
		cv2.imwrite(os.path.dirname(__file__) + 'im_{number}.png'.format_map({'number': p}), im[y:y+m,x:x+n])
cv2.imshow("cropped", im)



hist,bins = np.histogram(img2.flatten(),256,[0,256])
#Genera la función de distribución acumulada (cdf por sus siglas en inglés)
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
#Genera los gráficos del histograma y de la función de distribución acumulada
plt.plot(cdf_normalized, color = 'b')
plt.hist(img2.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histograma'), loc = 'upper right')
#plt.show()



cv2.waitKey(0)
cv2.destroyAllWindows()



#cv2.imshow('Histograma',im)
#cv2.imshow('Canal H',img1)
#cv2.imshow('Canal V',img2)
