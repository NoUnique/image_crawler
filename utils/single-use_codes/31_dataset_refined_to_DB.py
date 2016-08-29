#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sys
import glob
import shutil
import fnmatch
import MySQLdb

# code for make cropped image dataset from DB tables already exist

db = MySQLdb.connect(host = "10.202.35.109", port = 3306, user = "taey16", passwd = "Skp02596", db = "PBrain", charset='utf8')
cursor = db.cursor()
target_table = '11st_fashion_tab_texture_240K'

dataset_list = ['train', 'val', 'test']
label_list = {'none': '무지',
              'stripe': '스트라이프',
              'flower': '꽃무늬',
              'punch': '펀칭',
              'check': '체크',
              'dot': '도트',
              'paisley': '페이즐리',
              'print': '프린팅',
              'animalprint': '애니멀프린팅'}

current_path = os.getcwd()

index = 0
glob = []
for root, dirnames, filenames in os.walk(os.path.join(current_path, 'Images')):
  for filename in fnmatch.filter(filenames, '*.jpg'):
    glob.append(os.path.join(current_path, root, filename))

for image_path in glob:
  set_id = -1
  for dataset in dataset_list:
    if os.path.exists(image_path.replace('Images', dataset)):
      set_id = dataset_list.index(dataset)
  prd_no = index 
  org_img_url = image_path.replace('/data2/', '/')
  label = label_list[image_path.split('/')[5]]

  cursor.execute("INSERT INTO %s(__prd_no__, __org_img_url__, label, set_id) VALUES (%d, '%s', '%s', %d);" % (target_table, prd_no, org_img_url, label, set_id))

  index += 1
  
  if (index%100) == 0:
    print str(index) + '/' + str(len(glob))
    sys.stdout.flush()
