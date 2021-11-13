from requests import get

r = get('http://httpbin.org/get')

print(r.apparent_encoding)
