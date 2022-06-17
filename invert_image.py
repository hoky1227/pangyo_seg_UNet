import os
from glob import glob
from tqdm import tqdm
from PIL import Image
import numpy as np

path = '/users/hoky1227/pangyo_seg/Pytorch-UNet/data/masks/ct_seg_m_*_mask.gif'
fl = glob(path)


# img = Image.open('/users/hoky1227/pangyo_seg/Pytorch-UNet/data/sample/masks/fff9b3a5373f_16_mask.gif')
# print(np.array(img))

# raise

for f in tqdm(fl):
    img = Image.open(f)
    img = np.array(img)

    # invert 1 to 0
    img[img == 1] = 255
    img[img == 0] = 1
    img[img == 255] = 0


    # save the inverted mask
    img = Image.fromarray(img)
    img.save(f)


    # # Convert image to RGB
    # img = img.convert('RGB')

    # # Save image
    # img.save(f)