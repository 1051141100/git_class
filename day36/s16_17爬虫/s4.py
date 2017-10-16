import requests


# 1. requests.request
# requests.get(url,params)
# requests.request(method='get',url='xx')
#
# requests.post(url,params,data,cookie)
# requests.request(method='post',url='xx')

requests.request(
    method='POST',
    url='xxx',
    params={},
    data={}, #json
)

# data参数,(json)
import json
requests.post(url='xxx',data={'name':'alex','age':18}) # content-type: application/www-form-endoc...
requests.post(url='xxx',data="name=alex&age=18")       # content-type: application/www-form-endoc...


requests.post(url='xxx',data=json.dumps({'name':'alex','age':18}),headers={'Content-type':'application/json'})
requests.post(url='xxx',json={'name':'alex','age':18})

# headers,请求头


# cookies，Cookie

"""
1. method
2. url
3. params
4. data
5. json
6. headers
7. cookies
8. files
9. auth
10. timeout
11. allow_redirects
12. proxies
13. stream
14. cert
================ session,保存请求相关信息（不推荐）===================
import requests

session = requests.Session()

i1 = session.get(url="http://dig.chouti.com/help/service")
i2 = session.post(
    url="http://dig.chouti.com/login",
    data={
        'phone': "8615131255089",
        'password': "xxooxxoo",
        'oneMonth': ""
    }
)
i3 = session.post(
    url="http://dig.chouti.com/link/vote?linksId=8589523"
)
print(i3.text)

"""



# 8. files,文件上传
# requests.post(url='xx',files=())

# 9. auth，用户认证
# from requests.auth import HTTPBasicAuth, HTTPDigestAuth
# ret = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('wupeiqi', 'sdfasdfasdf'))
# print(ret.text)


# from contextlib import closing
# with closing(requests.get('http://httpbin.org/get', stream=True)) as r:
#     # 在此处理响应。
#     for i in r.iter_content():
#         print(i)







