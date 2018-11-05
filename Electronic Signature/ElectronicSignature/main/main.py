#coding:utf8
'''
Created on 2018年10月10日

@author: Administrator
'''
from PIL import Image
if __name__ == '__main__':
    photoPath="photos/Li_Zhang.jpg"
    img = Image.open(photoPath)
    Img = img.convert('L')
    Img.save(photoPath)
    threshold = 100
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    photo = Img.point(table, '1')
    photo.save("test2.jpg")
    print("finished!")
