#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import csv
import sys # for argument
import glob
import fnmatch
import requests
#import subprocess # for casperjs

patterns = ['stripe', 'flower', 'punch', 'check', 'dot', 'paisley' ,'print', 'animalprint']
pattern = patterns[int(sys.argv[1])]

current_path = os.getcwd()
csv_path = os.path.join(current_path, 'urls', pattern + os.sep)
query_path = os.path.join(current_path, 'queries' + os.sep)

# 정제된 패턴 쿼리목록
with open(os.path.join(query_path, pattern+'.txt')) as f:
  query_list = f.readlines()

url_lists = []
csv_list = [] 
for root, dir_names, file_names in os.walk(csv_path):
  for file_name in fnmatch.filter(file_names, '*.csv'):
    csv_list.append(os.path.join(current_path, 'urls', pattern, root, file_name))


# 쿼리목록으로부터 '패턴_옷형태' 를 읽어와 url csv목록에서 뒤짐
with open(os.path.join(query_path, pattern+'_portion.txt'), 'w') as fo:
  for query_endpoint in query_list:
    query, endpoint = query_endpoint.rstrip('\n').split(';')
    if endpoint == '':
      endpoint = 0
    else:
      endpoint = int(endpoint)
    csv_file = 'urls_google_'+query.replace(' ', '_') + '.csv' 
    
    for csv_file_path in csv_list:
      # url csv목록에 해당 쿼리가 있으면 바로 다운로드 시작
      if csv_file_path.split('/')[-1] == csv_file:
        with open(csv_file_path, 'rb') as f:
          csv_urls = f.readlines()
          csv_length = len(csv_urls)
    portion = '%.2f' % (float(endpoint)/float(csv_length))
    fo.write(query+';'+portion+'\n')

# TODO: 해당 쿼리가 csv목록에 없는 경우에 대한 처리를 추가할 것
