#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import MySQLdb
import shutil



db = MySQLdb.connect(host = "10.202.35.109", port = 3306, user = "taey16", passwd = "Skp02596", db = "PBrain", charset='utf8')
cursor = db.cursor()
target_table = "11st_fashion_tab_texture_230K_cropped"
dest_prefix = '/data2'
dest_path = '/data2/fashion_tab_texture/dataset_refined/none/'
if not os.path.exists(dest_path):
  os.makedirs(dest_path)

count = 0
cursor.execute("SELECT __org_img_url__, __mctgr_nm__, __sctgr_nm__ FROM %s WHERE label = '%s'" % (target_table, u'무지'))
rows = cursor.fetchall()
for row in rows:
  org_img_url, mctgr, sctgr = row
  file_name = org_img_url.split('/')[-1]
  file_path = os.path.join(dest_prefix, org_img_url[1:])
  # 중카테고리가 '니트', '모자' 가 아니거나 소카테고리가 '크롤링'이면
  if (mctgr != u'니트' and mctgr != u'모자') or (sctgr == u'크롤링'):
    shutil.copy(file_path, dest_path)
  count += 1
  if count % 100 == 0:
    print str(count) + '/' + str(len(rows))

print id
cursor.close()
db.close()
