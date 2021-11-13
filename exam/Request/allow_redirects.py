from requests import get

r = get('https://google.com', allow_redirects=False)

print(r.url)

r = get('https://google.com', allow_redirects=True)

print(r.url)
