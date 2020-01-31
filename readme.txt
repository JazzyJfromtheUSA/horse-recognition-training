This is the dataset that we want to use to train our model.
This is based on this guide https://towardsdatascience.com/training-yolo-for-object-detection-in-pytorch-with-your-custom-dataset-the-simple-way-1aa6f56cf7d9

Structure of dataset (folder names are in quotes)
---root
    --- "data"
        --- "horse_dataset"
            --- "need_boxing" (files that do not have text files containing box info)
                --- "1" (the number of the subfolder represents the class the images belong too ie "standing horse")
            --- "images" (Contains all of the images which have text files containing info)
                --- img1.jpg
                --- img2.jpg
                ..........
            --- "labels" (text files containing info for the images with the same file name)
                --- img1.txt
                --- img2.txt
                ..........
            --- train.txt (contains the file names used for training)
            --- val.txt (contains the file names used for validating)

How to add files to the dataset
1. add any unboxed images into the "need_boxing" folder. Probaby just put it in the "1" subfolder
1.5. You may want to run rename_images.py to give a more consistent name pattern for images
2. Run bbox.py to create text files with box info for images placed in "need_boxing".
3. Once finished boxing, run move_boxed_images.py to move any files you boxed out of "need_boxing" into "images"
4. Run create_list.py to generate a list of training and validating images inside of train.txt and val.txt

Please note: on my machine trying to run the files in VS Code causes errors where as the terminal has not

Sturcture of each data text file - We can change this if we want pretty easily

1. First number is the object class. It shold match the folders that contain the images/txt files
2. Next is x y location of first corner. This is on a scale of 0 - 1. For example if we have a 500 x 500 image ".5 .5" corresponds to (250,250)
3. Next you have two more numbers that represent the length in the x or y direction from 0 - 1
