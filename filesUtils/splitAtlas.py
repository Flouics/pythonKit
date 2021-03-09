import urllib.request
import urllib.parse
import json
import time
import base64
import os,sys
import shutil
from PIL import Image

# 用以获取当前的工作目录
cd = os.getcwd()
sys.path.append('../')
from common import utils

def main(root = cd):
    fileDir =  os.path.join(root, "splitAtlas")   
    outDir = os.path.join(root, "splitAtlasOut")
    print("outDir",outDir)
    utils.removedirs(outDir)
    for root, dirs, files in os.walk(fileDir):
        for dir in dirs:
            # 遍历文件夹
            #print(os.path.join(root, dir))
            pass
        for file in files:
            filePath = os.path.join(root, file)
            if filePath.endswith(".atlas"):
                split(filePath)

def split(filePath):
    print("filePath",filePath)
    folderPath, fileName = os.path.split(filePath)
    fname, suffix = os.path.splitext(fileName)
    pngName = fname + ".png"   
    pngFile = os.path.join(folderPath, pngName)   
    if os.path.exists(pngFile):
        big_image = Image.open(pngFile)
        with open(filePath, 'r') as atlas:
            #              
            _line = atlas.readline();
            while _line.find("repeat"):         #直到找到repeat这一行
                _line = atlas.readline();
            
            rl = None
            while True:                
                if rl is None:
                    rl = atlas.readline() # name
                if len(rl) == 0:
                    break
                else:
                    dict = {}
                    while  True: #直到找到有:分割符的                       
                        args = rl.split(":")
                        if len(args) < 2 :
                            dict["name"] = utils.trim(args[0])
                            rl = atlas.readline() 
                        else:
                            break

                    while  len(args) > 1: #开始解析            
                        dict[utils.trim(args[0])] = utils.trim(args[1]).split(",")
                        rl = atlas.readline() # rotate
                        args = rl.split(":")
                    
                    print(dict)
                    name = dict["name"] + ".png";
                    # rotate,size,orig,offset,index
                    args = dict["size"]
                    width = int(args[0])
                    height= int(args[1])
                    
                    args =  dict["xy"]
                    ltx = int(args[0])
                    lty = int(args[1])
                    
                    rbx = ltx+width
                    rby = lty+height
                    
                    #print(name,width,height,ltx,lty,rbx,rby)
                    
                    result_image = Image.new("RGBA", (width,height), (0,0,0,0))
                    rect_on_big = big_image.crop((ltx,lty,rbx,rby))
                    #print(rect_on_big)
                    result_image.paste(rect_on_big, (0,0,width,height))                   
                    outPath = os.path.join(folderPath.replace("splitAtlas","splitAtlasOut"),name)
                    utils.mkdirs(outPath)
                    result_image.save(outPath)

    print("success")
if __name__=="__main__":
    main(cd)