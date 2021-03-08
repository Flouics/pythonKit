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
    allfiles = []
    allKeysDict = {}

    for root, dirs, files in os.walk(fileDir):
        for dir in dirs:
            # 遍历文件夹
            print(os.path.join(root, dir))

        for file in files:
            allfiles.append(os.path.join(root, file))

    with codecs.open(os.path.join(cd, "out//keys.txt"), 'r', encoding='utf-8') as keys_f:
        lines = keys_f.readlines()
        for line in lines:
            line_arr = line.split("=")
            if len(line_arr) > 1:
                allKeysDict[trip(line_arr[0])] = trip(line_arr[1])

    with codecs.open(os.path.join(cd, "out//diff_files.txt"), 'w', encoding='utf-8') as diff_f:
        with codecs.open(os.path.join(cd, "out//keys.txt"), 'a', encoding='utf-8') as keys_f:
            with codecs.open(os.path.join(cd, "out//keys_new.txt"), 'w', encoding='utf-8') as keys_new_f:
                keyDict = {}
                filesList = []
                for path in allfiles:
                    dict = deal_file(path)
                    if len(dict.keys()) > 0:
                        keyDict.update(dict)
                        filesList.append(path)

                # 格式化输出
                # 需要修改的文件类型
                str = ""
                for path in filesList:
                    str = path.decode('utf-8') + "\n"
                    diff_f.write(str)

                # 需要修改的文件类型
                for k, v in keyDict.items():
                    if not allKeysDict.has_key(trip(k)):
                        str_format = k + " = {0}\n"
                        keys_f.write(str_format.format(k))
                        keys_new_f.write(str_format.format(""))

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


'''
def deal_file(path):
    pattern = r'(.*[\u4E00-\u9FA5]+)|([\u4E00-\u9FA5]+.*)'
    dict = {}
    with open(path, 'r') as f:
        lines = f.readlines()
        findret = ""
        for line in lines:
            if  len(re.findall('--',line)) == 0:
                findret = getChineseString(line)
                if findret != "":
                    if findret not in dict.keys():
                        dict[findret] = ""

    return dict
'''


def deal_file(path):
    pattern = u"(.*[\u4E00-\u9FA5]+)|([\u4E00-\u9FA5]+.*)"
    dict = {}
    with codecs.open(path, 'rb') as f:
        lines = f.readlines()
        for line in lines:
            if len(re.findall(r'--|print', line)) == 0:
                findlist = re.findall(pattern, line.decode('utf-8'))
                if findlist and findlist[0]:
                    for str in findlist[0]:
                        key_arr = re.split(u'\"|\'|\[|\]', str)
                        for key in key_arr:
                            if key != u"" and getChineseString(key, False) != "":
                                dict[key] = ""

    return dict


main()
