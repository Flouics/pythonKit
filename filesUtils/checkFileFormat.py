
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
#参考资料 https://h2non.github.io/filetype.py/
checkSuffix = "png"
# 暂时无用了
checkFormatStrDict = {
"jpg" : "image/jpeg"
,"png" : "image/png"
}

def main(root = cd,dirname = None):
    if dirname is None:
        print("please enter dirname, for example: dsHg")
        return
    fileDir =  os.path.join(os.path.join(root, dirname))
    outDir = os.path.join(os.path.join(root, "out"))
    print("outDir",outDir)
    utils.removedirs(outDir)
    for root, dirs, files in os.walk(fileDir):
        for dir in dirs:
            # 遍历文件夹
            #print(os.path.join(root, dir))
            pass
        for file in files:
            filePath = os.path.join(root, file)
            if file.endswith('.' + checkSuffix):
                guessSuffix = filetype.guess_extension(filePath)
                if not guessSuffix == checkSuffix:
                    print('{0} error: {1} -> {2}'.format(filePath,checkSuffix,guessSuffix))
                    outPath = filePath.replace(fileDir,outDir)
                    outPath = outPath.replace('.' +checkSuffix, '.' +guessSuffix)
                    if os.path.exists(filePath):
                        utils.mkdirs(outPath)
                        shutil.copyfile(filePath, outPath)


if __name__ == "__main__" :
        dirname = "fix"
        main(cd,dirname)
