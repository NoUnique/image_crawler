#!/usr/bin/python
#-*- coding: utf-8 -*-

import MySQLdb
import time
import shutil


t = time.time()

db = MySQLdb.connect(host = "10.202.35.109", port = 3306, user = "taey16", passwd = "Skp02596", db = "PBrain", charset='utf8')
cursor = db.cursor()
target_table = "11st_fashion_tab_texture2"
target_table1 = "11st_fashion_tab_attribute_texture"
target_table2 = "11st_fashion_tab_texture"
dest_prefix = '/data2'
destpath = '/freebee/img_google/Images2/none/'

id = 0

#cursor.execute("SELECT __org_img_url__, __lctgr_nm__, __mctgr_nm__, __sctgr_nm__, __prd_no__, __roi__ FROM %s WHERE label = '%s';" % (target_table1, '무지'))
#rows = cursor.fetchall()
#for row in rows:
#  filename = row[0].split('/')[-1]
#  filepath = '/data2/freebee/Images/' + filename
#  shutil.copy(filepath, dest_prefix + destpath)
#  url = destpath + filename
#  lctgr, mctgr, sctgr = row[1:4]
#  prd_no = int(row[4])
#  roi = row[5]
#  cursor.execute("INSERT INTO %s(__org_img_url__, __lctgr_nm__, __mctgr_nm__, __sctgr_nm__, __prd_no__, __roi__, label) VALUES ('%s', '%s', '%s', '%s', %d, '%s', '%s');" % (target_table, url, lctgr, mctgr, sctgr, prd_no, roi, u'무지'))
#  id += 1

cursor.execute("SELECT __org_img_url__, __lctgr_nm__, __mctgr_nm__, __sctgr_nm__, __prd_no__, __roi__ FROM %s WHERE label = '%s'" % (target_table2, ''))
rows = cursor.fetchall()
for row in rows:
  filename = row[0].split('/')[-1]
  filepath = '/data2/' + row[0]
  shutil.copy(filepath, dest_prefix + destpath)
  url = destpath + filename
  lctgr, mctgr, sctgr = row[1:4]
  prd_no = int(row[4])
  roi = row[5]
  cursor.execute("INSERT INTO %s(__org_img_url__, __lctgr_nm__, __mctgr_nm__, __sctgr_nm__, __prd_no__, __roi__, label) VALUES ('%s', '%s', '%s', '%s', %d, '%s', '%s');" % (target_table, url, lctgr, mctgr, sctgr, prd_no, roi, u'무지'))
  id += 1

print id
cursor.close()
db.close()
