import os

prefix = 'nada_'

for file in os.listdir("./dataset/images/"):
    filename = prefix+file
    os.rename("./dataset/images/"+file, "./dataset/images/"+filename)
    print(file)
