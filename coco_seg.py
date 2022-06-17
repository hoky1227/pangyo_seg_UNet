# -*- coding: utf-8 -*-

import json
from glob import glob
import os
from tqdm import tqdm

def change_key(dictionary, old_key, new_key):
    dictionary[new_key] = dictionary[old_key]
    del dictionary[old_key]
    return dictionary

path = '/users/hoky1227/pangyo_seg/high_resolution/masks_json/ct_seg_h_*.json'
# path = '/users/hoky1227/pangyo/images/ct_2d_*.jpg'
human_path = '/users/hoky1227/pangyo_seg/high_resolution/masks_coco/'
# human_path = '/users/hoky1227/pangyo/human_annotations2/'
img_path = '/users/hoky1227/pangyo_seg/high_resolution/imgs/'

fl = glob(path)

c = 0

coco_json = {'images': [], 'annotations': []}

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

    # get only 'label_id' == '105' annotation info in dataset['annotations']
    human_annot = {'images' : imgs}
    # human_annot = {'annotations' : []}
    human_annot['annotations'] = [a for a in annot if a['label_id'] == '105']
    # human_annot['annotations'] = annot

    if human_annot['annotations'] == []:
        c += 1
        continue

    for i in range(len(human_annot['annotations'])):
        human_annot['annotations'][i]['image_id'] = imgs['id'] 
        human_annot['annotations'][i] = change_key(human_annot['annotations'][i], 'label_id', 'category_id')
        human_annot['annotations'][i] = change_key(human_annot['annotations'][i], 'info', 'segmentation')
        human_annot['annotations'][i] = change_key(human_annot['annotations'][i], 'annotation_id', 'id')
        seg = []
        for j in range(len(human_annot['annotations'][i]['segmentation'])):
            seg.append(human_annot['annotations'][i]['segmentation'][j]['x'])
            seg.append(human_annot['annotations'][i]['segmentation'][j]['y'])
        human_annot['annotations'][i]['segmentation'] = [seg]
        human_annot['annotations'][i]['id'] = int(human_annot['annotations'][i]['id'])
        human_annot['annotations'][i]['category_id'] = 1

    

    # make json file with same name as input file
    # with open(human_path + name, 'w', encoding='utf-8-sig') as fp:
    #     json.dump(human_annot, fp, ensure_ascii=False, indent=2)
    coco_json['images'].append(human_annot['images'])
    coco_json['annotations'].extend(human_annot['annotations']) 
    coco_json['categories'] = [{'id': 1, 'name': 'road', "supercategory": "road"}]

with open(human_path + 'coco_json.json', 'w') as fp:
    json.dump(coco_json, fp, indent=2)


print('# of road not included files', c)