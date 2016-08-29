#!/usr/bin/python
#-*- coding: utf-8 -*-

import MySQLdb
import time


t = time.time()

db = MySQLdb.connect(host = "10.202.35.109", port = 3306, user = "taey16", passwd = "Skp02596", db = "PBrain")
cursor = db.cursor()
source_table = "image_sentence"
target_table = "11st_fashion_tab_attribute"

patterns = ['무지', '스트라이프', '꽃패턴', '펀칭', '체크', '도트', '사진', '일러스트', '헤링본']
start_from = 1


id = 0
cursor.execute("SELECT id, __prd_no__, __roi__, __img_url__, __img_sentence__ FROM %s WHERE id = %d;" % (source_table, start_from))
row = cursor.fetchone()
while row is not None:
	check = 0
	start_from += 1
	prd_no = row[1]
	roi = row[2]
	img_url = row[3]
	img_sentence = row[4]
	for pattern in patterns:
		if pattern in img_sentence.split(' '):
			id += 1
			check += 2**patterns.index(pattern)	

			if check in [1, 2, 4, 8, 16, 32, 64, 128, 256]:
				#하나만 일치하면 tag는 기본값(-1)
				tag = -1
				if check == 1: # 무지(0)
					label = 0
				elif check == 2: # 스트라이프(1)
					label = 1
				elif check == 4: # 꽃패턴(2)
					label = 2
				elif check == 8: # 펀칭(3)
					label = 3
				elif check == 16: # 체크(4)
					label = 4
				elif check == 32: # 도트(5)
					label = 5
				elif check == 64 or check == 128: # 프린팅(사진, 일러스트)(7)
					label = 7
				elif check == 256: # 헤링본(8)
					label = 8
			else:
				# 여러개 일치하면 tag를 1로 표시해둠
				tag = 1
				label = -1 # Unknown
			
			cursor.execute("INSERT INTO %s(id, __prd_no__, __org_img_url__, __roi__, __img_sentence__, __tag__, label) VALUES (%d, %s, '%s', '%s', '%s', %d, %d);" % (target_table, id, prd_no, img_url, roi, img_sentence, tag, label))
	cursor.execute("SELECT id, __prd_no__, __roi__, __img_url__, __img_sentence__ FROM %s WHERE id = %d;" % (source_table, start_from))
	row = cursor.fetchone()

print id
cursor.close()
db.close()
