from timeit import default_timer as dt
from requests import get

time = dt()

for i in range(1,10000):
    get('http://127.0.0.1:5000/').content

print(dt()-time)
