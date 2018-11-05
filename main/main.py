#coding:utf8
'''
Created on 2018年10月10日

@author: Administrator
'''
from PIL import Image
if __name__ == '__main__':
    photoPath="photos/test1.jpg"
    resultName="test1.png"
    threshold = 100
    
    img = Image.open(photoPath)
    Img = img.convert('L')
    Img.save(photoPath)
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    photo = Img.point(table, '1')
    
    photo = Img.convert("RGBA")
    for row in range(photo.size[0]):
        for col in range(photo.size[1]):
            changedPx=list(photo.getpixel((row,col)))
            if changedPx[0]>threshold:
                changedPx[3]=0
            changedPx=tuple(changedPx)
            photo.putpixel((row,col),changedPx)
    
    
    photo.save(resultName)
    print("finished!")
