import os

file_name = 'log_initial_test_240K_resception_model_199_device2_3.log'
file_path = os.getcwd()

for output_file_name in ['train.log', 'test.log']:
  with open(os.path.join(file_path, output_file_name), 'w') as fout:
    fout.write('epoch\tloss\ttime\terr\n')

with open(os.path.join(file_path, file_name)) as f:
  for line in f.readlines():
    if line[0:2] == 'ep':
      line_split = line.split(' ')
      # ['epoch', '8', 'trn', 'loss:', '0.845235', 'err:', '28.494367, 'solver:', 'nag,', 'elapsed:', '8452.8160']
      if line_split[2] == 'trn':
        output_file_name = 'train.log'
      elif line_split[2] == 'tst':
        output_file_name = 'test.log'
      else:
        output_file_name = 'errors.txt'
      with open(os.path.join(file_path, output_file_name), 'a') as fout:
        fout.write('\t%0.4e\t%0.4e\t%0.4e\t%0.4e\n' % (float(line_split[1]), float(line_split[4]), float(line_split[-1]), float(line_split[6])))  
