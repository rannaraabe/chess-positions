import glob
import time
import cv2
import numpy
# from google.colab.patches import cv2_imshow

dataset_list = [f for f in glob.glob("/home/rannaraabe/test/*.jpeg")]
start_time = time.time()
vr = 50
index = 0

for i in dataset_list:
    x = 0
    y = 0
    img = cv2.imread(i)
    while(y < 400):
      while(x < 400):
        cropped_img = img[y:y+vr, x:x+vr].copy()
        filename = "./dataset/r" + str(index) + ".jpeg"
        cv2.imwrite(filename, cropped_img)
        x += vr
        index += 1
      x = 0
      y += vr
    print("imagem " + i + " ok")

print("%s seconds" % (time.time() - start_time))
