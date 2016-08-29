#!/usr/bin/python
#-*- coding: utf-8 -*-

import MySQLdb
import time


t = time.time()

db = MySQLdb.connect(host = "10.202.35.109", port = 3306, user = "taey16", passwd = "Skp02596", db = "PBrain")
cursor = db.cursor()
target_table = "11st_fashion_tab_attribute"

id = 1
label_dic = { 0:'무지',
              1:'스트라이프',
              2:'꽃무늬',
              3:'펀칭',
              4:'체크',
              5:'도트',
              6:'페이즐리',
              7:'프린팅',
              8:'헤링본',
              -1:'' }
cursor.execute("SELECT label_legacy FROM %s WHERE id = %d;" % (target_table, id))
row = cursor.fetchone()
while row is not None:
  label_int = int(row[0])
  cursor.execute("UPDATE %s SET label = '%s' WHERE id = %d;" % (target_table, label_dic[label_int], id)) 

  id += 1
  cursor.execute("SELECT label_legacy FROM %s WHERE id = %d;" % (target_table, id))
  row = cursor.fetchone()

print id 
cursor.close()
db.close()
