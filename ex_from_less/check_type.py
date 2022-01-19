import requests

response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1":"value32"})
print(response.text)

