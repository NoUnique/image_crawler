#!/usr/bin/python
#-*- coding: utf-8 -*-

import MySQLdb
import time


t = time.time()

db = MySQLdb.connect(host = "10.202.35.109", port = 3306, user = "taey16", passwd = "Skp02596", db = "PBrain")
cursor = db.cursor()
target_table = "11st_fashion_tab_attribute"

id = 1
cursor.execute("SELECT __img_sentence__ FROM %s WHERE id = %d;" % (target_table, id))
row = cursor.fetchone()
while row is not None:
  img_sentence = row[0].split(' ')
  if (img_sentence[0] != '상의') and (img_sentence[0] != '하의'):
    lctgr = '기타'
    mctgr = img_sentence[0]
    sctgr = img_sentence[1]
  else:
    lctgr = img_sentence[0]
    mctgr = img_sentence[1]
    sctgr = img_sentence[2]

  cursor.execute("UPDATE %s SET __lctgr_nm__ = '%s', __mctgr_nm__ = '%s', __sctgr_nm__ = '%s' WHERE id = %d;" % (target_table, lctgr, mctgr, sctgr, id)) 

  id += 1
  cursor.execute("SELECT __img_sentence__ FROM %s WHERE id = %d;" % (target_table, id))
  row = cursor.fetchone()

print id 
cursor.close()
db.close()
