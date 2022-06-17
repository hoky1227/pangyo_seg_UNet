import PIL.Image as Image
import numpy as np
import cv2
from glob import glob
from tqdm import tqdm

path = '/users/hoky1227/pangyo_seg/mid_resolution/masks_unfilled/ct_seg_m_*_mask.gif'

fl = glob(path)

for f in tqdm(fl):
    img = Image.open(f)

    img = np.array(img)

    # find all the contours
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # fill the contour of the mask
    cv2.drawContours(img, contours, -1, (255, 255, 255), -1)

    # save the filled mask using Image
    img = Image.fromarray(img)
    img.save(f.replace('_unfilled', ''))
