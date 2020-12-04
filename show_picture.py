from __future__ import print_function, division
import os
import torch
import pandas as pd
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

import warnings
warnings.filterwarnings("ignore")

plt.ion() 

def show_picture(image):
    image_set = image.split("_")[0]
    folder = '{}_set'.format(image_set)
    path = 'scratch/{}/{}'.format(folder, folder)
    image_path = io.imread(os.path.join(path, image))
    plt.figure()
    plt.imshow(image_path)
    plt.show()




