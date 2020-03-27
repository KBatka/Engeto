#variable_name = expression1 if condition else expression2

my_str = 'Python'
result = ''

if my_str.istitle():
    result = print('Titlecased')
else:
    result = print('Not titlecased')

my_str = 'Python'
result = print('Titlecased') if my_str.istitle() else print('Not titlecased')

#ptá se mne, zda je první písmeno velké, nebo všechna?

#rozpracováno