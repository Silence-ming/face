import numpy as np
import cv2
def distance(one,two):
    return np.sqrt(np.sum((np.power((one-two),2))))
img=cv2.imread('a.jpg')
w=img.shape[1]
h=img.shape[0]
myImg=np.zeros([h,w,3],np.int8)
black=np.array([0,0,0]);
white=np.array([255,255,255]);
grey=np.array([125,125,125]);
for y in range(0,h-1):
    for x in range(0,w-1):
         current=img[y,x,:]
         right=img[y,x+1,:]
         down=img[y+1,x,:]
         if distance(current,right)>20 and distance (current,down)>20:
             myImg[y, x, :] = black
         elif distance(current,right)<20 and distance (current,down)<20:
             myImg[y, x, :] = grey
         else:
             myImg[y, x, :] = white
cv2.imwrite('new.jpg',myImg)
cv2.destroyAllWindows()