from django.shortcuts import render,HttpResponse
import requests
import re
import time


def login(req):

    # ctime = time.time()*1000
    #
    # qcode_url = "https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={0}".format(ctime)
    # r1 = requests.get(qcode_url)
    # # print(r1.text) # window.QRLogin.code = 200; window.QRLogin.uuid = "Idm9DGWY_A==";
    # data = re.findall('uuid = "(.*)";', r1.text)
    # qcode = data[0]
    qcode = 'sdfdf'
    return render(req,'login.html',{'qcode':qcode})

def check_login(req):
    # 被夯住 30s
    # r1 = requests.get('微信检测是否用户已经扫码的URL')
    # r1.text，内容中含有408，表示用户30s未扫码
    # r1.text，内容中含有302，表示用户已经扫码，把用户头像返回
    # r1.text，内容中含有200，表示用户已经扫码，点击确认登录
    time.sleep(10)
    return HttpResponse('...')

