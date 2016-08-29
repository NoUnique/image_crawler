#!/usr/bin/python

import MySQLdb
import time


t = time.time()

db = MySQLdb.connect(host = "10.202.35.109", port = 3306, user = "taey16", passwd = "Skp02596", db = "PBrain")
cursor = db.cursor()

count = 810000
cursor.execute("SELECT * FROM image_sentence WHERE id = %d" % count)
row = cursor.fetchone()
while row is not None:
	if row[1] == '-1':
		pass
	else:
		values = row[3].split('/')
		if values[1] == 'data2':
			cursor.execute("UPDATE image_sentence SET __prd_no__ = '%s',__img_url__ = '%s' WHERE id = %s" % (values[4].split('.')[0], '/freebee/'+values[4], row[0]))
		elif values[1] == 'data3':
			cursor.execute("UPDATE image_sentence SET __prd_no__ = '%s',__img_url__ = '%s' WHERE id = %s" % (values[4].split('.')[0], '/freebee3/'+values[4], row[0]))
		count += 1	
		cursor.execute("SELECT * FROM image_sentence WHERE id = %d" % count)
		row = cursor.fetchone()
print count
cursor.close()
db.close()
