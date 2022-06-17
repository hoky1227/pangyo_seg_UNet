# -*- coding: utf-8 -*-

import json
from glob import glob
import os
from tqdm import tqdm

def change_key(dictionary, old_key, new_key):
    dictionary[new_key] = dictionary[old_key]
    del dictionary[old_key]
    return dictionary

path = '/users/hoky1227/pangyo_seg/masks_json/ct_2d_*.json'
# path = '/users/hoky1227/pangyo/images/ct_2d_*.jpg'
human_path = '/users/hoky1227/pangyo_seg/masks_coco/'
# human_path = '/users/hoky1227/pangyo/human_annotations2/'
img_path = '/users/hoky1227/pangyo_seg/imgs/'

fl = glob(path)

c = 0

for f in tqdm(fl):
    name = os.path.basename(f)\

    dataset = json.load(open(f, 'r'))
    imgs = dataset['images']
    annot = dataset['annotations']
    imgs = change_key(imgs, 'image_id', 'id')
    imgs['id'] = int(imgs['id'])
    imgs['width'] = int(imgs['width'])
    imgs['height'] = int(imgs['height'])
    imgs = change_key(imgs, 'filename', 'file_name')
    imgs['file_name'] = img_path + name.rstrip('.json') + '.jpg'

    # get only 'label_id' == '39' annotation info in dataset['annotations']
    human_annot = {'images' : imgs}
    # human_annot = {'annotations' : []}
    # human_annot['annotations'] = [a for a in annot if a['label_id'] == '39']
    human_annot['annotations'] = annot

    for i in range(len(human_annot['annotations'])):
        human_annot['annotations'][i]['image_id'] = imgs['id'] 
        human_annot['annotations'][i] = change_key(human_annot['annotations'][i], 'label_id', 'category_id')
        human_annot['annotations'][i] = change_key(human_annot['annotations'][i], 'info', 'segmentation')
        human_annot['annotations'][i] = change_key(human_annot['annotations'][i], 'annotation_id', 'id')
        seg = [[]]
        for j in range(len(human_annot['annotations'][i]['segmentation'])):
            seg[0].append(human_annot['annotations'][i]['segmentation']['x'])
            seg[0].append(human_annot['annotations'][i]['segmentation']['y'])
        human_annot['annotations'][i]['segmentation'] = seg

    if human_annot['annotations'] == []:
        c += 1
        continue

    # make json file with same name as input file
    # with open(human_path + name, 'w', encoding='utf-8-sig') as fp:
    #     json.dump(human_annot, fp, ensure_ascii=False, indent=2)

    with open(human_path + name, 'w') as fp:
        json.dump(human_annot, fp, indent=2)

print('# of human not included files', c)