if 8 / 3  == 2:
	print('ok 1')
elif 8 / 3 == 3:
	print('not ok')
else:
	print('not ok')

password = '54321' # not known

if not password:
	true_password = '12345'
else:
	true_password = password


true_password = password if password else '12345'
print(true_password)



for i in [1, 2, 3, 4, 5, 6]:
	print(i * i)

for i in range(1, 11):
	if i % 2 == 0:
		print(i * i)


lc = [i * i for i in range(1, 11) if i % 2 == 0]
print(lc)


i = 0
while len(str(i)) < 3:
	print(i)
	i += 1

