#coding:utf-8
import sys
sys.path.append("..")
import requests
import pytest

#查询用户权限接口
def test_userRight(get_tokens,get_environments,get_shopId):
    token = get_tokens()
    get_environments = get_environments()
    shopId = get_shopId()
    url = get_environments + 'userRight.do'+'&token='+token+'&shopId='+shopId
    headers = shopId
    r = requests.get(url=url,headers=headers)
    return r

if __name__ == "__main__":
        pytest.main(["-s", "test_userRight.py"])

#print(test_userRight(get_tokens))