import glob
import time
import cv2
import numpy

dataset_list = [f for f in glob.glob("./dataset/original/*.jpeg")]
start_time = time.time()
vr = 10
index = 0

for i in dataset_list:
  x = 0
  y = 0
  img = cv2.imread(i)
  img = cv2.resize(img, (80,80), interpolation = cv2.INTER_AREA)
  while(y < 80):
    while(x < 80):
      cropped_img = img[y:y+vr, x:x+vr].copy()
      filename = "./dataset/images/" + str(index) + ".jpeg"
      cv2.imwrite(filename, cropped_img)
      x += vr
      index += 1
    x = 0
    y += vr

print("%s seconds" % (time.time() - start_time))
