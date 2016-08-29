#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import csv
import urllib2 as urllib
from PIL import Image
from StringIO import StringIO
import pickle
import sys
import requests

# format list to download
format_list = ['jpeg', 'jpg', 'gif', 'png']
# limit of ratio of images (from 1:2.5 to 2.5:1)
ratio_limit = (0.4, 2.5)
# limit of dimensions of images
dimension_limit = 128

# list of texture pattern
# (pattern_eng, pattern_kor), (keywords)
with open('pattern_list.list') as f:
  patterns = pickle.load(f)

# list of clothes type
# (clothing_eng, lctgr, clothing_kor(mctgr)), (keywords) 
with open('clothing_list.list') as f:
  clothings = pickle.load(f)

# To use english search result only
def isASCII(string):
  return all(ord(c) < 128 for c in string)

current_path = os.getcwd()
csvfolder = current_path + '/urls/'
if not os.path.exists(csvfolder):
  raise Exception('Error: There is no URL csv folder!! - '+csvfolder)

for pattern in patterns:
  if patterns.index(pattern) == int(sys.argv[1]):
    download_folder = current_path + '/Images2/'+pattern[0][0]+'/'
    if not os.path.exists(download_folder):
      os.makedirs(download_folder)

    sub1_csvfolder = csvfolder + pattern[0][0]+'/'
    if not os.path.exists(sub1_csvfolder):
      raise Exception('Error: There is no URL csv/pattern folder!! - '+sub1_csvfolder)
  
    for clothing in clothings:
      sub2_csvfolder = sub1_csvfolder + pattern[0][0] +'_'+clothing[0][0]+'/'
      if not os.path.exists(sub2_csvfolder):
        raise Exception('Error: There is no URL csv/pattern/pattern_clothing folder!! - '+sub2_csvfolder)
      
      # list of URL lists
      url_lists = []
  
      for pkeyword in pattern[1]:
        for ckeyword in clothing[1]:
          query = pkeyword+' '+ckeyword
          csv = pkeyword.replace(' ', '_')+'_'+ckeyword.replace(' ', '_')+'.csv'
          # for Google URLs
          csv_google = sub2_csvfolder+'urls_google_'+csv
          if os.path.isfile(csv_google):
          #if (os.path.isfile(csv_google)) and (isASCII(csv_google)):
            with open(csv_google, 'rb') as f:
              csv_urls = f.readlines()
              url_lists.append(csv_urls)
              #url_lists.append(csv_urls[:int(len(csv_urls)/3)]) # 검색품질이 좋은 이미지만 쓰기 위해 1/3 지점까지만 사용
          # for Bing URLs
          csv_bing = sub2_csvfolder+'urls_bing_'+csv
          if os.path.isfile(csv_bing):
          #if (os.path.isfile(csv_binge)) and (isASCII(csv_bing)):
            with open(csv_google, 'rb') as f:
              csv_urls = f.readlines()
              url_lists.append(csv_urls)
              #url_lists.append(csv_urls[:int(len(csv_urls)/3)]) # 검색품질이 좋은 이미지만 쓰기 위해 1/3 지점까지만 사용
  
      # pattern_clothing list having rank without redundant
      target_urls = []

#  # a = [1,2,3,4], b=['a', 'b', 'c'], c=[5,4,3,2,1], d = [a,b,c]
#  # [item for m in map(None, *d) for item in m if item is not None]
#      for url_rank in map(None, *url_lists):
#        for url in url_rank:
#          if ((url is not None) and (url not in target_urls)):
#            target_urls.append(url)

      for url_order in url_lists:
        for url in url_order:
          if url not in target_urls:
            target_urls.append(url)
  
      print pattern[0][0]+'_'+clothing[0][0]+'의 '+str(len(target_urls))+'개 이미지 URL에 대해 다운로드를 시도합니다'
      
      index = 1 
      
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
                fileformat = 'jpg'
              else:
                fileformat = content_type
              filename = pattern[0][0]+'_'+clothing[0][0]+'_'+format(index, '08')+'.'+fileformat
              with open(download_folder+filename, 'wb') as f:
                f.write(image_read)
              print ' is downloaded'
              index += 1
          else:
            print ' is not image format'
        except:
          print ' download error index: '+str(target_urls.index(ori_url))
      
      print str(index-1)+'개 이미지 다운로드 완료'
