from requests import get

def response_method(res, **kwargs):
    print(f'kwargs : {kwargs}')
    print(f'res : {res}')
    print(f'res.status_code : {res.status_code}')

r = get('http://httpbin.org/get', hooks={'response':response_method})
