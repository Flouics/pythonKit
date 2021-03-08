#coding=utf-8

##作用：读取replace.txt，替换掉files需要替换的文字，然后输出到outFiles文件夹。

import os,re,sys
import codecs
sys.path.append('../')
from common import utils

cd = os.getcwd()
srcId = 924
outId = 3023
srcStr = "Act" + str(srcId)
outStr = "Act" + str(outId)
srcCmd = ".hd" + str(srcId)
outCmd = ".hd" + str(outId)
fileDir = os.path.join(cd, "copyAct/src/"+ srcStr.lower())
outDir = os.path.join(cd, "copyAct/out/" + outStr.lower())

def main():
    allFilesList = []
    allKeysDict = {}

    utils.removedirs(outDir)

    allKeysDict["." + srcStr.lower()] = "." + outStr.lower()
    allKeysDict[srcStr] = outStr
    allKeysDict[srcStr.lower() + "Proxy"] = outStr.lower() + "Proxy"
    allKeysDict["/" + srcStr.lower()] = "/" + outStr.lower()
    allKeysDict[srcCmd] = outCmd

    for root, dirs, files in os.walk(fileDir):
        for dir in dirs:
            # 遍历文件夹
            print(os.path.join(root, dir))

        for file in files:
            allFilesList.append(os.path.join(root, file))


    for file in allFilesList:
        newfile = file.replace(fileDir, outDir)
        newfile = newfile.replace(srcStr,outStr)
        newfile = newfile.replace(srcStr.lower(), outStr.lower())
        utils.mkdirs(newfile)
        with codecs.open(file, 'r',encoding='utf-8') as f:
            with codecs.open(newfile, 'w',encoding='utf-8') as newf:
                lines = f.readlines()
                for line in lines:
                    for key in allKeysDict:
                        line = line.replace(key,allKeysDict[key])
                    newf.write(line)

def trip(str):
    return str.strip()


main()