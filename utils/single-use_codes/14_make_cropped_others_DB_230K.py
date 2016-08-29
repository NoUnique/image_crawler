#!/usr/bin/python
#-*- coding: utf-8 -*-

import MySQLdb
import glob
import json
import os
from PIL import Image

# code for make cropped image dataset from DB tables already exist

db = MySQLdb.connect(host = "10.202.35.109", port = 3306, user = "taey16", passwd = "Skp02596", db = "PBrain", charset='utf8')
cursor = db.cursor()
target_table = '11st_fashion_tab_texture_230K_cropped'

label_list = { 'none': u'무지',
               'stripe': u'스트라이프',
               'flower': u'꽃무늬',
               'punch': u'펀칭',
               'check': u'체크',
               'dot': u'도트',
               'paisley': u'페이즐리',
               'print': u'프린팅',
               'animalprint': u'애니멀프린팅' }

category = { 'tshirts': (u'상의', u'티셔츠'),
             'shirts': (u'상의', u'셔츠'),
             'blous': (u'상의', u'블라우스'),
             'knit': (u'상의', u'니트'),
             'jacket': (u'상의', u'재킷'),
             'onepiece': (u'상하일체', u'원피스'),
             'skirts': (u'하의', u'치마'),
             'coat': (u'상의', u'코트'),
             'cardigan': (u'상의', u'가디건'),
             'vest': (u'상의', u'조끼'),
             'pants': (u'하의', u'바지'),
             'leggings': (u'하의', u'레깅스'),
             'shoes': (u'기타', u'신발'),
             'bags': (u'기타', u'가방'),
             'swimwears': (u'기타', u'수영복'),
             'hat': (u'기타', u'모자'),
             'panties': (u'기타', u'팬티'),
             'bra': (u'기타', u'브래지어') }

current_path = os.getcwd()
file_list = sorted(glob.glob(current_path + '/tmp.json_230K/*'))
format_list = ['jpg', 'JPG', 'jpeg', 'JPEG', 'png', 'PNG'] # jpg & png only
dest_prefix = '/data2'
dest_path = '/fashion_tab_texture/dataset_230K/Images/'

# 무지 데이터가 38328 개 이므로 increment는 38329부터 시작
id = 38329

for filename in file_list:
  with open(filename, 'r') as f:
    i = -1
    lines = f.readlines()
    for line in lines:
      jsonDict= json.loads(line)
      roiDict = jsonDict['roi']
      file_name = jsonDict['url'].split('/')[-1]
      file_format = file_name.split('.')[-1]
      file_path = dest_prefix + jsonDict['url'].split('PBrain')[1]
      pattern = file_name.split('_')[0]
      clothes = file_name.split('_')[1]
      if file_format in format_list:
        roi = roiDict[roiDict.keys()[0]][0]
        try:
          cropped_file_name = format(id, '010') + '.jpg' # save to jpg
          url = dest_path + cropped_file_name
          lctgr, mctgr = category[clothes]
          sctgr = u'크롤링' 
          prd_no = id
          label = label_list[pattern]
          roi_list = [int(roi[0]), int(roi[1]), int(roi[2])-int(roi[0]), int(roi[3])-int(roi[1])]
          # roi가 존재하고 일정 크기(128x128) 이상일 때
          if (len(roi_list) >= 4) and (roi_list[2] > 128) and (roi_list[3] > 128):
            image = Image.open(file_path)
            image = image.crop((roi_list[0], roi_list[1], roi_list[0]+roi_list[2], roi_list[1]+roi_list[3]))
            # 배경이 투명한 png 일 경우 흰 배경 추가
            if (file_format in ['png', 'PNG']) and (image.mode == 'RGBA'):
              image.load()
              background = Image.new('RGB', image.size, (255, 255, 255))
              background.paste(image, mask=image.split()[3])
              image = background
            if image.mode != 'RGB':
              image = image.convert('RGB')
            image.save(dest_prefix + url, 'jpeg', quality=100)
            cursor.execute("INSERT INTO %s(__org_img_url__, __lctgr_nm__, __mctgr_nm__, __sctgr_nm__, __prd_no__, label) VALUES ('%s', '%s', '%s', '%s', %d, '%s');" % (target_table, url, lctgr, mctgr, sctgr, prd_no, label))
            id += 1
        except BaseException as error:
          print str(error)
  
        i += 1
        if i % 100 == 0:
          print pattern + ' ' + str(i) + ' / ' + str(len(lines))

print id
cursor.close()
db.close()
