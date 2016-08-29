#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sys
import glob
import urllib2
import json

pattern_list = ['none', 'stripe', 'flower', 'punch', 'check', 'dot', 'paisley', 'print', 'animalprint']

host_ip = '10.202.34.62'
cdn_port = 2596
predict_port = 8080
data_path = '/data2/fashion_tab_texture/dataset_refined/test/'

image_url = data_path.replace('/data2/', 'http://%(host_ip)s:%(cdn_port)d/PBrain/freebee/' % \
  {'host_ip': host_ip, 'cdn_port': cdn_port} )

request_url = 'http://%(host_ip)s:%(predict_port)d/texture_request_handler?url=%%s' % \
  {'host_ip': host_ip, 'predict_port': predict_port}

def get_result(image_url):
  try:
    url = request_url % image_url
    result = json.load(urllib2.urlopen(url))
    #print result
    top = result['texture_name'][0]
    
  except Exception as err:
    raise err
  
  return top


confusion_table = []
confusion_count_table = []
for pattern in pattern_list:
  root = os.path.join(data_path, pattern)
  image_list = glob.glob(os.path.join(root, '*.jpg'))
  count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  length = len(image_list)
  for image_file in image_list:
    try:
      image_url = image_file.replace('/data2/', 'http://%(host_ip)s:%(cdn_port)d/PBrain/freebee/' % \
        {'host_ip': host_ip, 'cdn_port': cdn_port} )
      predicted = get_result(image_url)
      print image_file.split('/')[-1] + ' predicted : ' + predicted; sys.stdout.flush()
      count[pattern_list.index(predicted)] += 1
      print pattern + ' confusion : ' + str(map(lambda x: '%.2f' % (float(x)/float(length)*100.0), count)); sys.stdout.flush()
    except:
      length -= 1
      print 'server error(500)'
      
  print pattern + 'ENDED'
  confusion_table.append(map(lambda x: '%.2f' % (float(x)/float(length)*100.0), count))
  confusion_count_table.append(count)
print 'Making confusion_matrix process ENDED'
for line in confusion_table:
  print str(line)

print ' '

for line in confusion_count_table:
  print str(line)


    
