from requests.sessions import Session

sess = Session()

s1 = sess.get('https://www.google.com')
print(s1.cookies)
s2 = sess.post('https://www.google.com')
print(s2.request._cookies)