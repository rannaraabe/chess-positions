import cv2
import numpy as np
import time
import glob
import csv
import skimage
from skimage.feature import hog
from skimage import data, exposure

sliced_data = [f for f in glob.glob("./dataset/images/*.jpeg")]
start_time = time.time()

with open('./dataset/dataset_hog.csv', mode='w') as data_csv:
  data_writer = csv.writer(data_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

  for i in sliced_data:
    sliced_im = cv2.imread(i)
    out, hog_image = hog(sliced_im, orientations=8, pixels_per_cell=(10, 10),
                    cells_per_block=(1, 1),feature_vector=True, visualize=True)
    data_writer.writerow(out)

print("%.2fs seconds" % (time.time() - start_time))
