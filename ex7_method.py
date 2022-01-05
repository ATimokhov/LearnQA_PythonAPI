import requests
# https://playground.learnqa.ru/ajax/api/compare_query_type

response_post = requests.delete("https://playground.learnqa.ru/api/compare_query_type")


print(response_post.text)

