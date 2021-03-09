#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import os.path
import shutil
from PIL import Image

fileName = raw_input('输入要解析的文件名:')

if fileName.find('.png') != -1:
    fileName = fileName[:-4]

pngName = fileName + '.png'
atlasName = fileName + '.atlas'

print pngName,atlasName

big_image = Image.open(pngName)
atlas = file(atlasName, "r");


curPath = os.getcwd()# 当前路径
aim_path = os.path.join(curPath, fileName)
print aim_path
if os.path.isdir(aim_path):
    shutil.rmtree(aim_path,True)#如果有该目录,删除
os.makedirs(aim_path)

#
_line = atlas.readline();
_line = atlas.readline();
_line = atlas.readline();
_line = atlas.readline();

while True:
    line1 = atlas.readline() # name
    if len(line1) == 0:
        break
    else:
        line2 = atlas.readline() # rotate
        line3 = atlas.readline() # xy
        line4 = atlas.readline() # size
        line5 = atlas.readline() # orig
        line6 = atlas.readline() # offset
        line7 = atlas.readline() # index
        
        name = line1.replace("\n","") + ".png";
        
        args = line4.split(":")[1].split(",");
        width = int(args[0])
        height= int(args[1])
        
        args = line3.split(":")[1].split(",");
        ltx = int(args[0])
        lty = int(args[1])
        
        rbx = ltx+width
        rby = lty+height
        
        print name,width,height,ltx,lty,rbx,rby
        
        result_image = Image.new("RGBA", (width,height), (0,0,0,0))
        rect_on_big = big_image.crop((ltx,lty,rbx,rby))
        print(rect_on_big)
        result_image.paste(rect_on_big, (0,0,width,height))
        result_image.save(aim_path+'/'+name)
atlas.close()
del big_image

