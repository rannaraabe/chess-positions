import glob
import time
import cv2
import numpy

dataset_list = [f for f in glob.glob("./dataset/original/*.jpeg")]
start_time = time.time()
vr = 10
index = 0

def get_board_from_filename_fen(fen):
    ranks = fen.split('-')
    line = 0
    board = []
    for rank in ranks:
        line_n = 0
        line = []
        for c in rank:
            if c >= '0' and c <= '9':
                line.extend(['e']*(ord(c)-ord('0')))
            else:
                line.append(c)
        board.append(line)
    return board

for i in dataset_list:
    x = 0
    y = 0
    img = cv2.imread(i)
    fen = i.split('/')[-1].split('.jpeg')[0]
    board = get_board_from_filename_fen(fen)
    img = cv2.resize(img, (80,80), interpolation = cv2.INTER_AREA)

    while(y < 80):
        while(x < 80):
            cropped_img = img[y:y+vr, x:x+vr].copy()
            filename = "./dataset/cut/" + str(board[y//vr][x//vr]) + "-" + str(index) + ".jpeg"
            cv2.imwrite(filename, cropped_img)
            x += vr
            index += 1
        x = 0
        y += vr

print("%s seconds" % (time.time() - start_time))
