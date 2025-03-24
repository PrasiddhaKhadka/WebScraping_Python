import requests

proxies={
    "http":"https://47.251.122.81:8888",
    # "http":"http://168.80.25.31:8000",
    # "http":"https://172.245.198.243:8000",
    # "http":"https://177.234.137.176:8000",
    
}

r = requests.get("https://api.ipify.org?format=json",proxies=proxies)
print(r.json())