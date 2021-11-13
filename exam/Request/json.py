from requests import post

r = post('http://httpbin.org/post', json={'jsondata':'value'})

print(r.request.headers['Content-Type'])
print(r.request.body)
