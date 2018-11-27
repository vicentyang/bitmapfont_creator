#coding=utf-8
import os
from PIL import Image

def createFNT():
    pass

UNIT_SIZE = 55 # 图像的高
TARGET_WIDTH = 0 #

path = "/Users/vicent/Desktop/20180929"
imagefile = []
i = 0
padding = 5
for root, dirs, files in os.walk(path):
    for f in files :
        # print(f)
        if not f.startswith("."):
            i += 1
            _img = Image.open(path+'/'+f)
            TARGET_WIDTH += _img.width + padding
            imagefile.append(_img)
print('TARGET_WIDTH', i, TARGET_WIDTH)
target = Image.new('RGBA', (TARGET_WIDTH, UNIT_SIZE))
left = 0
right = UNIT_SIZE
print(target)
for image in imagefile:
    # print(image)
    target.paste(image, (left, 0))
    left += image.width + padding
    # right += UNIT_SIZE
quality_value = 100
# target.save(path+'/result.png', quality = quality_value)
target.save('./result.png', quality = quality_value)
