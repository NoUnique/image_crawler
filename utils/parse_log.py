
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

def parse(LOG_FILE_PATH, LOG_FILE_NAME, SET_ID):
    log_filename = '%s/%s' % (LOG_FILE_PATH, LOG_FILE_NAME % SET_ID)
    print log_filename
    entries = [entry.strip().split('\t') \
               for entry in open(log_filename, 'r')]
    entries = entries[1:]
    epoch = []
    loss = []
    elapsed = []
    err = []
    for entry in entries:
        epoch.append(entry[0])
        loss.append(entry[1])
        elapsed.append(entry[2])
        err.append(entry[3])
    epoch = np.asarray(epoch).astype(np.float)
    loss = np.asarray(loss).astype(np.float)
    elapsed = np.asarray(elapsed).astype(np.float)
    err = np.asarray(err).astype(np.float)
    return epoch, loss, elapsed, err

# inception-v3-20151205 classifier finetune
LOG_FILE_PATH = '/data2/ImageNet/ILSVRC2012/torch_cache/inception-v3-2015-12-05/X_gpu1_cudnn_v4_inception-v3-2015-12-05_nag_Sun_Feb_14_19_20_26_2016/'
LOG_FILE_NAME = '%s.log'
epoch_finetune, trn_loss_finetune, trn_elapsed_finetune, trn_err_finetune = parse(LOG_FILE_PATH, LOG_FILE_NAME, 'train')
epoch_finetune, val_loss_finetune, val_elapsed_finetune, val_err_finetune = parse(LOG_FILE_PATH, LOG_FILE_NAME, 'test')

plt.figure(figsize=(16,9));
plt.title('inception-v3')
plt.plot(epoch*40037, trn_loss, 'r-o');
plt.plot(epoch*40037, val_loss, 'b-o');
plt.grid(True); plt.xlabel('iter'); plt.ylabel('loss');
plt.figure(figsize=(16,9));
plt.title('inception-v3')
plt.plot(epoch*40037, trn_err, 'r-o');
plt.plot(epoch*40037, val_err, 'b-o');
plt.grid(True); plt.xlabel('iter'); plt.ylabel('err');

