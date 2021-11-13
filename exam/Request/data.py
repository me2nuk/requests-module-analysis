from requests import post

r = post('http://httpbin.org/post', data={'data1':'value'})

print(r.json())
print(r.request.body)
