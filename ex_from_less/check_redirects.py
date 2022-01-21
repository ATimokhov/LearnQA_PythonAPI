import requests

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_resp = response.history[0]
second_resp = response

print(first_resp.url)
print(second_resp.url)