from pycocotools.coco import COCO
from PIL import Image
import cv2
from tqdm import tqdm

coco = COCO('/users/hoky1227/pangyo_seg/masks_coco/coco_json.json')

# Get and fill in the all binary masks the masks from COCO json file and save them as .gif files. Set name of each mask as the image name.
for i in tqdm(coco.imgs):
    img = coco.loadImgs(i)[0]
    mask = coco.annToMask(coco.loadAnns(coco.getAnnIds(img['id']))[0])
    mask = Image.fromarray(mask)

    mask.save(img['file_name'].replace('imgs', 'masks').replace(".jpg", "_mask.gif"))