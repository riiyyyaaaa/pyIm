import cv2, matplotlib
import numpy as numpy
import matplotlib.pyplot as plt

img = cv2.imread("./image.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

print(img)
# print(gray_img)

plt.imshow(gray_img)
plt.show()

plt.imshow(img)
plt.show()