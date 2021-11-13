from requests import post

r = post('http://httpbin.org/post', auth=('username','password'))

print(r.request.headers)
print(r.request.headers['Authorization'])
