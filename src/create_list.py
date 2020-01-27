# Program to split our pictures into training and validation lists
# Provided from https://github.com/cfotache/pytorch_custom_yolo_training/blob/master/createlist.py

import glob
import os
import numpy as np
import sys

current_dir = "../data/horse_dataset/images"
split_pct = 10
file_train = open("../data/horse_dataset/train.txt", "w")
file_val = open("../data/horse_dataset/val.txt", "w")
counter = 1
index_test = round(100 / split_pct)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        file_val.write(current_dir + "/" + title + ".jpg" + "\n")
    else:
        file_train.write(current_dir + "/" + title + ".jpg" + "\n")
        counter = counter + 1
file_train.close()
file_val.close()
