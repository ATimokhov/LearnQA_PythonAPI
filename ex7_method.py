import requests

# тест методов
response_post = requests.post("https://playground.learnqa.ru/api/compare_query_type", data={"method": "POST"})
response_get = requests.get("https://playground.learnqa.ru/api/compare_query_type", params={"method": "GET"})
response_put = requests.put("https://playground.learnqa.ru/api/compare_query_type", data={"method": "PUT"})
response_delete = requests.delete("https://playground.learnqa.ru/api/compare_query_type", data={"method": "DELETE"})
print(f'{response_post.text} - {response_post.status_code}')
print(f'{response_get.text} - {response_get.status_code}')
print(f'{response_put.text} - {response_put.status_code}')
print(f'{response_delete.text} - {response_delete.status_code}')

# 1 http-запрос любого типа без параметра method
response_post1 = requests.post("https://playground.learnqa.ru/api/compare_query_type")
print(f'#1 Без параметра method: {response_post1.text} - Status CODE: {response_post1.status_code}')

# 2 Делает http-запрос не из списка. Например, HEAD.
response_head = requests.head("https://playground.learnqa.ru/api/compare_query_type", data={"method": "HEAD"})
print(f'#2 http-запрос не из списка. Например, HEAD: {response_head.text} - Status CODE: {response_head.status_code}')

# 3 Запрос с правильным значением method
response_post = requests.post("https://playground.learnqa.ru/api/compare_query_type", data={"method": "POST"})
print(f'#3 Запрос с правильным значением method: {response_post.text} - Status CODE: {response_post.status_code}')

# 3 циклы