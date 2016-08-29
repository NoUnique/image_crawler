#!/usr/bin/python

import MySQLdb
import glob
import time


t = time.time()

file_list = glob.glob("/works/newdb/csv_160325//*.txt")
id = 0
for f in file_list:
	print (str(f) + ' is in progress')
	db = MySQLdb.connect(host = "10.202.35.109", port = 3306, user = "taey16", passwd = "Skp02596", db = "PBrain")
	cursor = db.cursor()

	file = open(f)
	for line in file:
		values = line.split(";;")
		id += 1
		cursor.execute("INSERT INTO image_sentence(id, __local_path__, __roi__, __img_sentence__) VALUES ( %d, '%s', '%s', '%s');" % (id, values[0], values[1], values[2][:-1]))
		
	db.close()
