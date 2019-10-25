import requests

# Послать запросы к своему сайту 1000 шт.
# 

r = requests.get('https://google.com/')
print(r.text)

