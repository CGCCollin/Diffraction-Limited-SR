import numpy as np
import pandas as pd
import tifffile
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import torch
from datetime import datetime
from scipy.signal import convolve2d
import cv2


class ImgTransform():
    def __init__(self, name):
        self.name = name
    # change the brightness by a scaling value
    # shift the image by a specified angle

    def transformation(self, img, bright_shift=0, rot=0):
        img *= bright_shift
        rot_matrix = cv2.getRotationMatrix2D(
            (len(img/2), len(img[0])/2), rot, 1)
        img = cv2.warpAffine(img, rot_matrix, img.shape)
        return img


class VFlip(ImgTransform):
    def __init__(self, name):
        super(VFlip, self).__init__(name)

    def transformation(self, img, bright_shift=0, rot=0):
        img = np.flipud(img)
        img = super(VFlip, self).transformation(img, bright_shift, rot)
        return img


flip_transform = VFlip("vflip")

img = tifffile.imread(r"dset\CCPs\cell1\WF_raw.tif")
img = img.astype('uint32')
img = img.mean(axis=0)
transform = flip_transform.transformation(np.copy(img), 1.2, 25)
norm = mpl.colors.LogNorm(img.min(), img.max())
fig, axes = plt.subplots(1, 2, figsize=(15, 6))
axes[0].imshow(img, cmap='grey', norm=norm)
axes[0].set_title("og mean")
axes[1].imshow(transform, cmap='grey', norm=norm)
axes[1].set_title("Transformation")
plt.show()
