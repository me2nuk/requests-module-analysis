from requests import get

r = get("http://httpbin.org/get")

r.raise_for_status()

print("found url")

r = get("http://httpbin.org/not-found")

r.raise_for_status()

print("not found url")
