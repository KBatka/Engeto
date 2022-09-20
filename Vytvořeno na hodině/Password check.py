data = {'user1': 'password1', 'Mark': '1234', 'Danny': 'qwert'}

username = str(input('Please enter username:'))
password = str(input('Please enter password'))

if username and password in data.items:
    print('Permission granted')
else: print('Password or username is wrong')