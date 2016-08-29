rm -R logs
mkdir logs
nohup python img_downloader.py 0 > logs/log_stripe.log &
nohup python img_downloader.py 1 > logs/log_flower.log &
nohup python img_downloader.py 2 > logs/log_punch.log &
nohup python img_downloader.py 3 > logs/log_check.log &
nohup python img_downloader.py 4 > logs/log_dot.log &
nohup python img_downloader.py 5 > logs/log_paisley.log &
nohup python img_downloader.py 6 > logs/log_print.log &
nohup python img_downloader.py 7 > logs/log_animalprint.log &
