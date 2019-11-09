import requests


step = 0
while step < 1000:
	r = requests.get("http://skillbox.ru")
	step += 1
	print(r)