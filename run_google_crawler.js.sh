#!/bin/sh
nohup casperjs google_crawler.js --q="공항패션" --o="airport_fashion_g.csv" &
nohup casperjs google_crawler.js --q="공항패션가방" --o="airport_fashion_bag_g.csv" &
nohup casperjs google_crawler.js --q="공항패션신발" --o="airport_fashion_shoes_g.csv" &
nohup casperjs google_crawler.js --q="공항패션종결자" --o="airport_fashion_final_g.csv" &
nohup casperjs google_crawler.js --q="일반인공항패션" --o="1ban_airport_fashion_g.csv" &
nohup casperjs google_crawler.js --q="길거리패션가방" --o="on_load_fashion_bag_g.csv" &
nohup casperjs google_crawler.js --q="남자연예인공항패션" --o="man_airport_fashion_g.csv" &
nohup casperjs google_crawler.js --q="여자연예인공항패션" --o="woman_airport_fashion_g.csv" &
nohup casperjs google_crawler.js --q="여성복" --o="womans_clothes_g.csv" &
nohup casperjs google_crawler.js --q="캐주얼복장" --o="casual_clothes_g.csv" &
nohup casperjs google_crawler.js --q="길거리패션" --o="on_load_clothes_g.csv" &
nohup casperjs google_crawler.js --q="아이돌공항패션" --o="idol_air_port_fashion_g.csv" &

nohup casperjs bing_crawler.js --q="공항패션" --o="airport_fashion_b.csv" &
nohup casperjs bing_crawler.js --q="공항패션가방" --o="airport_fashion_bag_b.csv" &
nohup casperjs bing_crawler.js --q="공항패션신발" --o="airport_fashion_shoes_b.csv" &
nohup casperjs bing_crawler.js --q="공항패션종결자" --o="airport_fashion_final_b.csv" &
nohup casperjs bing_crawler.js --q="일반인공항패션" --o="1ban_airport_fashion_b.csv" &
nohup casperjs bing_crawler.js --q="길거리패션가방" --o="on_load_fashion_bag_b.csv" &
nohup casperjs bing_crawler.js --q="남자연예인공항패션" --o="man_airport_fashion_b.csv" &
nohup casperjs bing_crawler.js --q="여자연예인공항패션" --o="woman_airport_fashion_b.csv" &
nohup casperjs bing_crawler.js --q="여성복" --o="womans_clothes_b.csv" &
nohup casperjs bing_crawler.js --q="캐주얼복장" --o="casual_clothes_.csv" &
nohup casperjs bing_crawler.js --q="길거리패션" --o="on_load_clothes_b.csv" &
nohup casperjs bing_crawler.js --q="아이돌공항패션" --o="idol_air_port_fashion_b.csv" &
