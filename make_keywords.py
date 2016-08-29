#!/usr/bin/python
#-*- coding: utf-8 -*-

import pickle
import os

# list of texture pattern
# (prefix, label_kor), (keywords)
patterns = [(('none', '무지'), ('plain', 'plain red', 'plain blue', 'plain yellow', 'plain green', 'plain black', 'plain white', 'plain orange', 'plain skyblue', 'plain sky blue', 'plain grey', 'plain gray', 'plain ivory', 'plain purple', 'plain pink', 'plain yellow green', '무지')),
            (('stripe', '스트라이프'), ('stripe', 'striped', '스트라이프', '줄무늬')),
            (('flower', '꽃무늬'), ('flower', 'flower pattern', '꽃무늬', '꽃패턴', '꽃')),
            (('punch', '펀칭'), ('eyelet', 'laser cut', 'lace', 'lace pattern', '펀칭')),
            (('check', '체크'), ('check', 'check pattern', '체크', '체크무늬')),
            (('dot', '도트'), ('dot', 'dotted', 'polka dot', 'polkadot', 'polka-dot', '도트', '땡땡이')),
            (('paisley', '페이즐리'), ('paisley', 'paisley pattern', '페이즐리', '페이즐리 무늬')),
            (('print', '프린팅'), ('print', 'printed', '프린트', '프린팅')),
            (('animalprint', '애니멀프린팅'), ('animal print', 'leopard', 'leopard pattern', 'leopard print', 'zebra', 'zebra pattern', 'zebra print', '레오파드', '호피', '호피무늬', '얼룩말무늬')) ] # '펀칭'은 'eyelet'의 콩글리시, 애니멀프린트에서 뱀피/악어피 등의 분류는 잘 검색되지 않음
        
# list of clothes type
# (prefix, lctgr, mctgr), (keywords) 
clothings = [ (('tshirts', '상의', '티셔츠'), ('tshirt', 'tshirts', 't shirt', 't-shirt', 't shirts', 't-shirts', 'polo shirt', 'polo shirts', 'sweat shirt', 'sweat shirts', 'sweatshirt', 'sweatshirts', 'henley shirt', 'henley shirts', 'henley t-shirt', 'henley t shirt', 'henley tshirts', 'henley t-shirts', 'sleeveless', 'sleeveless shirt', 'sleeveless shirts', 'sleeveless t-shirt', 'sleeveless t shirt', 'sleeveless tshirt', 'sleeveless t-shirts', 'sleeveless tshirts', 'sleeveless top', 'hoodie', '티셔츠')),
              (('shirts', '상의', '셔츠'), ('shirt', 'shirts', 'camp shirt', 'camp shirts', 'dress shirt', 'dress shirts', '셔츠')),
              (('blous', '상의', '블라우스'), ('blouse', 'boat blouse', 'boat neck blouse', 'cowl blouse', 'cowl neck blouse', 'bow blouse', 'pussy bow blouse', 'gatherd blouse', 'gathered neck blouse', 'square blouse', 'square neck blouse', 'scoop blouse', 'scoop neck blouse', 'peter pan blouse', 'peter pan neck blouse', '블라우스')),
              (('knit', '상의', '니트'), ('sweater', 'turtleneck sweater', 'pullover sweater', '니트', '스웨터')),
              (('jacket', '상의', '재킷'), ('jacket', 'denim jacket', 'leather jacket', 'tuxedo jacket', 'sport coat', 'windbreaker', 'blazer', '자켓', '재킷')),
              (('onepiece', '상하일체', '원피스'), ('dress', 'swing dress', 'wrap dress', 'sarong dress', 'pencil dress', 'slip dress', 'shirt dress', 'shirtdress', 'turtleneck dress', 'strappy dress', 'playsuit', 'pantsuit', 'romper', 'romper suit', 'sleeveless dress', '원피스')),
              (('skirts', '하의', '치마'), ('skirt', 'skirts', 'swing skirt', 'swing skirts', 'wrap skirt', 'wrap skirts', 'pleated skirts', 'A skirt', 'A line skirt', 'A-line skirt', 'A-lined skirt', 'A skirts', 'A line skirts', 'A-line skirts', 'A-lined skirts', 'pencil skirt', 'pencil skirts', 'mini skirt', 'mini skirts', 'miniskirt', 'miniskirts', 'mini=skirt', 'mini-skirts', 'prairie skirt', 'prairie skirts', 'slip skirt', 'slip skirts', 'skort', 'skorts', '치마', '스커트')),
              (('coat', '상의', '코트'), ('coat', 'trench coat', '코트')),
              (('cardigan', '상의', '가디건'), ('cardigan', '가디건')),
              (('vest', '상의', '조끼'), ('vest', 'sweater vest', 'waistcoat', '조끼')),
              (('pants', '하의', '바지'), ('pants', 'trouser', 'trousers', 'jeans', 'bell bottom', 'bell-bottom', 'bell bottom trouser', 'bell bottom trousers', 'bell bottom jean', 'bell bottom jeans', 'bell-bottom jean', 'bell-bottom jeans', 'bell-bottom trouser', 'bell-bottom trousers', 'bermuda short', 'bermuda shorts', 'capri pant', 'capri pants', 'lowrise pant', 'lowrise pants', 'low-rise pant', 'low-rise pants', 'low rise pant', 'low rise pants', 'overall pant', 'overall pants', 'palazzo pant', 'palazzo pants', 'parachute pant', 'parachute pants', 'shorts', 'sweat pant', 'sweat pants', 'sweatpants', 'slim pant', 'slim pants', 'wind pant', 'wind pants', 'yoga pant', 'yoga pants', 'yogapants', '바지')),
              (('leggings', '하의', '레깅스'), ('leggings', 'ankle leggings', 'ankle-length leggings', '레깅스')),
              (('shoes', '기타', '신발'), ('shoes', 'sneakers', 'running shoes', 'loafers', 'boots', 'flip flop', 'flip flops', 'flip-flop', 'flip-flops', 'court shoe', 'court shoes', '단화')),
              (('bags', '기타', '가방'), ('bag', '가방')),
              (('swimwears', '기타', '수영복'), ('swimwear', '수영복')),
              (('hat', '기타', '모자'), ('hat', 'cap', 'baseball cap', 'flat cap', 'beanie', 'fedora', 'floppy hat', 'bowler hat', 'panama hat', 'boater hat', '모자')),
              (('panties', '기타', '팬티'), ('panties', 'knicker', 'knickers', 'boxers', 'briefs', 'boxer briefs', 'boxer shorts', 'underwear', '팬티', '트렁크', '언더웨어')),
              (('bra', '기타', '브래지어'), ('bra', '브래지어', '브라')) ]

with open('pattern_list.list', 'w') as f:
  pickle.dump(patterns, f)

with open('clothing_list.list', 'w') as f:
  pickle.dump(clothings, f)


current_path = os.getcwd()
dest_path = os.path.join(current_path, 'queries')
if not os.path.exists(dest_path):
  os.makedirs(dest_path)

for pattern in patterns:
  pattern_name = pattern[0][0] 
  pattern_keywords = pattern[1]
  with open(os.path.join(dest_path, pattern_name + '.txt'), 'w') as f:
    for clothing in clothings:
      clothing_keywords = clothing[1]
      for ckeyword in clothing_keywords:
        for pkeyword in pattern_keywords:
          f.write(pkeyword+' '+ckeyword+';\n')


# 변동사항
# 16.07.21(목): pussy blouse 삭제 (검색 시 무한루프)
# 16.07.21(목): tuxedo vest 삭제 (검색품질 낮음)
# 16.07.21(목): pajama, pajama shirt, pajama shirts, pajama pants 삭제 (분류 없음)
# 16.07.21(목): harrington jacket 삭제 (패턴+옷 으로 검색했을 때 검색품질 낮음)
# 16.07.21(목) 11:25: 1차 키워드 입력 완료(티셔츠, 셔츠, 블라우스, 원피스, 치마, 바지 위주의 입력)
# 16.07.21(목): scrub, scrubs, scrub top, scrub tops 삭제 (검색품질 낮음)
