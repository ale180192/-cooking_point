import numpy as np
import cv2
import matplotlib
import pylab as pl

def Filtro_g (im,coef):
	[y,x]=im.shape
	im_g= np.zeros([y,x])
	for j in range(1, y-1):   
		for i in range(1, x-1):   
			suma=0
			for jj in range(5):   
				for ii in range(5):   
					indiceA=j+jj-1
    
					indiceB=i+ii-1
    
 
					suma=im[indiceA,indiceB]*coef[jj,ii]+suma 
			im_g[j,i]=suma
	return im_g



def Filtro (im,coef):
	[y,x]=im.shape
	im2= np.zeros([y,x])
	for j in range(1, y-1):   
		for i in range(1, x-1):   
			suma=0
			for jj in range(3):   
				for ii in range(3):   
					indiceA=j+jj-1
    
					indiceB=i+ii-1
    
 
					suma=im[indiceA,indiceB]*coef[jj,ii]+suma 
			im2[j,i]=suma
	return im2
	
	
	
def Hist (im):
	#Calculo de histograma
	[y,x]= im.shape

	histo=np.zeros(256)


	for (j) in range(y):
		for (i) in range(x): 
			indice= im[j,i]
			histo[indice]=histo[indice]+1
		
	return histo	
		
def ecu (im, a, histo ):
	[y,x]= im.shape
	suma=0
	a=np.zeros(256)
	for i in range(256):
		suma=suma+histo[i]
		a[i]=round(255/(x*y)*suma)

#aplicacion de la ecualizacion
	for (j) in range(y):
		for (i) in range(x): 
			im[j,i]= a[im[j,i]]
			

def max(im):
	[y,x]= im.shape

	tmp=0


	for (j) in range(y):
		for (i) in range(x): 
			if tmp < im[j,i]:
				tmp=im[j,i]
				
	return tmp
	
def min (im):
	[y,x]= im.shape

	tmp=2e6


	for (j) in range(y):
		for (i) in range(x): 
			if tmp > im[j,i]:
				tmp=im[j,i]
				
	return tmp
	
def binarizan(im, umbral):
	[y,x]= im.shape

	tmp=np.zeros([y,x], np.uint8)
	


	for (j) in range(y):
		for (i) in range(x): 
			if umbral < im[j,i]:
				tmp[j,i]= 255
	
				
	return (tmp)
 
def binarizab(im, umbral):
	[y,x]= im.shape

	tmp=np.zeros([y,x], np.uint8)
	


	for (j) in range(y):
		for (i) in range(x): 
			if umbral > im[j,i]:
				tmp[j,i]= 255
	
				
	return (tmp)
 
def erosion (im):
	erosion = cv2.erode(imfin3,kernel,iterations = 1)
	cv2.imshow('EROSION', erosion)
	return (erosion)

def dilatacion (im):
	dilatacion = cv2.dilate(im,kernel,iterations = 1)
	cv2.imshow('DILATACION', dilatacion)
	return (dilatacion)