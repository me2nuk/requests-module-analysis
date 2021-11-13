from requests import get

r = get('http://httpbin.org/get')

print(r.is_permanent_redire)
