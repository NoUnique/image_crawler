#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sys # for argument
import glob

current_path = os.getcwd()
query_path = os.path.join(current_path, 'queries' + os.sep)

# 키워드에 대한 검색결과 바운더리 portion값을 가져오기 
with open(os.path.join(query_path, 'stripe_portion.txt'), 'r') as f:
  query_portion_list = f.readlines()

with open(os.path.join(query_path, 'clothing_portion.txt'), 'w') as f:
  for query_portion in query_portion_list:
    query, portion = query_portion.split(';')
    portion = float(portion)
    query_pattern = query.split(' ')[0]
    if query_pattern == 'striped':
      query = ' '.join(query.split(' ')[1:])
      f.write(query+';%.2f\n' % portion)
