dejdej = input('Please enter the password:')

moje_znaky = ['a','e','f','q','z']

if dejdej.islower() and dejdej[0] in moje_znaky:
        print('Welcome!')
else:
        print('The input does not match')