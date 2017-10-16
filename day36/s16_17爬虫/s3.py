
"""
1.
    r0 = request.get()
    r0_cookie_dict = r0.cookies.get_dict()


2.
    r1 = requests.post(
        url="http://dig.chouti.com/login",
        data={
            'phone':'xxx',
            'password':'xx',
            'oneMonth':1
        },
        cookies=r0_cookie_dict
    )

    print(r1.text)

    r1_cookie_dict = r1.cookies.get_dict()



3.
    r2 = requests.post(url='http://dig.chouti.com/link/vote?linksId=14708366',cookies=r0_cookie_dict)
    r2.text

问题：自动登录并点赞

"""