from requests import get

r = get('http://httpbin.org/get', headers={'test':'value'})

print(r.request.headers)
