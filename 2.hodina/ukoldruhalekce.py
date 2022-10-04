#variable_name = expression1 if condition else expression2

my_str = 'Python'
result = ''

if my_str.istitle():
    result='Titlecased'

else:
    result = 'Not titlecased'

print(result)


my_str = 'python'
result = 'Titlecased' if my_str.istitle() else 'Not titlecased'
print(result)