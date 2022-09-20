#Úkol 7

# Create Candidate
candidates = []

# Print candidates at the beginning
print('Candidates at the beginning:', candidates)

# Create employees
employees = ['Francis', 'Ann', 'Jacob', 'Claire']

# Print employees at the beginning
print('Employees at the beginning:', employees)

# Add new candidates
candidates.append('Agnes')
candidates.append('Bruno')

# Print new candidates
print('New names added to candidates:', candidates)

# Insert name
employees.insert(1, 'Bruno')

# Print the employees list after entering a new name
print('New names added to employees:', employees)

#Úkol 8
# Results from previous task
candidates_test = ["Agnes",'Bruno']
employees_test = ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire']
print("Sedi seznam candidates z ukolu 7:",candidates==candidates_test)
print("Sedi seznam emploeeys z ukolu 7:", employees_test == employees)

# Delete names from candidates
candidates.remove('Bruno')

# Print remaining candidates
print('Bruno removed from candidates:', candidates)

# Repeat element
agnes_repeat = ['Agnes']*3

# Print repeating element in list candidates
print('Repetition of Agnes in the candidate list:', agnes_repeat)

# Join lists
employees = employees + candidates

# Print joined lists
print('Joined candidates and employees:', employees)

# Index 2

my_var = employees[2]
print('On index 2 is:', my_var)

# Find out last index and assign it to variable
last = len(employees) - 1
print("At index ", last, "is:", employees[last])

#Úkol 9
# Results from the previous task


# Interval 2-5
interval = employees[2:6]
print('In interval from 2 to 5 is:', interval)

# Each 3rd
each_third = employees[0::3]
print('Every third member is:', each_third)

# Save index

x = employees.index('Jacob')

# Jacob index
print('Jacob is on the index:', x)

# Number of name Agnes
print('Number of Agnes names in the sheet:', employees.count('Agnes'))