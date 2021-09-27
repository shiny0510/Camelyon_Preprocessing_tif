#%%
import os
from openslide import OpenSlide
import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt
from pytictoc import TicToc

t = TicToc()

print("image dim read")

t.tic()
img1 = OpenSlide('/data/camel/training/evaluation_masks/tumor_002_mask.tif')
img2 = OpenSlide('/data/camel/training/tumor/tumor_002.tif')


size0= img1.level_dimensions

print(img1.level_dimensions)
t.toc()

print("image initial")
t.tic()
image1 = np.asarray(img1.get_thumbnail(size0[3]))
image2 = np.asarray(img2.get_thumbnail(size0[3]))

pil_image = Image.fromarray(image2)
pil_image.save('./test_origin.jpg')
#gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY) #로고파일의 색상을 그레이로 변경
#ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY) #배경은 흰색으로, 그림을 검정색으로 변경
#cv2.imshow('mask',mask) #배경 흰색, 로고 검정

image2[np.where(image1[:,:,1]>0)] = [255,17,0]

t.toc()

print(image1.shape)
print(image1)
#image = Image.open('/data/camel/testing/evaluation/evaluation_masks/tumor_005_evaluation_mask.png')

print("show image")
t.tic()
plt.imshow(image2)
plt.show()
t.toc()

pil_image = Image.fromarray(image2)
pil_image.save('./test.jpg')
#%%
'''
image = np.asarray(img.get_thumbnail(size3))
image2 = np.asarray(img.get_thumbnail(size0))

img = 0

ret, binary = cv2.threshold(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), 150, 255, cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(~binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
x, y, w, h = cv2.boundingRect(contours[0])
cv2.rectangle(cv2.drawContours(image.copy(), contours, 0, (255, 0, 255), 3), (x, y), (x + w, y + h), (255, 0, 0), 5)
count = 0
image = 0
'''