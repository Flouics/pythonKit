# coding=utf-8
# encoding=utf-8

##作用：遍历files里面文件，找出包含的中文，输出到out.txt里面。
# 存在的问题

import os, re, sys
import codecs

# 用以获取当前的工作目录
cd = os.getcwd()
fileDir = os.path.join(cd, "files")


def main():
    excludeFileTypeList = [".ds_store", ".py", ".sublime-project", ".sublime-workspace", ".sublime-workspace"]
    with codecs.open(os.path.join(cd, "cmpFilesSrc.txt"), 'r', ) as rf:
        with codecs.open(os.path.join(cd, "cmpFiles.txt"), 'wb', ) as wf:
            lines = rf.readlines()
            for line in lines:
                find_chinese_str = getChineseString(line)
                if find_chinese_str == "" and len(re.findall("DsHgDesign", line)) == 0:
                    fname, fename = os.path.splitext(line)
                    if fename != "" and trip(fename).lower() not in excludeFileTypeList:
                        matchObj = re.match(r'(.*) (/.*)', line)
                        if matchObj:
                            wr_line = matchObj.group(2).replace('/res/skin/dsHg/','')
                            wf.write(wr_line + "\n")


def trip(str):
    return str.strip()


def getChineseString(str, need_decode=True):
    findret = ""
    if need_decode:
        str = str.decode('utf-8')
    for _char in str:
        if u'\u4e00' <= _char and _char <= u'\u9fa5':
            findret += _char.encode('utf-8')
    return findret


main()
