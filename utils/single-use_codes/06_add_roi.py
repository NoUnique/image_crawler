#!/usr/bin/python
#-*- coding: utf-8 -*-

import time
import MySQLdb
import glob
import json
import os

t = time.time()

db = MySQLdb.connect(host = "10.202.35.109", port = 3306, user = "taey16", passwd = "Skp02596", db = "PBrain")
cursor = db.cursor()
targetTable = '11st_fashion_tab_texture'
auto_increment = 229987

current_path = os.getcwd()
file_list = sorted(glob.glob(current_path + '/tmp.json/*'))

cursor.execute("DELETE FROM %s WHERE id > %d;" % (targetTable, auto_increment-1))
cursor.execute("ALTER TABLE %s AUTO_INCREMENT=%d;" % (targetTable, auto_increment))

for filename in file_list:
  with open(filename, 'r') as f:
    i = -1
    lines = f.readlines()
    for line in lines:
      jsonDict= json.loads(line)
      roiDict = jsonDict['roi']
      url = jsonDict['url']
      url_key = url.split('PBrain')[1]

      for rois in roiDict.keys():
        for roi in roiDict[rois]:
          roiText = str(int(roi[0]))+' '+str(int(roi[1]))+' '+str(int(roi[2]-roi[0]))+' '+str(int(roi[3]-roi[1]))
          # for first roi, update the row already exists
          if roi == roiDict[roiDict.keys()[0]][0]:
            # update
            cursor.execute("UPDATE %s SET __roi__='%s' WHERE __org_img_url__='%s';" % (targetTable, roiText, url_key))
          else:
            # insert
            cursor.execute("INSERT INTO %s (__roi__, __prd_no__, __org_img_url__, __lctgr_nm__, __mctgr_nm__, __sctgr_nm__, label) SELECT '%s', __prd_no__, __org_img_url__, __lctgr_nm__, __mctgr_nm__, __sctgr_nm__, label FROM %s WHERE __org_img_url__='%s' LIMIT 1;" % (targetTable, roiText, targetTable, url_key))

      i += 1

      if i % 100 == 0:
        print str(i) + ' / ' + str(len(lines))

cursor.close()
db.close()
