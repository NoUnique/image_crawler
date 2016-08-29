#!/usr/bin/python
#-*- coding: utf-8 -*-

import pickle

with open('stripe.txt', 'r') as f:
  lines = f.readlines()

dic = {}
for line in lines:
  key, value = line.split(';')
  dic[key] = value



# list of texture pattern
# (pattern_eng, pattern_kor), (keywords)
with open('pattern_list.list') as f:
  patterns = pickle.load(f)

# list of clothes type
# (clothing_eng, lctgr, clothing_kor(mctgr)), (keywords)
with open('clothing_list.list') as f:
  clothings = pickle.load(f)

pattern = patterns[0]
pattern_name = pattern[0][0]
pattern_keywords = pattern[1]
with open('stripe_output.txt', 'w') as f:
  for clothing in clothings:
    clothing_keywords = clothing[1]
    for ckeyword in clothing_keywords:
      for pkeyword in pattern_keywords:
        key = pkeyword+' '+ckeyword
        f.write(key+';'+dic[key])
