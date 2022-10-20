
Prague = ("Prague",1000)
Wien = ("Wien",1100)
Brno = ("Brno",2000)
Svitavy = ["Svitavy",1500]
Zlin = ("Zlin",2300)
Ostrava = ["Ostrava",3400]
destinace =[Prague,Wien,Brno,Svitavy,Zlin,Ostrava]

print('='*20)
print('Welcome to the DESTINATIO, place where people plan their trips')
print('='*20)
print('We can offer you the following destinations:')
print('_'*20)
#print(f'1 {Prague[0]} | {Prague[1]}')
#primitivnejsi zpusob tisku do konzole
print("1",Prague[0]," | ",Prague[1])
print("2", Wien [0],"|", Wien[1])
print("3", Brno [0],"|", Brno [1])
print("4", Svitavy [0],"|", Svitavy[1])
print("5", Zlin [0], "|", Zlin[1])
print("6", Ostrava [0], "|", Ostrava [1])

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
#2022
birth = int(input('YEAR of BIRTH:'))
if birth >= 2007:
    print("We cannot provide our services to clients under 15 years of age")

print('='*20)


def input_valid_mail():
  mail = input('EMAIL:')
  if "@" not in mail:
    print("Please enter valid email")
    input_valid_mail()


input_valid_mail()

print('='*20)
#Password has to be at least 8 chars long, cannot begin and end with a number and has to contain both letters and numbers
password = input('PASSWORD:')
delka = len(password)

if delka <= 8:
    print("short")
elif password.isalpha():
    print("has to contains numbers")
elif password[0].isdigit():
    print("cannot begin with a number")
elif password[-1].isdigit():
    print("cannot end with a number")

#TODO: rekurzivni funkce podobne jako input_valid_mail nebo bool promena is_valid a nakonec otestovat a exit()

print('='*20)
print('Thank you', name,"",surname)
print('We have made your reservation to', destinace[index_destinace][0])
print('The total price is', destinace[index_destinace][1])
