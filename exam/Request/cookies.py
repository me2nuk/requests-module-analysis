from requests import get

r = get('http://httpbin.org/get', cookies={'cookie_test':'value'})

print(r.request._cookies)
