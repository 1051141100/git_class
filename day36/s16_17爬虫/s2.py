import requests
from bs4 import BeautifulSoup


# 1. 获取token和cookie
r1 = requests.get(url='https://github.com/login')
s1 = BeautifulSoup(r1.text, 'html.parser')
val = s1.find(attrs={'name': 'authenticity_token'}).get('value')
# cookie返回给你
r1_cookie_dict = r1.cookies.get_dict()



# 2. 发送用户认证
r2 = requests.post(
    url='https://github.com/session',
    data={
        'commit': 'Sign in',
        'utf8': '✓',
        'authenticity_token': val,
        'login': 'xxxxx',
        'password': 'xxxx',

    },
    cookies=r1_cookie_dict
)
r2_cookie_dict = r2.cookies.get_dict()  # {}


all_cookie_dict = {}
all_cookie_dict.update(r2_cookie_dict)
all_cookie_dict.update(r1_cookie_dict)


r3 = requests.get(
    url='自己个人信息页面',
    cookies=all_cookie_dict
)

print(r3.text)  # 登录成功之后，可以查看的页面