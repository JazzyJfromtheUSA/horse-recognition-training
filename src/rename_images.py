# we have a lot of different names for pictures
# this script just gives them numbers or whatever else you fancy

import os

i = 1

need_boxing_dir = "../data/horse_dataset/need_boxing/1/"

for file in os.listdir(need_boxing_dir):
    old_file = need_boxing_dir + file
    new_file = need_boxing_dir + "horse_" + str(i) + ".jpg"
    i += 1

    os.rename(old_file, new_file)
