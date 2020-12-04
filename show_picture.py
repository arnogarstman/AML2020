import os
import pandas as pd
from skimage import io, transform
import matplotlib.pyplot as plt

plt.ion() 

def show_picture(image):
    image_set = image.split("_")[0]
    folder = '{}_set'.format(image_set)
    path = 'scratch/{}/{}'.format(folder, folder)
    image_path = io.imread(os.path.join(path, image))
    plt.figure()
    plt.imshow(image_path)
    plt.show()




