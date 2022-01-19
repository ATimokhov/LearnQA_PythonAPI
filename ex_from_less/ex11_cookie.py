import pytest
import requests

#resp_cookie_test = requests.get("https://playground.learnqa.ru/api/homework_cookie")
#value1 = dict(resp_cookie_test.cookies)
#print(value1)

class TestCheckCookie:
    def test_check_value_cookie(self):
        resp_cookie = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        value = dict(resp_cookie.cookies)
        print(f"Значение cookies = {value}")
        assert value == {"HomeWork": "hw_value"}, f"Cookies {value} не соответствует ожидаемому значению"