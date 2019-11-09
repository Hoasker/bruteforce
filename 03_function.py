# from helper_03_function import check_symbols
import helper_03_function
from os import name

username = 'f43hfiu43$'
email = 'qwe@q%we.ru'

if helper_03_function.check_symbols(['#', '$#', '@'], username):
    print('username has restricted symbols')
if helper_03_function.check_symbols(restricted_symbols=['#', '$#', '%'], s=email):
    print('email has restricted symbols')

print(name)
