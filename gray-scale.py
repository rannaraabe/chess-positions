import cv2
import numpy as np
import time
import glob
import csv
import skimage
from skimage.feature import hog
from skimage import data, exposure

column_names_gray = []
cont = 0
for i in range(0,100):
  column_names_gray.append("att"+str(cont))
  cont+=1

sliced_data_gray = [f for f in glob.glob("./dataset/images/*.jpeg")]
start_time = time.time()

with open('./dataset/dataset_gray.csv', mode='w') as data_csv:
  data_writer = csv.writer(data_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  print(len(sliced_data_gray))
  data_writer.writerow(column_names_gray)

  for i in sliced_data_gray:
    sliced_im = cv2.imread(i, 0)
    features = np.reshape(sliced_im, (10*10))
    data_writer.writerow(features)

print("%.2fs seconds" % (time.time() - start_time))