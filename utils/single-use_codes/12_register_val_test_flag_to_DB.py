import os
import glob
import MySQLdb
import fnmatch

target_table = '11st_fashion_tab_texture_cropped'

validation_folder = 'val'
evaluation_folder = 'test'
training_folder = 'train'

db = MySQLdb.connect(host = "10.202.35.109", port = 3306, user = "taey16", passwd = "Skp02596", db = "PBrain")
cursor = db.cursor()

current_path = os.getcwd()
  
folder_list = [training_folder, validation_folder, evaluation_folder]
for folder in folder_list:
  glob = []
  for root, dirnames, filenames in os.walk(folder):
    for filename in fnmatch.filter(filenames, '*.jpg'):
      glob.append(os.path.join(current_path, root, filename))
  file_list = sorted(glob)
  # ** in glob only works in python 3.5
  #target_path = os.path.join(current_path, folder, '**/*.jpg') # jpg files only
  #file_list = sorted(glob.glob(target_path))
  
  print 'start at ' + folder
  count = 0
  for file_path in file_list:
    id = int(file_path.split('/')[-1].split('.')[0])
    flag = folder_list.index(folder)

    cursor.execute("UPDATE %s SET set_id = %d WHERE id = %d" % (target_table, flag, id))

    count += 1
    if count % 1000 == 0:
      print str(count) + '/' + str(len(file_list))

cursor.close()
db.close()
