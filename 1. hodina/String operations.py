#Name, surname, full_name
name = (input("Please insert your first name:"))
print("Name:" + name)

surname = (input("Please insert your surname:"))
print("Surname:" + surname)

full_name = name + surname
print("Full name:" + full_name)

name_length = str(len(name+surname))
print("Length of full name:" + name_length)

print("="*len(full_name))
print(full_name)
print("="*len(full_name))