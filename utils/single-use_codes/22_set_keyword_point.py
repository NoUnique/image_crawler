#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sys # for argument
import glob

# 패턴 별 특정 옷 형태에 대해 잘 드러나는 것과 아닌 것에대한 제한 표시
pattern_restrict = {'stripe': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    'flower': [0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    'punch': [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                    'check': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    'dot': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    'paisley': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    'print': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    'animalprint': [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}

patterns = ['stripe', 'flower', 'punch', 'check', 'dot', 'paisley' ,'print', 'animalprint']

pattern_portions = [({'stripe': '*0.6',
                      'striped': '*1.0',
                      '스트라이프': '*0.3;+0.05',
                      '줄무늬': '*0.3;+0.1'}),
                    ({'flower': '*1.0',
                      'flower pattern': '*0.9',
                      '꽃무늬': '*0.2;+0.1',
                      '꽃패턴': '*0.2;+0.05',
                      '꽃': '*0.2;+0.05'}),
                    ({'eyelet': '*1.0',
                      'laser cut': '*0.8',
                      'lace': '*1.1',
                      'lace pattern': '*1.0',
                      '펀칭': '*0.01'}),
                    ({'check': '*1.0',
                      'check pattern': '*0.6',
                      '체크': '*0.3;+0.1',
                      '체크무늬': '*0.15;+0.05'}),
                    ({'dot': '*1.0',
                      'dotted': '*0.8',
                      'polka dot': '*1.0',
                      'polkadot': '1.0',
                      'polka-dot': '1.0',
                      '도트': '*0.6;+0.1',
                      '땡땡이': '*0.15;+0.05'}),
                    ({'paisley': '*1.0',
                      'paisley pattern': '*0.9',
                      '페이즐리': '*0.6;+0.1',
                      '페이즐리 무늬': '*0.05;+0.05'}),
                    ({'print': '',
                      'printed': '',
                      '프린트': '',
                      '프린팅': ''}),
                    ({'animal print': '*0.8',
                      'leopard': '*1.0',
                      'leopard pattern': '*1.0',
                      'leopard print': '*0.95',
                      'zebra': '*0.5',
                      'zebra pattern': '*0.4',
                      'zebra print': '*0.7',
                      '레오파드': '*0.5;+0.1',
                      '호피': '*0.05',
                      '호피무늬': '*0.2;+0.05',
                      '얼룩말무늬': '*0.1'}) ]

pkeywords_list = {'stripe': ('stripe', 'striped', '스트라이프', '줄무늬'),
                  'flower': ('flower', 'flower pattern', '꽃무늬', '꽃패턴', '꽃'),
                  'punch': ('eyelet', 'laser cut', 'lace', 'lace pattern', '펀칭'),
                  'check': ('check', 'check pattern', '체크', '체크무늬'),
                  'dot' : ('dot', 'dotted', 'polka dot', 'polkadot', 'polka-dot', '도트', '땡땡이'),
                  'paisley': ('paisley', 'paisley pattern', '페이즐리', '페이즐리 무늬'),
                  'print': ('print', 'printed', '프린트', '프린팅'),
                  'animalprint': ('animal print', 'leopard', 'leopard pattern', 'leopard print', 'zebra', 'zebra pattern', 'zebra print', '레오파드', '호피', '호피무늬', '얼룩말무늬') }

ckeywords_list = [ ('tshirt', 'tshirts', 't shirt', 't-shirt', 'polo shirt', 'polo shirts', 'sweat shirt', 'sweat shirts', 'sweatshirt', 'sweatshirts', 'henley shirt', 'henley shirts', 'henley t-shirt', 'henley t shirt', 'henley tshirts', 'henley t-shirts', 'sleeveless', 'sleeveless shirt', 'sleeveless shirts', 'sleeveless t-shirt', 'sleeveless t shirt', 'sleeveless tshirt', 'sleeveless t-shirts', 'sleeveless tshirts', 'sleeveless top', 'hoodie', '티셔츠'),
                   ('shirt', 'shirts', 'camp shirt', 'camp shirts', 'dress shirt', 'dress shirts', '셔츠'),
                   ('blouse', 'boat blouse', 'boat neck blouse', 'cowl blouse', 'cowl neck blouse', 'bow blouse', 'pussy bow blouse', 'gatherd blouse', 'gathered neck blouse', 'square blouse', 'square neck blouse', 'scoop blouse', 'scoop neck blouse', 'peter pan blouse', 'peter pan neck blouse', '블라우스'),
                   ('sweater', 'turtleneck sweater', 'pullover sweater', '니트', '스웨터'),
                   ('jacket', 'denim jacket', 'leather jacket', 'tuxedo jacket', 'sport coat', 'windbreaker', 'blazer', '자켓', '재킷'),
                   ('dress', 'swing dress', 'wrap dress', 'sarong dress', 'pencil dress', 'slip dress', 'shirt dress', 'shirtdress', 'turtleneck dress', 'strappy dress', 'playsuit', 'pantsuit', 'romper', 'romper suit', 'sleeveless dress', '원피스'),
                   ('skirt', 'skirts', 'swing skirt', 'swing skirts', 'wrap skirt', 'wrap skirts', 'pleated skirts', 'A skirt', 'A line skirt', 'A-line skirt', 'A-lined skirt', 'A skirts', 'A line skirts', 'A-line skirts', 'A-lined skirts', 'pencil skirt', 'pencil skirts', 'mini skirt', 'mini skirts', 'miniskirt', 'miniskirts', 'mini=skirt', 'mini-skirts', 'prairie skirt', 'prairie skirts', 'slip skirt', 'slip skirts', 'skort', 'skorts', '치마', '스커트'),
                   ('coat', 'trench coat', '코트'),
                   ('cardigan', '가디건'),
                   ('vest', 'sweater vest', 'waistcoat', '조끼'),
                   ('pants', 'trouser', 'trousers', 'jeans', 'bell bottom', 'bell-bottom', 'bell bottom trouser', 'bell bottom trousers', 'bell bottom jean', 'bell bottom jeans', 'bell-bottom jean', 'bell-bottom jeans', 'bell-bottom trouser', 'bell-bottom trousers', 'bermuda short', 'bermuda shorts', 'capri pant', 'capri pants', 'lowrise pant', 'lowrise pants', 'low-rise pant', 'low-rise pants', 'low rise pant', 'low rise pants', 'overall pant', 'overall pants', 'palazzo pant', 'palazzo pants', 'parachute pant', 'parachute pants', 'shorts', 'sweat pant', 'sweat pants', 'sweatpants', 'slim pant', 'slim pants', 'wind pant', 'wind pants', 'yoga pant', 'yoga pants', 'yogapants', '바지'),
                   ('leggings', 'ankle leggings', 'ankle-length leggings', '레깅스'),
                   ('shoes', 'sneakers', 'running shoes', 'loafers', 'boots', 'flip flop', 'flip flops', 'flip-flop', 'flip-flops', 'court shoe', 'court shoes', '단화'),
                   ('bag', '가방'),
                   ('swimwear', '수영복'),
                   ('hat', 'cap', 'baseball cap', 'flat cap', 'beanie', 'fedora', 'floppy hat', 'bowler hat', 'panama hat', 'boater hat', '모자'),
                   ('panties', 'knicker', 'knickers', 'boxers', 'briefs', 'boxer briefs', 'boxer shorts', 'underwear', '팬티', '트렁크', '언더웨어'),
                   ('bra', '브래지어', '브라') ]
pattern = patterns[int(sys.argv[1])]
pattern_portion = pattern_portions[int(sys.argv[1])]

current_path = os.getcwd()
query_path = os.path.join(current_path, 'queries' + os.sep)

# 옷 종류 키워드에 대한 검색결과 바운더리 portion값을 가져오기 
with open(os.path.join(query_path, 'clothing_portion.txt'), 'r') as f:
  clothing_portions = {}
  lines = f.readlines()
  for line in lines:
    clothing = line.split(';')[0]
    portion = float(line.split(';')[-1])
    clothing_portions[clothing] = portion

def calculate_portion(pkeyword, ckeyword):
  portion = clothing_portions[ckeyword]
  operation_list = pattern_portion[pkeyword].split(';')
  for operation in operation_list:
    operator = operation[0]
    number = float(operation[1:])
    if operator == '*':
      portion = portion * number
    elif (operator == '+') and (portion > 0.1):
      portion = portion + number 
  return portion
  
with open(os.path.join(query_path, pattern+'.txt'), 'w') as f:
  pkeywords = pkeywords_list[pattern]
  for i in range(18):
    restrict = pattern_restrict[pattern][i]
    ckeywords = ckeywords_list[i]
    for ckeyword in ckeywords:
      for pkeyword in pkeywords:
        if restrict == 1:
          portion = calculate_portion(pkeyword, ckeyword)
        else:
          portion = 0.0
        query = pkeyword + ' ' + ckeyword
        f.write(query+';%.2f\n' % portion)
