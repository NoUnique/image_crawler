#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sys # for argument
import glob

patterns = ['stripe', 'flower', 'punch', 'check', 'dot', 'paisley' ,'print', 'animalprint']
pattern = patterns[int(sys.argv[1])]

pattern_portions = [({'stripe': '*0.6',
              'striped': '*1.0',
              '스트라이프': '*0.3;+0.05',
              '줄무늬': '*0.3;+0.1'}),
            ({'flower': '',
              'flower pattern': '',
              '꽃무늬': '',
              '꽃패턴': '',
              '꽃': ''}),
            ({'eyelet': '',
              'laser cut': '',
              'lace': '',
              'lace pattern': '',
              '펀칭': ''}),
            ({'check': '',
              'check pattern': '',
              '체크': '',
              '체크무늬': ''}),
            ({'dot': '',
              'dotted': '',
              'polka dot': '',
              'polkadot': '',
              'polka-dot': '',
              '도트': '',
              '땡땡이': ''}),
            ({'paisley': '',
              '페이즐리': ''}),
            ({'print': '',
              'printed': '',
              '프린트': '',
              '프린팅': ''}),
            ({'animal print': '',
              'leopard': '',
              'leopard pattern': '',
              'leopard print': '',
              'zebra': '',
              'zebra pattern': '',
              'zebra print': '',
              '레오파드': '',
              '호피': '',
              '호피무늬': '',
              '얼룩말무늬': ''}) ] # '펀칭'은 'eyelet'의 콩글리시, 애니멀프린트에서 뱀피/악어피 등의 분류는 잘 검색되지 않음
pattern_portion = pattern_portions[int(sys.argv[1])]

current_path = os.getcwd()
query_path = os.path.join(current_path, 'queries' + os.sep)

# 키워드에 대한 검색결과 바운더리 portion값을 가져오기 
with open(os.path.join(query_path, pattern+'_portion.txt'), 'r') as f:
  query_portion_list = f.readlines()

with open(os.path.join(query_path, pattern+'_clothing_portion.txt'), 'w') as f:
  for query_portion in query_portion_list:
    query, portion = query_portion.split(';')
    portion = float(portion)
    query_pattern = query.split(' ')[0]
    
    operation_list = pattern_portion[query_pattern].split(';')
    for operation in operation_list[::-1]: # 각 오퍼레이션에 대해 뒤집어진 순서로 (뺄셈 먼저, 나눗셈 나중에)
      operator = operation[0]
      number = float(operation[1:])
      if operator == '*':
        portion = portion / number
      elif (operator == '+') and (portion > number):
        portion = portion - number 
    f.write(query+';%.2f\n' % portion)
