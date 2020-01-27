This is the dataset that we want to use to train our model.
This does not contain any code.
This is based on this guide https://towardsdatascience.com/training-yolo-for-object-detection-in-pytorch-with-your-custom-dataset-the-simple-way-1aa6f56cf7d9

Structure of dataset
---root
    --- data
        --- dataset name
            --- images
                --- img1.jpg
                --- img2.jpg
                ..........
            --- labels
                --- img1.txt
                --- img2.txt
                ..........
            --- train.txt
            --- val.txt