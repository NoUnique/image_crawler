#!/usr/bin/python
#-*- coding: utf-8 -*-

import MySQLdb
from PIL import Image

# code for make cropped 'none(무지)' image dataset from DB tables already exist

db = MySQLdb.connect(host = "10.202.35.109", port = 3306, user = "taey16", passwd = "Skp02596", db = "PBrain", charset='utf8')
cursor = db.cursor()
target_table = "11st_fashion_tab_texture_cropped"
source_tables = ["11st_fashion_tab_attribute_texture", "11st_fashion_tab_texture"]
format_list = ['jpg', 'JPG', 'jpeg', 'JPEG', 'png', 'PNG'] # jpg & png only
dest_prefix = '/data2'
dest_path = '/fashion_tab_texture/dataset/Images/none/'

id = 1

for source_table in source_tables:
  cursor.execute("SELECT __org_img_url__, __lctgr_nm__, __mctgr_nm__, __sctgr_nm__, __prd_no__, __roi__ FROM %s WHERE label = '%s';" % (source_table, '무지'))
  rows = cursor.fetchall()
  for row in rows:
    try:
      file_name = row[0].split('/')[-1]
      file_format = file_name.split('.')[-1]
      if file_format in format_list:
        if source_table == source_tables[0]:
          file_path = '/data2/freebee/Images/' + file_name
        else:
          file_path = dest_prefix + row[0]
        cropped_file_name = format(id, '010') + '.jpg' # save to jpg
        url = dest_path + cropped_file_name
        lctgr, mctgr, sctgr = row[1:4]
        prd_no = int(row[4])
        roi = row[5]
        roi_list = map(int, roi.split(' '))
        # roi가 존재하고 일정 크기(128x128) 이상일 때
        if (len(roi_list) >= 4) and (roi_list[2] > 128) and (roi_list[3] > 128):
          image = Image.open(file_path)
          image = image.crop((roi_list[0], roi_list[1], roi_list[0] + roi_list[2], roi_list[1] + roi_list[3]))
          # 배경이 투명한 png 일 경우 흰 배경 추가 
          if (file_format in ['png', 'PNG']) and (image.mode == 'RGBA'):
            image.load()
            background = Image.new('RGB', image.size, (255, 255, 255))
            background.paste(image, mask=image.split()[3])
            image = background
          if image.mode != 'RGB':
            image = image.convert('RGB')
          image.save(dest_prefix + url, 'jpeg', quality=100)
          cursor.execute("INSERT INTO %s(__org_img_url__, __lctgr_nm__, __mctgr_nm__, __sctgr_nm__, __prd_no__, label) VALUES ('%s', '%s', '%s', '%s', %d, '%s');" % (target_table, url, lctgr, mctgr, sctgr, prd_no, u'무지'))
          id += 1
    except BaseException as error:
      print str(error)

print id
cursor.close()
db.close()
