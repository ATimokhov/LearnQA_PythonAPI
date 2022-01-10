import requests
import json
import time

# Создаем задачу
response_get = requests.get("https://playground.learnqa.ru/api/longtime_job")
print(f'Получаем токен и тайминг: {response_get.text} - {response_get.status_code}')
# Парсим ответ
obj = json.loads(response_get.text)
token_value = obj["token"]
token_params = {"token": token_value}
sleep_time = obj["seconds"]

# Создаем реквест с токеном без ожидания
response_get = requests.get("https://playground.learnqa.ru/api/longtime_job", params=token_params)
print(f'Делаем реквест без ожидания: {response_get.text} - {response_get.status_code}')

# Создаем реквест с ожиданием
time.sleep(sleep_time)
response_get2 = requests.get("https://playground.learnqa.ru/api/longtime_job", params=token_params)
obj_final = json.loads(response_get2.text)
true_result = "result"
true_status = "Job is ready"
if true_result in obj_final:
    if true_status == obj_final["status"]:
        print(f'Делаем реквест с ожиданием {sleep_time} сек. : {response_get2.text} - {response_get2.status_code}')
    else:
        print(f"status не соответствует")
else:
    print(f"Нет result")