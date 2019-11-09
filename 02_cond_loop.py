if 8 / 3 == 2:
    print('Ok 1')
elif 8 / 3 == 2.6666:
    print('Ok 2')
elif 8 / 3 == 2.6666666666:
    print('Ok 2')
elif 8 / 3 == 2.66666666666666666:
    print('Ok 2')
else:
    print('Not ok')

password = '54321'  # not known

if not password:
    true_password = '12345'
else:
    true_password = password

true_password = password if password else '12345'
print(true_password)


for i in range(1, 100):
    if i % 2 == 0:
        print(i * i)

lc = [i * i for i in range(1, 100) if i % 2 == 0]
print(lc)


i = 0
while len(str(i)) < 10:
    print(i)
    i += 1  # i = i + 1
