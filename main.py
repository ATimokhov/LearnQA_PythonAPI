#committest
import requests
response = requests.get("https://playground.learnqa.ru/api/get_text")
test = response.text
print("Hello from Andrey. Text from GET request: " + test)
