
import os
import shutil

#创建文件对应的目录
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

#创建相对文件对应的目录
def mkdirs_by_relative(file_relative):
    file_path = file_relative
    if file_relative.startswith('/'):
        file_path = file_relative.replace('/','',1)
    file = os.path.join(os.getcwd(),file_path)
    return mkdirs(file)

# 删除文件夹
def removedirs(path):
    if os.path.exists(path):
        shutil.rmtree(path)