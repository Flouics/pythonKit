#coding=utf-8

##作用：读取replace.txt，替换掉files需要替换的文字，然后输出到outFiles文件夹。

import os,re,sys
import codecs

cd = os.getcwd()
fileDir = os.path.join(cd, "files")
outDir = os.path.join(cd, "outFiles")
# secs = conf.sections()  # 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，

def main():
    allFilesList = []
    allKeysDict = {}
    with codecs.open(os.path.join(cd, "out//diff_files.txt"), 'r') as diff_f:
        lines = diff_f.readlines()
        for line in lines:
            allFilesList.append(trip(line))

    with codecs.open(os.path.join(cd, "out//keys.txt"), 'r', encoding='utf-8') as keys_f:
        lines = keys_f.readlines()
        for line in lines:
            line_arr = line.split("=")
            if len(line_arr) > 1:
                allKeysDict[trip(line_arr[0])] = trip(line_arr[1])

    for file in allFilesList:
        newfile = file.replace("files","outFiles")
        mkdirs(newfile)
        pattern = u"(.*[\u4E00-\u9FA5]+)|([\u4E00-\u9FA5]+.*)"
        with codecs.open(file, 'r',encoding='utf-8') as f:
            with codecs.open(newfile, 'w',encoding='utf-8') as newf:
                lines = f.readlines()
                for line in lines:
                    findlist = re.findall(pattern, line)
                    if findlist and findlist[0]:
                        for str in findlist[0]:
                            key_arr = re.split(u'\"|\'|\[|\]', str)
                            for key in key_arr:
                                if key != u"" and getChineseString(key, False) != "" :
                                    if allKeysDict.has_key(key):
                                        line = line.replace(key,allKeysDict[key])
                    newf.write(line)

def getChineseString(str, need_decode=True):
    findret = ""
    if need_decode:
        str = str.decode('utf-8')
    for _char in str:
        if u'\u4e00' <= _char and _char <= u'\u9fa5':
            findret += _char.encode('utf-8')
    return findret


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


#获取对应块的键值
def getReplaceOptions(section_str):
    options = conf.options(section_str)  # 获取某个section名为Mysql-Database所对应的键
    return options

#获取对应块的值
def getReplaceOptionValue(section_str,key):
    value = conf.get(section_str,key)  # 获取某个section名为Mysql-Database所对应的键
    return value

main()