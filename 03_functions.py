def check_symbols(restricted_symbols, s):
	for symbol in restricted_symbols:
		if symb in s:
			return True
	return False

username = 'asdfw$'

if check_symbols(['#', '$#', '@'], =username):
	print('username has restricted symbols')


