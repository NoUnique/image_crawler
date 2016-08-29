#!/usr/bin/python
#-*- coding: utf-8 -*-

import MySQLdb
import shutil
import os

# code for make cropped 'none(무지)' image dataset from DB tables already exist

db = MySQLdb.connect(host = "10.202.35.109", port = 3306, user = "taey16", passwd = "Skp02596", db = "PBrain", charset='utf8')
cursor = db.cursor()
source_table = "11st_fashion_tab_texture_attribute"
source_path = '/data2/freebee/Images/'
dest_path = '/data2/fashion_tab_texture/dataset_refined/print/'

if not os.path.exists(dest_path):
  os.makedirs(dest_path)

id = 0

cursor.execute("SELECT __prd_no__, __mctgr_nm__ FROM %s WHERE label = '%s';" % (source_table, '프린팅'))
rows = cursor.fetchall()
for row in rows:
  prd_no, mctgr = row
  if mctgr == u'티셔츠':
    source = os.path.join(source_path, str(prd_no)+'.jpg')
    output = os.path.join(dest_path, format(id, '010') + '.jpg')
    shutil.copy(source, output)
    id += 1

    if id%100 == 0:
      print str(id) + '/' + str(len(rows))
