# Google/Bing Image Crawler
- Crawler for Image search of Google/Bing
- by using CasperJS and PIL(Python Image Library)
- Since CasperJS doesn't have 'do..while' logic, I use yotsumoto's method https://github.com/yotsumoto/casperjs-goto


# Requirements
- CasperJS http://www.casperjs.org
- Python 2.7 (> 2.7.6, DO NOT SUPPORT Python 3) https://www.python.org
  Some URLs(using SSL) are not reachable because python 2.7.6 does not support a 'true SSLContext object'
  An Error occurs in SSLv3 handshakes
- PIL(Python Image Library) 'pip install pillow'
- Requests 'pip install requests' - for more robust download (in img_download.py)


# Code
- google_crawler.js: query image search to google by using CasperJS, and save urls of original image to 'links.csv'
- bing_crawler.js: query image search to bing by using CasperJS, and save urls of original image to 'links.csv'
- imgurl_crawler.py: example code for multiple queries, save result urls to csv file.
- img_downloader.py: read from 'url.csv' and download images to target folder.
- img_insertDB.py: read from 'img.csv' and insert it to DB


# Usage (imgurl_crawler.py)
- Set parameters in 'imgurl_crawler.py'
- 'python imgurl_crawler.py'


# Usage (img_downloader.py)
- For Temporary Use
- ARGUMENT REQUIRED!! Usage : 'python img_downloader.py 0' (0 to 7. index of label)


# Usage (*_crawler.js)
- 'casperjs google_crawler.js --q='query_string' [--t=1000 --o='./urls/urls.csv']'
- --q : query string
- --t : (optional, default = 1000) wait time(ms) after scrolling in virtual browser. optimal value depends on network speed and compute power of system
- --o : (optional, default = 'urls.csv') name of output url file 

# Credits: 
- TaeHwan Yoo
