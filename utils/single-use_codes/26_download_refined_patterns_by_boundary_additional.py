#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import csv
import urllib2 as urllib
from PIL import Image
from StringIO import StringIO
import sys # for argument
import glob
import fnmatch
import requests
#import subprocess # for casperjs

patterns = ['stripe', 'flower', 'punch', 'check', 'dot', 'paisley' ,'print', 'animalprint']
pattern = patterns[int(sys.argv[1])]

# format list to download
format_list = ['jpeg', 'jpg', 'png']
# limit of ratio of images (from 1:2.5 to 2.5:1)
ratio_limit = (0.4, 2.5)
# limit of dimensions of images
dimension_limit = 128
# path of dataset
dataset_path = '/data2/fashion_tab_texture/dataset_refined/Images'
current_path = os.getcwd()
csv_path = os.path.join(current_path, 'urls', pattern + os.sep)
query_path = os.path.join(current_path, 'queries' + os.sep)
dest_path = os.path.join(dataset_path, pattern + '_additional' + os.sep)

if not os.path.exists(dest_path):
  os.makedirs(dest_path)

# 정제된 패턴 쿼리목록
with open(os.path.join(query_path, pattern+'_boundary.txt')) as f:
  query_list = f.readlines()

url_lists = []
csv_list = [] 
for root, dir_names, file_names in os.walk(csv_path):
  for file_name in fnmatch.filter(file_names, '*.csv'):
    csv_list.append(os.path.join(current_path, 'urls', pattern, root, file_name))


# 쿼리목록으로부터 '패턴_옷형태' 를 읽어와 url csv목록에서 뒤짐
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
        url_lists.append(csv_urls[0:endpoint])

# TODO: 해당 쿼리가 csv목록에 없는 경우에 대한 처리를 추가할 것

target_urls = []
for url_order in url_lists:
  for url in url_order:
    if url not in target_urls:
      target_urls.append(url)

print pattern + '에 대한 '+ str(len(target_urls))+'개 이미지 URL에 대해 다운로드를 시도합니다'
index = len(os.listdir(dest_path))
for ori_url in target_urls:
  try:
    url = ori_url.rstrip('\n')
    print url,
    # Use requests to aviod SSL error for more robust download
    response = requests.get(url, timeout = 3)
    content_type = response.headers['Content-Type'].split('/')[1].split(';')[0]
    if (content_type in format_list):
      image_read = response.content
      width, height = Image.open(StringIO(image_read)).size
      ratio = float(width)/float(height)
      if (ratio < ratio_limit[0] or ratio > ratio_limit[1]):
        print ' has not good ratio. ratio is '+str(ratio)
      elif (width < dimension_limit or height < dimension_limit):
        print ' has not enough size'
      else:
        if (content_type == 'jpeg'):
          file_format = 'jpg'
        else:
          file_format = content_type
        file_name = pattern+'_'+format(index, '010')+'.'+file_format
        with open(os.path.join(dest_path, file_name), 'wb') as f:
          f.write(image_read)
        print ' is downloaded'
        index += 1
    else:
      print ' is not image format'
  except:
    print ' download error index: '+str(target_urls.index(ori_url))

print str(index)+'개 이미지 다운로드 완료'
