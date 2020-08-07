#coding:utf-8
#其它程序模块调用的公共header
import requests
import json
import pytest

@pytest.fixture()
def get_header():
	header = {'Connection':'keep-alive','DNT':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Accept':'*/*',
		'Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'}
	return header

#利汇预发环境
@pytest.fixture()
def get_environments():
	environments = "http://pcapi.pre.lihvip.com/"
	return environments
# #利汇测试环境
# def get_environments():
# 	environments = "http://pcapi.test.lihvip.com/"
# 	return environments

#利汇站点id
@pytest.fixture()
def get_shopId():
    shopId = {'shopId':'1000'}
    return shopId

shopId = get_shopId()

#获取后台登录的token
@pytest.fixture()
def get_tokens():
    data = {'phone':'13632656270',
            'passwd':'123456'}
    headers = {
               'shopId':'1000'
               }
    url = get_environments()+'login.do'
    r = requests.post(url=url, data=data, headers=headers)
    return (r.json()["token"])
#print(get_tokens())

