#hlavní slovník
database = {'id123': {},'id124': {},'id125': {}}
print(database)

#And here are the others:
first_dict = {'name': 'Thomas', 'age': 45, 'Country': 'Czechia', 'City': 'Brno'}
second_dict = {'name': 'Daniel', 'age': 34, 'Country': 'Czechia', 'City': 'Prague'}
third_dict = {'name': 'Eva', 'age': 43, 'Country': 'Czechia', 'City': 'Olomouc'}

database.update(id123 = first_dict, id124 = second_dict, id125 = third_dict)

print(first_dict)
print(second_dict)
print(third_dict)
print(database)


