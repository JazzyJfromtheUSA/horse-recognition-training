import os
import shutil

# this program checks to make sure we do not have any images in "needs_boxing" that should be in "images"
# if there are we move them to where they belong

dataset_directory = "../data/horse_dataset"

# create lists containing all the files in "need_boxing" and "labels"
text_files = sorted(os.listdir(os.path.join(dataset_directory, "labels/1")))
jpg_files = sorted(os.listdir(os.path.join(dataset_directory, "need_boxing/1")))

labels = []
images = []


# remove the file extensions from both lists
for file_name in text_files:
    labels.append(file_name.replace(".txt", ""))

for file_name in jpg_files:
    images.append(file_name.replace(".jpg", ""))

for image_file in images:
    if image_file in labels:
        # we found an image we can move
        current_location = dataset_directory + "/need_boxing/1/" + image_file + ".jpg"
        new_location = dataset_directory + "/images/" + image_file + ".jpg"
        shutil.move(current_location, new_location)

