#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import random
import shutil
import fnmatch
import glob

# ** in glob only works in python 3.5
#glob = glob.iglob(current_path + '/ALL/**/*', recursive = True)
current_path = os.getcwd()

glob = []
for root, dirnames, filenames in os.walk('Images'):
  for filename in fnmatch.filter(filenames, '*.jpg'):
    glob.append(os.path.join(current_path,root, filename))
file_list = random.sample(glob, len(glob))

# train:val:test = 8:1:2
validation_size_limit = int(len(glob) * 1/10)

validation_size = 0
while (validation_size < validation_size_limit-32):
  validation_size += 32
test_size = validation_size
sample_size = validation_size + test_size

print 'val_size: ' + str(validation_size) + '\ttest_size: ' + str(test_size)

dest_prefix = '/data2'
dest_path = '/fashion_tab_texture/dataset_refined/'

for root in ['train', 'val', 'test']:
  path = os.path.join(current_path, root)
  if not os.path.exists(path):
    os.makedirs(path)
  for dirname in ['none', 'stripe', 'flower', 'punch', 'check', 'dot', 'paisley', 'print', 'animalprint']:
    path = os.path.join(current_path, root, dirname)
    if not os.path.exists(path):
      os.makedirs(path)


for file_path in file_list[0:validation_size]:
  file_path_list = file_path.split('/')
  file_path_list[-3] = 'val'
  dest_path = '/'.join(file_path_list)
  os.symlink(file_path, dest_path)

for file_path in file_list[validation_size:sample_size]:
  file_path_list = file_path.split('/')
  file_path_list[-3] = 'test'
  dest_path = '/'.join(file_path_list)
  os.symlink(file_path, dest_path)

for file_path in file_list[sample_size:]:
  file_path_list = file_path.split('/')
  file_path_list[-3] = 'train'
  dest_path = '/'.join(file_path_list)
  os.symlink(file_path, dest_path)
