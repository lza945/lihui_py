#  test_sample.py
import requests
import json
# import pytest
# #
# # password = ('123456','abcdefdfs','as52345fasdf4')
# # @pytest.mark.parametrize('passwd',password)
# # def test_passwd_length(passwd):
# #     assert len(passwd) >= 8
def get_environments():
	environments = "http://pcapi.pre.lihvip.com/"
	return environments

url = get_environments()+'login.do'

r = requests.post(url=url, data={"phone":"13632656270","passwd":"123456"}, headers={'shopId': '1000',})
print(r.text)

print(url)