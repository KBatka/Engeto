print('='*20)
print('Welcome to the DESTINATIO, place where people plan their trips')
print('='*20)
print('We can offer you the following destinations:')
print('_'*20)
print('1 Prague | 1000')
Prague = 1000
print('2 Wien | 1100')
Wien = 1100
print('3 Brno | 2000')
Brno = 2000
print('4 Svitavy | 1500')
Svitavy = 1500
print('5 Zlin | 2300')
Zlin = 2300
print('6 Ostrava | 3400')
Ostrava = 3400
destinace = ['slot',Prague,Wien,Brno,Svitavy,Zlin,Ostrava]

print('_'*20)
nr_destination = int(input('Please, enter the destination number to select:'))
print('='*20)
print('REGISTRATION:')
print('_'*20)
print('In order to complete your reservations, please share few details about yourself with us.')
print('_'*20)
name = input('NAME:')
print('='*20)
surname = input('SURNAME:')
print('='*20)
birth = input('YEAR of BIRTH:')
print('='*20)
mail = input('EMAIL:')
print('='*20)
password = input('PASSWORD:')
print('='*20)
print('Thank you' + name)
print('We have made your reservation to', nr_destination)
print('The total price is', destinace[nr_destination])
