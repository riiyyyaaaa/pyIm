import cv2
print (cv2.__version__)

im = cv2.imread("./image.jpg")

print(type(im))

print(im.shape)

print(im.dtype)