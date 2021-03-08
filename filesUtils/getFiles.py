# coding=utf-8
# encoding=utf-8

##作用：热更根据所需项目目录之下的cmpFiles选择保留的更新文件。
#cmpFiles 只作为索引，实际文件还是以_tempout里面的文件为参考对象
#为什么选择用files，而不用text，主要是svn导出相关的更新文件，这样操作比较方便而已
#注意事项，暂未发现。
import os, re, sys
import codecs
import shutil

# 用以获取当前的工作目录
cd = os.getcwd()

def main(root = cd,dirname = None):
    if dirname is None:
        print("please enter dirname, for example: dsHg")
        return
    cmpDir =  os.path.join(os.path.join(root, dirname))
    srcDir = os.path.join(os.path.join(root, dirname))
    destDir = os.path.join(os.path.join(root, "out"))
    allfiles = getAllFilesList(root)

    #先清空目标文件夹
    if os.path.exists(destDir):
        shutil.rmtree(destDir)
    for basePath in allfiles:
        srcPath = os.path.join(srcDir, basePath)
        destPath = os.path.join(destDir, basePath)
        if os.path.exists(srcPath) :
            mkdirs(destPath)
            shutil.copyfile(srcPath,destPath)
        else:
            print('file not exist:',srcPath)

def getAllFilesList(cmpDir):
    allfiles = []
    with codecs.open(os.path.join(cmpDir, "cmpFiles.txt"), 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = trip(line)
            allfiles.append(line)
    return allfiles

def trip(str):
    return str.strip()

#创建对应的目录
def mkdirs(file):
    path = os.path.dirname(file)
    path = path.strip()
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        return False

if __name__ == "__main__" :
        dirname = "files"
        main(cd,dirname)
