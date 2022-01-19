import pytest
import requests
#resp_header1 = requests.get("https://playground.learnqa.ru/api/homework_header")
#header_value1 = dict(resp_header1.headers)
#print(f"Значение headers = {header_value1}")

class TestCheckHeader:
    def test_check_value_headers(self):
        resp_header = requests.get("https://playground.learnqa.ru/api/homework_header")
        header_value = dict(resp_header.headers)
        secret_header_value = header_value["x-secret-homework-header"]
        print(f"Значение headers = {secret_header_value}")
        assert secret_header_value == "Some secret value", f"Значение 'x-secret-homework-header' не равно {secret_header_value}"
