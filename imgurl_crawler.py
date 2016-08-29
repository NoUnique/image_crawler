#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import csv
import pickle

# format list to download
format_list = ['jpeg', 'gif', 'png']
# limit of ratio of images (from 1:3 to 3:1)
ratio_limit = (1/2.5, 2.5/1)
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

current_path = os.getcwd()
csvfolder = current_path + '/urls/'
if not os.path.exists(csvfolder):
  os.makedirs(csvfolder)

for pattern in patterns:
  sub1_csvfolder = csvfolder + pattern[0][0]+'/'
  if not os.path.exists(sub1_csvfolder):
    os.makedirs(sub1_csvfolder)

  for clothing in clothings:
    sub2_csvfolder = sub1_csvfolder + pattern[0][0] +'_'+clothing[0][0]+'/'
    if not os.path.exists(sub2_csvfolder):
      os.makedirs(sub2_csvfolder)
    for pkeyword in pattern[1]:
      for ckeyword in clothing[1]:
        query = pkeyword+' '+ckeyword
        csv = pkeyword.replace(' ', '_')+'_'+ckeyword.replace(' ', '_')+'.csv' 
        if not os.path.exists(sub2_csvfolder+'urls_google_'+csv):
          print "query: '"+query+"', target: google"
          os.system('casperjs google_crawler.js --q="'+query+'" --o='+sub2_csvfolder+'urls_google_'+csv)
#        if not os.path.exists(sub2_csvfolder+'urls_bing_'+csv):
#          print "query: '"+query+"', target: bing"
#          os.system('casperjs bing_crawler.js --q="'+query+'" --o='+sub2_csvfolder+'urls_bing_'+csv)

# TODO:
#1. 한글 + 'pussy blouse' 조합의 경우에 무한루프에 빠짐(수정필요)
#2. 한글 + 영문(영문 + 한글은 해당없음) 조합으로 Bing에서 크롤링 할 경우 크롤링 갯수가 현저히 줄어듬
#3. 이미지 크기별로 검색 가능한 기능 추가할 것
