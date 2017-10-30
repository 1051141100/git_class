from scrapy.utils.request import request_fingerprint
from scrapy.http import Request


obj1 = Request(url='http://www.baidu.com?a=1&b=2',headers={'Content-Type':'application/text'},callback=lambda x:x)
obj2 = Request(url='http://www.baidu.com?b=2&a=1',headers={'Content-Type':'application/json'},callback=lambda x:x)

v1 = request_fingerprint(obj1,include_headers=['Content-Type'])
print(v1)

v2 = request_fingerprint(obj2,include_headers=['Content-Type'])
print(v2)




