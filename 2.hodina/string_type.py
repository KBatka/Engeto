gimme = str(input('Give me some input:'))

print(type(gimme))

if gimme.isdecimal():
    print('Numeric')
elif gimme.isalpha():
    print('Letters Only')
else:
    print('Mixed')



