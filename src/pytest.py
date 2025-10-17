import httpx

url = "http://127.0.0.1:3030/api/v1/fact/me"
for i in range(1,8):
    data = httpx.get(url)
    print(f"Request {i} : status: {data.status_code} : response : {data.text}")