import time
#import glob
import os
import random
import shutil
import fnmatch

# set size of validation set
validation_size_limit = 50000

validation_size = 0
while (validation_size < validation_size_limit-32):
  validation_size += 32
test_size = validation_size * 2
sample_size = validation_size + test_size

t = time.time()

current_path = os.getcwd()
for root in ['val', 'test']:
  for dirname in ['none', 'stripe', 'flower', 'punch', 'check', 'dot', 'paisley', 'print', 'animalprint']:
    path = os.path.join(current_path, root, dirname)
    if not os.path.exists(path):
      os.makedirs(path)
# ** in glob only works in python 3.5
#file_list = random.sample(glob.iglob(current_path + '/ALL/**/*', recursive = True), sample_size)
glob = []
for root, dirnames, filenames in os.walk('train'):
  for filename in fnmatch.filter(filenames, '*.jpg'):
    glob.append(os.path.join(current_path,root, filename))
file_list = random.sample(glob, sample_size)

for file_path in file_list[0:validation_size]:
  file_path_list = file_path.split('/')
  file_path_list[-3] = 'val'
  dest_path = '/'.join(file_path_list)
  shutil.move(file_path, dest_path)

for file_path in file_list[validation_size:]:
  file_path_list = file_path.split('/')
  file_path_list[-3] = 'test'
  dest_path = '/'.join(file_path_list)
  shutil.move(file_path, dest_path)
