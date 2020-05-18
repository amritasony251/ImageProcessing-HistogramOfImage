import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image

img = cv2.imread("img6.bmp")
width, height, bit = np.shape(img)
print(width)
print(height)
print(bit) 

#print (img[600][700])
x = np.linspace(0,255,256)

hist_plot = [0]*256
print(hist_plot)

size = width*height
for i in range(0, width):
   for j in range(0, height) :
      temp = img[i][j][0]
      hist_plot[temp] = hist_plot[temp] + 1

hist = [0]*256      
for l in range(0, 256):
    hist[l] = float(hist_plot[l])/float(size)   

plt.bar(x, hist) 
plt.show()   
print(hist_plot)      
      
