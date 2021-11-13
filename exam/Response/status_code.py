from requests import get

r = get('http://httpbin.org/get')

print(r.status_code)