import cv2
import numpy as np
import time
import glob
import csv
import skimage
from skimage.feature import hog
from skimage import data, exposure

column_names = []
cont = 0

for i in range(0,100):
  column_names.append("att"+str(cont))
  cont += 1
print(column_names)

sliced_data = [f for f in glob.glob("./dataset/images/*.jpeg")]
start_time = time.time()

with open('./dataset/dataset_mean.csv', mode='w') as data_csv:
  data_writer = csv.writer(data_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  print(len(sliced_data))
  data_writer.writerow(column_names)

  for i in sliced_data:
    sliced_im = cv2.imread(i)
    feature_matrix = np.zeros((10,10)) 
    for i in range(0,sliced_im.shape[0]):
      for j in range(0,sliced_im.shape[1]):
          feature_matrix[i][j] = ((int(sliced_im[i,j,0]) + int(sliced_im[i,j,1]) + int(sliced_im[i,j,2]))/3)
    features = np.reshape(feature_matrix, (10*10))
    data_writer.writerow(features)

print("%.2fs seconds" % (time.time() - start_time))