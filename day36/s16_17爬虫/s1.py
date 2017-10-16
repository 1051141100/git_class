import requests
from bs4 import BeautifulSoup

# http方式
response = requests.get('http://www.autohome.com.cn/news/')
# response.encoding='gbk'
# print(response.text)

# 文件方式
with open('autohome_new_txt','r',encoding='utf-8') as f:
    data = f.read()

soup = BeautifulSoup(data,'html.parser')
tag = soup.find(name='div',attrs={'id':'auto-channel-lazyload-article'})

li_list = tag.find_all('li') # [标签对象,标签对象]
for li in li_list:
    h3 = li.find(name='h3')
    if not h3:
        continue
    print(h3.text,li.find(name='a').get('href'))
    #print(li.find(name='a').attrs['href'])
    # print(li.find('p').text)

    img_url = li.find('img').get('src')
    print(img_url)

    res = requests.get('http:'+img_url)

    with open('xxxx.jpg','wb') as f:
        f.write(res.content)