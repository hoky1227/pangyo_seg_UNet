import os
from glob import glob
from tqdm import tqdm

path = '/users/hoky1227/pangyo_seg/Pytorch-UNet/data/masks/ct_seg_m_*_mask.gif'
img_path = '/users/hoky1227/pangyo_seg/Pytorch-UNet/data/imgs/ct_seg_m_*.jpg'
fl = glob(path)
img_fl = glob(img_path)

# print(img_fl[0])
# os.remove(img_fl[0])

print(len(fl))
print(len(img_fl))

c = 0

for f in img_fl:
    fn = f.replace('imgs', 'masks').replace('.jpg', '_mask.gif')
    if fn not in fl:
        print(f)
        c += 1
        # delete the image
        # os.remove(f)
print(c)
