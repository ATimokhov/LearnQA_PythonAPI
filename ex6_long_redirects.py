import requests
response1 = requests.get(" https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
redirects = response1.history
number_of_elements = len(redirects)
print(f'Кол-во редиректов: {number_of_elements}')
print(f'Итоговый URL: {response1.url} ')

