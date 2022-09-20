
Prague = ("Prague",1000)

#print(type(Prague))

Wien = ("Wien",1100)
Brno = ("Brno",2000)
Svitavy = ("Svitavy",1500)
Zlin = ("Zlin",2300)
Ostrava = ("Ostrava",3400)

destinace = [Prague,Wien,Brno,Svitavy,Zlin,Ostrava]
#print(destinace)
#exit()

print('='*20)
print('Welcome to the DESTINATIO, place where people plan their trips')
print('='*20)
print('We can offer you the following destinations:')
print('_'*20)
#print(f'1 {Prague[0]} | {Prague[1]}')
#primitivnejsi zpusob tisku do konzole
print("1",Prague[0]," | ",Prague[1])
#TODO: predelat na fstring a doplnit destinace a ceny z tuple
print('2 Wien | 1100')

print('3 Brno | 2000')

print('4 Svitavy | 1500')

print('5 Zlin | 2300')

print('6 Ostrava | 3400')


print('_'*20)
nr_destination = int(input('Please, enter the destination number to select:'))
index_destinace = nr_destination -1
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
print('We have made your reservation to', destinace[index_destinace][0])
print('The total price is', destinace[index_destinace][1])
