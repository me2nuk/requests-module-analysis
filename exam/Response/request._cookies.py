from requests import get

r = get('http://httpbin.org/get')

print(r.request._cookies)
