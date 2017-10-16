from bs4 import BeautifulSoup

html_doc = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <div id='i1'>
            <a>sdfs</a>
        </div>
        <p class='c2'>asdfa</p>
    </body>
</html>
"""

# from bs4.element import Tag
# soup = BeautifulSoup(html_doc, features="html.parser")
#
# obj1 = Tag(name='div', attrs={'id': 'it'})
# obj1.string = '我是一个新来的'
#
# tag = soup.find('a')
#
# v = tag.wrap(obj1)
# print(soup)

from bs4.element import Tag
# soup = BeautifulSoup(html_doc, features="html.parser")
#
# tag = soup.find('a')
# v = tag.unwrap()
# print(soup)


# from bs4.element import Tag
# soup = BeautifulSoup(html_doc, features="html.parser")
# obj = Tag(name='i', attrs={'id': 'it'})
# obj.string = '我是一个新来的'
# tag = soup.find('body')
# tag.insert_before(obj)
# # tag.insert_after(obj)
# print(soup)

# soup = BeautifulSoup(html_doc, features="html.parser")
# tag = soup.find(attrs={'class':'c2'})
#
# import copy
# new_tag = copy.deepcopy(tag)
#
# soup.find(id='i1').append(new_tag)
# print(soup)

# from bs4.element import Tag
# soup = BeautifulSoup(html_doc, features="html.parser")
#
# tag = Tag(name='i',attrs={'id': 'it'})
# tag.string = "asdfasdf"
#
# soup.find(id='i1').append(tag)
# print(soup)



# print(tag.text)
# print(list(tag.stripped_strings))

# print(tag.string)
# for item in tag.children:
#     print(item,type(item))


# print(tag.next)
# print(list(tag.next_elements))

# print(tag.previous)
# print(list(tag.previous_elements))


# print(tag.previous_sibling)
# print(list(tag.previous_siblings))

# print(tag.next_sibling)
# print(list(tag.next_siblings))



# 1. name
# soup = BeautifulSoup(html_doc, features="html.parser")
# tags = soup.find_all(attrs={'class':'c1'})
# for tag in tags:
#     print(tag.name)

# 2. attrs,获取属性；删除，增加，修改
# soup = BeautifulSoup(html_doc, features="html.parser")
# # tag = soup.find(attrs={'class':'c1'})
# tag = soup.find(class_='c1')
# print(tag)
#
# tag.attrs['id'] = 1
# del tag.attrs['class']
# print(tag)
#
# # 3. children是找所有孩子
# soup = BeautifulSoup(html_doc, features="html.parser")
# tag = soup.find(attrs={'class':'c1'})
# print(list(tag.children))


# 4. descendants是找所有后代
# soup = BeautifulSoup(html_doc, features="html.parser")
# tag = soup.find(attrs={'class':'c1'})
# print(list(tag.descendants))

# ps:找后代
# soup = BeautifulSoup(html_doc, features="html.parser")
# tag = soup.find(attrs={'class':'c1'})
# print(tag.find_all(recursive=False))
# print(tag.find_all(recursive=True))
#
# soup = BeautifulSoup(html_doc, features="html.parser")
# tag = soup.find(attrs={'class':'c1'})
#
# # print(tag)
#
# print(tag.decode())   # 对象变成字符串
# # print(tag.encode()) # 对象变成字节
# from bs4.element import Tag
#
# # tag.get_text()
# # tag.text
