#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import random
import shutil
import fnmatch
import MySQLdb
import glob

db = MySQLdb.connect(host = "10.202.35.109", port = 3306, user = "taey16", passwd = "Skp02596", db = "PBrain", charset='utf8')
cursor = db.cursor()
target_table = '11st_fashion_tab_texture_230K_cropped'

label_list = { u'무지': 'none',
               u'스트라이프': 'stripe',
               u'꽃무늬': 'flower',
               u'펀칭': 'punch',
               u'체크': 'check',
               u'도트': 'dot',
               u'페이즐리': 'paisley',
               u'프린팅': 'print',
               u'애니멀프린팅': 'animalprint' }

set_list = ['train', 'val', 'test']

# set size of validation set
cursor.execute("SELECT __org_img_url__, label, set_id FROM %s" % target_table)
db_rows = cursor.fetchall()
db_size = len(db_rows)

# train:val:test = 8:1:2
validation_size_limit = int(db_size * 1/11)

validation_size = 0
while (validation_size < validation_size_limit-32):
  validation_size += 32
test_size = validation_size * 2
sample_size = validation_size + test_size

print 'val_size: ' + str(validation_size) + '\ttest_size: ' + str(test_size)

dest_prefix = '/data2'
dest_path = '/fashion_tab_texture/dataset_230K/'

current_path = os.getcwd()
for root in ['train', 'val', 'test']:
  path = os.path.join(current_path, root)
  if not os.path.exists(path):
    os.makedirs(path)
  for dirname in ['none', 'stripe', 'flower', 'punch', 'check', 'dot', 'paisley', 'print', 'animalprint']:
    path = os.path.join(current_path, root, dirname)
    if not os.path.exists(path):
      os.makedirs(path)

## 전체를 train폴더에 카피
#print 'coping files to /train/ folder...'
#for row in db_rows:
#  org_img_url = row[0]
#  label = row[1]
#  set_id = int(row[2]) # set_id -> 0:train, 1:validation, 2:test
#  file_name = org_img_url.split('/')[-1]
#  source_path = dest_prefix + org_img_url
#  train_dest_path = os.path.join(current_path, set_list[set_id], label_list[label]) + '/'
#  shutil.copy(source_path, train_dest_path)
#
#  if int(file_name.split('.')[0]) % 1000 == 0:
#    print org_img_url
#print 'copy(train) done'
  
# 일부를 뽑아 validation / test셋을 만듦
sample_index_list = random.sample(xrange(db_size), sample_size)
target_set_id = 1
for index_list in [sample_index_list[0:validation_size], sample_index_list[validation_size:]]:
  for i in index_list:
    row = db_rows[i]
    org_img_url = row[0]
    label = row[1]
    file_name = org_img_url.split('/')[-1]
    set_id = int(row[2]) # set_id -> 0:train, 1:validation, 2:test
    source_path = os.path.join(current_path, set_list[set_id], label_list[label], file_name)
    dest_path = os.path.join(current_path, set_list[target_set_id], label_list[label]) + '/'
    shutil.move(source_path, dest_path)
    # DB에 업데이트
    cursor.execute("UPDATE %s SET set_id=%d WHERE __org_img_url__='%s'" % (target_table, target_set_id, org_img_url))
    
    if index_list.index(i) % 100 == 0:
      print str(index_list.index(i)) + '/' + str(len(index_list))
  target_set_id += 1
