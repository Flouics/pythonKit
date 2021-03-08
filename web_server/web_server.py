from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler


# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = HTTPServer(("", 8080),SimpleHTTPRequestHandler)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()