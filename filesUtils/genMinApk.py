
# coding=utf-8
# encoding=utf-8

#检查文件格式
import os, re, sys
import codecs
import shutil
import filetype
sys.path.append('../')
from common import utils


# 用以获取当前的工作目录
cd = os.getcwd()

def main(root = cd,dirname = None):
    if dirname is None:
        print("please enter dirname, for example: dsHg")
        return
    fileDir =  os.path.join(os.path.join(root, dirname))
    resDir = os.path.join(os.path.join(fileDir, "src"))
    checkDir = os.path.join(os.path.join(fileDir, "hot"))
    outDir = os.path.join(os.path.join(fileDir, "out"))
    utils.removedirs(outDir)
    for root, dirs, files in os.walk(resDir):
        for dir in dirs:
            # 遍历文件夹
            #print(os.path.join(root, dir))
            pass
        for file in files:
            filePath = os.path.join(root, file)
            checkPath = filePath.replace(resDir, checkDir)
            outPath = filePath.replace(resDir, outDir)
            if  not os.path.exists(checkPath):
                #print(filePath)
                utils.mkdirs(outPath)
                shutil.copyfile(filePath, outPath)

if __name__ == "__main__" :
        dirname = "apk"
        main(cd,dirname)
