# -*- coding: utf-8 -*-

import requests
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
import os
from tqdm import tqdm
import json
# from PIL import Image
# from io import BytesIO
import urllib.request as req

seg_path = '/users/hoky1227/pangyo_seg/high_resolution/masks_json/'
img_path = '/users/hoky1227/pangyo_seg/high_resolution/imgs/'

encoding = 'pLGIwnTnLPmyOxVd%2BYfPiHCNp3ru%2FL9bXwltuC84w9UnsyHKO%2FwOJ3unkZx%2FldjQ4%2Bdlc8oPErMg0pRFpi9ahw%3D%3D'
decoding = 'pLGIwnTnLPmyOxVd+YfPiHCNp3ru/L9bXwltuC84w9UnsyHKO/wOJ3unkZx/ldjQ4+dlc8oPErMg0pRFpi9ahw=='

params_list = []

url = 'http://apis.data.go.kr/C100006/zerocity/getCctvList/event/2DSegmentation'

for i in range(1, 8):
    globals()[f'params{i}'] = {'serviceKey' : decoding,
                                'type' : 'json',
                                'numOfRows' : '1000',
                                'pageNo' : str(i),
                                'sgmtType' : '01',
                                'startDt' : '2021-07-01',
                                'endDt' : '2021-12-31' }

for i in range(1, 8):
    params_list.append(globals()[f'params{i}'])

# response = requests.get(url, params=params1)
# aa = response.json()[0]
# print(aa)


for param in tqdm(params_list):
    response = requests.get(url, params=param)
    aa = response.json()[0]

    for i in range(len(aa['cctvfileList'])):
        seg_url = aa['cctvfileList'][i]['hgh_prcs_imsg_file_stor_flph']
        img_url = aa['cctvfileList'][i]['image_flph']
        response_seg = requests.get(seg_url)
        seg = response_seg.json()
        save_seg = aa['cctvfileList'][i]['hgh_prcs_imsg_file']
        save_img = aa['cctvfileList'][i]['image_file']
        with open(seg_path + save_seg, 'w') as f:
            json.dump(seg, f, indent=2)
        down_img = req.urlretrieve(img_url, img_path + save_img)