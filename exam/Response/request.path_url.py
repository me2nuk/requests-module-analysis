from requests import get

r = get('http://httpbin.org/get')

print(r.request.path_url)
