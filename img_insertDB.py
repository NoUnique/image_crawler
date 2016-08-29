#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sys
import pickle
import MySQLdb
import glob

# list of texture pattern
# (pattern_eng, pattern_kor), (keywords)
with open('pattern_list.list') as f:
  patterns = pickle.load(f)

# list of clothes type
# (clothing_eng, lctgr, clothing_kor(mctgr)), (keywords) 
with open('clothing_list.list') as f:
  clothings = pickle.load(f)

targetTable = '11st_fashion_tab_attribute_texture_copy'

# 소분류 : (크롤링) 고정
sctgr = '크롤링'
current_path = os.getcwd()

db = MySQLdb.connect(host = "10.202.35.109", port = 3306, user = "taey16", passwd = "Skp02596", db = "PBrain")
cursor = db.cursor() 

cursor.execute("SET names utf8")

for pattern in patterns:
  if patterns.index(pattern) == int(sys.argv[1]):
    download_folder = current_path + '/Images/'+pattern[0][0]+'/'
    if os.path.exists(download_folder):
      label = pattern[0][1]
      file_list = sorted(glob.glob(download_folder+'*'))
      for clothing in clothings:
        # 대분류 : (상의/하의/상하일체/기타)
        lctgr = clothing[0][1]
        # 중분류 : (니트, 원피스, 티셔츠 등)
        mctgr = clothing[0][2]
        for filename_abs in file_list:
          filename = filename_abs.split('/')[-1] 
          if clothing[0][0] == filename.split('_')[1]:
            prd_no = int(filename.split('_')[-1].split('.')[0])
            org_img_url = '/freebee/img_google/Images/'+pattern[0][0]+'/'+filename
            cursor.execute("INSERT INTO %s(__prd_no__, __org_img_url__, __lctgr_nm__, __mctgr_nm__, __sctgr_nm__, label) VALUES (%d, '%s', '%s', '%s', '%s', '%s');" % (targetTable, prd_no, org_img_url, lctgr, mctgr, sctgr, label))
          
db.close()
