data = {'user1': 'password1', 'Mark': '1234', 'Danny': 'qwert'}

get_name = input('Please enter username:')

get_password = input('Please enter password: ')

if get_password == data['Mark']:
    print('Permission granted')
elif get_password == data['Danny']:
    print('Permission granted')
elif get_password == data['user1']:
    print('Permission granted')
else:
    print('Password or username is wrong')

# po kontrole si uvědomuji chybu s libovolným username nepárujícím se s heslem