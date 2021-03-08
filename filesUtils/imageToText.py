import urllib.request
import urllib.parse
import json
import time
import base64
import os,sys
import shutil
# 用以获取当前的工作目录
cd = os.getcwd()
sys.path.append('../')
from common import utils

AppCode = "eca22ce80d9c4cbaac530cfa053f1b69"

def main(root = cd,dirname = None):
    if dirname is None:
        print("please enter dirname, for example: dsHg")
        return
    fileDir =  os.path.join(os.path.join(root, dirname))
    outDir = os.path.join(os.path.join(root, "i2tOut"))
    print("outDir",outDir)
    utils.removedirs(outDir)
    for root, dirs, files in os.walk(fileDir):
        for dir in dirs:
            # 遍历文件夹
            #print(os.path.join(root, dir))
            pass
        for file in files:
            filePath = os.path.join(root, file)
            result =  getImageToTextReslut(filePath)
            if result and result["prism_wnum"] > 0:
                outPath = filePath.replace(fileDir,outDir)
                utils.mkdirs(outPath)
                shutil.copyfile(filePath, outPath)

def getImageToTextReslut(filePath):
    print("check file" + filePath)
    result = None
    with open(filePath, 'rb') as f:  # 以二进制读取本地图片
        data = f.read()
        encodestr = str(base64.b64encode(data),'utf-8')
        dict = {'img': encodestr}
        url_request = "https://ocrapi-advanced.taobao.com/ocrservice/advanced"
        result = posturl(url_request, data=dict)
        print(result)
    return json.loads(result)

def posturl(url, data={}):
    # 请求头
    # 请修改为你自己的appcode，可从云市场订单或者api网关处获得
    headers = {
        'Authorization': 'APPCODE ' + AppCode,
        'Content-Type': 'application/json; charset=UTF-8'
    }
    try:
        params = json.dumps(data).encode(encoding='UTF8')
        req = urllib.request.Request(url, params, headers)
        r = urllib.request.urlopen(req)
        html = r.read()
        r.close();
        return html.decode("utf8")
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read().decode("utf8"))
    time.sleep(1)

if __name__=="__main__":
    dirname = "image2text"
    main(cd, dirname)