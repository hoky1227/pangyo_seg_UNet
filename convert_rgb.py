import os
from glob import glob
from tqdm import tqdm
from PIL import Image

path = '/users/hoky1227/pangyo_seg/Pytorch-UNet/data/masks/ct_seg_m_*_mask.gif'
fl = glob(path)

for f in tqdm(fl):
    img = Image.open(f)

    # Convert image to RGB
    img = img.convert('RGB')

    # Save image
    img.save(f)
