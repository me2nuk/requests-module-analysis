from requests import post

files = {'file':open('/etc/passwd', 'rb')}

r = post('http://httpbin.org/post', files=files)

print(r.request.body)
print(r.json())
