from requests import get

r = get("http://httpbin.org/get", params={'params1':'value'})

print(r.url)
