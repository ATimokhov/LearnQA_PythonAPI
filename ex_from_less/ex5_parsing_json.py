import requests
import json

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'

parsed_data = json.loads(json_text)
array = 1

print(parsed_data['messages'][array]['message'])