import os
from glob import glob
from tqdm import tqdm
from PIL import Image
import numpy as np

# 3285 was not correct image

path = '/users/hoky1227/pangyo_seg/Pytorch-UNet/data/masks/*'
fl = glob(path)

# shp = (1080, 1920, 3)
shp = (1080, 1920)

for f in tqdm(fl):
    img = Image.open(f)
    img = np.array(img)
    # print(img.shape)

    if img.shape != shp:
        print(f)
    # print(img.shape != shp)
    # raise