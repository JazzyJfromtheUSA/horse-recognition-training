# One element of the horse data set contains:
#   JPG/PNG file containing the horse pictures
#   JPG/PNG file containing the mask/outline of the horse
#   Text file containg info such as the file name, image resolution, and coordinates of the box surrounding the horse

import os
import numpy as np
import torch
from PIL import Image

# Class to load and contain data for each element in the data set
class Horse_Dataset:
    def __init__(self, dataset_directory, transforms):
        self.dataset_directory = dataset_directory
        self.transforms = transforms
