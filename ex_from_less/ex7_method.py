import requests
# тест методов
# response_post = requests.post("https://playground.learnqa.ru/api/compare_query_type", data={"method": "POST"})
# response_get = requests.get("https://playground.learnqa.ru/api/compare_query_type", params={"method": "GET"})
# response_put = requests.put("https://playground.learnqa.ru/api/compare_query_type", data={"method": "PUT"})
# response_delete = requests.delete("https://playground.learnqa.ru/api/compare_query_type", data={"method": "DELETE"})
# print(f'{response_post.text} - {response_post.status_code}')
# print(f'{response_get.text} - {response_get.status_code}')
# print(f'{response_put.text} - {response_put.status_code}')
# print(f'{response_delete.text} - {response_delete.status_code}')

# 1 http-запрос любого типа без параметра method
response_post1 = requests.post("https://playground.learnqa.ru/api/compare_query_type")
print(f'#1 Без параметра method: {response_post1.text} - Status CODE: {response_post1.status_code}')

# 2 Делает http-запрос не из списка. Например, HEAD.
response_head = requests.head("https://playground.learnqa.ru/api/compare_query_type", data={"method": "HEAD"})
print(f'#2 http-запрос не из списка. Например, HEAD: {response_head.text} - Status CODE: {response_head.status_code}')

# 3 Запрос с правильным значением method
response_post = requests.post("https://playground.learnqa.ru/api/compare_query_type", data={"method": "POST"})
print(f'#3 Запрос с правильным значением method: {response_post.text} - Status CODE: {response_post.status_code}')

# 4 циклы
print('#4 циклы')
dict1 = {"POST": 1, "PUT": 2, "DELETE": 3, "GET": 4}
#keys = dict1.keys()

for keys in dict1:
    response_post4 = requests.post("https://playground.learnqa.ru/api/compare_query_type", data={"method": keys})
    print(f'POST REQUEST RESPONSE: {response_post4.text} | CODE: {response_post4.status_code} | with params: {keys}')
for keys in dict1:
    response_put4 = requests.put("https://playground.learnqa.ru/api/compare_query_type", data={"method": keys})
    print(f'PUT REQUEST RESPONSE: {response_put4.text} | CODE: {response_put4.status_code} | with params: {keys}')
for keys in dict1:
    response_delete4 = requests.delete("https://playground.learnqa.ru/api/compare_query_type", data={"method": keys})
    print(f'DELETE REQUEST RESPONSE: {response_delete4.text} | CODE: {response_delete4.status_code} | with params: {keys}')
for keys in dict1:
    response_get4 = requests.get("https://playground.learnqa.ru/api/compare_query_type", params={"method": keys})
    print(f'GET REQUEST RESPONSE: {response_get4.text} | CODE: {response_get4.status_code} | with params: {keys}')