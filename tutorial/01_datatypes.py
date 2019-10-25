a = 1 /3
a = a + 2

print(a)

print(type(a))

print(a + a + a)

b_true = True
b_false = False


if a + a + a == 7.000000000000000000001:
	print("okay")
else:
	print("Not okay")


a = None

s = '12345678'
print(type(s))
s = 'Hello ' + 'World'
print(s)

s = f"Value of {a}"
print(s)

print(s[10:-5])

list_of_something = [1, 2, 3, 4, 'abc', ['1', True]]
print(list_of_something)
print(list_of_something[0])
print(list_of_something[5][0])
print(list_of_something[3:-1])


dictionary = {
	'key': 'value',
	'Moscow': 'Москва',
	'l': list_of_something 
}

print(dictionary)
print(dictionary['l'])
print(dictionary['l'][5][0])

