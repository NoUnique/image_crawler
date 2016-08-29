#!/usr/bin/python
#-*- coding: utf-8 -*-

import time
import MySQLdb
import os

db = MySQLdb.connect(host = "10.202.35.109", port = 3306, user = "taey16", passwd = "Skp02596", db = "PBrain")
cursor = db.cursor()
target_table = '11st_fashion_tab_texture_cropped'

for id in range(1,1715271):
  cursor.execute("UPDATE %s SET __org_img_url__='%s' WHERE id=%d;" % (target_table, '/fashion_tab_texture/Images/'+format(id, '010')+'.jpg', id))

cursor.close()
db.close()
