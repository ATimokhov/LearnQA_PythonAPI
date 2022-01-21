import pytest
import requests

class TestUAgent:
    data = [
        ({'user_agent': 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
          'platform': 'Mobile', 'browser': 'No', 'device': 'Android'}),
        ({'user_agent': 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
          'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'}),
        ({'user_agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
          'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'}),
        ({'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0',
          'platform': 'Web', 'browser': 'Chrome', 'device': 'No'}),
        ({'user_agent': 'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
          'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'})
    ]
    @pytest.mark.parametrize('ua_data', data)
    def test_u_agent(self, ua_data):
        ua_resp = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={"User-Agent": ua_data['user_agent']})
        assert ua_resp.json()['platform'] == ua_data['platform'], f"Значение {ua_resp.json()['platform']} не равно ожидаемому {ua_data['platform']}"
        assert ua_resp.json()['browser'] == ua_data['browser'], f"Значение {ua_resp.json()['browser']} не равно ожидаемому {ua_data['browser']}"
        assert ua_resp.json()['device'] == ua_data['device'], f"Значение {ua_resp.json()['device']} не равно ожидаемому {ua_data['device']}"