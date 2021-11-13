from requests import get

r = get("http://httpbin.org/get", timeout=1)

print(r.text)
