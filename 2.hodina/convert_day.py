ot = input('Please enter the number of the day(1-7):')

if ot == '1':
    print('Monday')
elif ot == '2':
    print('Tuesday')
elif ot == '3':
    print('Wednesday')
elif ot == '4':
    print('Thursday')
elif ot == '5':
    print ('Friday')
elif ot == '6':
    print('Saturday')
elif ot == '7':
    print('Sunday')
elif ot.isalpha():
    print('Enter only numbers please')
elif ot == '':
    print('No input provided')
else:
    print('only nrs between 1-7')

#aneb jak si vymyslet vlastní řešení :D
