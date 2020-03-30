#startovní pole

'''
author = 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

i = ''

print("_ _"*50)
print('Welcome to the app. Please login in')

names = ['bob','ann','mike','liz']
login = ['123','pass123','password123','pass123']

username = input('USERNAME:')
password = input('PASSWORD:')

while True:
    if username == names[0]:
        password is login[-3]
        if password not in login[-3]:
            print('wrong password')
    if username == names[1]:
        password is login[1]
        if password not in login[1]:
            print('wrong password')
    if username == names[2]:
        password is login[2]
        if password not in login[2]:
            print('wrong password')
    if username == names[3]:
        password is login[3]
        if password not in login[3]:
            print('wrong password')
    if password == '':
            print('please write something')
    print('Welcome, enjoy')
    break

print("_ _"*50)

print('We have three texts to be analysed.')
handler = input('Enter a number btw. 1 - 3 to select:')
#kod pro a) výběr objektu v listu, b) vyhodnocení 5 požadavků

print('There are',nr_of_words,'words in the selected text.')
print('There are',nrcapitalltr,'titlecased words')
print('There are',nrupwrds,'uppercase words')
print('There are',nrlcwrds,'lowercase words')
print('There are',nrnumonly,'numeric strings')

print("_ _"*50)
#tabulka ->pracuji s handlerem
#počítá délku slov a jejich četnost v jednotlivých objektech
#tolik řádků jako je zastoupení jednotlivých slov, tzn. třeba pětiznakové můžou chybět
# (napsat tak, aby se samo korigovalo nebo pro každý blok zvlášť? wtf how?)
print("_ _"*50)

print('If we summed all the numbers in this text we would get:'#sum hodnoty všech numer objektů)