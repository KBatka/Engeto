prevod_pismenek=str(input("Napiš prosím libovolné slovo")).lower()

print("Převedeno na:", prevod_pismenek)

#indexing
my_str="indexing"
list(my_str)

first_five = my_str[:5]
last_five = my_str [3:]
each_third = my_str[0::3]

print("Indexing:", first_five,",", last_five,",", each_third)

print("First five letters:" + first_five)
print("Last five letters:" + last_five)
print("Each third letter:" + each_third)

#Name, surname, full_name
#řeším
name = (input("Please insert your first name:"))
print("Name:" + name)
surname = (input("Please insert your surname:"))
print("Surname:" + surname)
full_name = name + surname
print("Full name:" + full_name)


name_length = len(name+surname)
print("Length of full name:" + name_length)

print("="*len(full_name))
print(full_name)
print("="*len(full_name))