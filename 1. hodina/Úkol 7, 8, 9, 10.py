#Úkol 7

# Create Candidate
candidates = []

# Print candidates at the beginning
print('Candidates at the beginning:', candidates)

# Create employees
emplooyes = ['Francis', 'Ann', 'Jacob', 'Claire']

# Print employees at the beginning
print('Employees at the beginning:', emplooyes)

# Add new candidates
candidates.append('Agnes')
candidates.append('Bruno')

# Print new candidates
print('New names added to candidates:', candidates)

# Insert name
emplooyes.insert(1,'Bruno')

# Print the employees list after entering a new name
print('New names added to employees:', emplooyes)

#Úkol 8
# Results from previous task
candidates = ['Bruno', 'Agnes']
employees = ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire']

# Delete names from candidates
candidates.remove('Bruno')

# Print remaining candidates
print('Bruno removed from candidates:', candidates)

# Repeat element
candidates = ['Agnes']*3

# Print repeating element in list candidates
print('Repetition of Agnes in the candidate list:', candidates)

# Join lists
emplooyes = emplooyes + candidates

# Print joined lists
print('Joined candidates and employees:', emplooyes)

# Index 2
emplooyes = ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire', 'Agnes', 'Agnes', 'Agnes']
my_var = ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire', 'Agnes', 'Agnes', 'Agnes'][2]
print('On index 2 is:', my_var)

# Find out last index and assign it to variable
last = ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire', 'Agnes', 'Agnes', 'Agnes'][7]
print('On the <last_index> index is:', last)

#Úkol 9
# Results from the previous task
candidates = ['Agnes', 'Agnes', 'Agnes']
employees = ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire', 'Agnes', 'Agnes', 'Agnes']

# Interval 2-5
interval = employees[2:6]
print('In interval from 2 to 5 is:', interval)

# Each 3rd
each_third = employees[0::3]
print('Every third member is:', each_third)

# Save index
employees = ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire', 'Agnes', 'Agnes', 'Agnes']
x = employees.index('Jacob')

# Jacob index
print('Jacob is on the index:', x)

# Number of name Agnes
print('Number of Agnes names in the sheet:', employees.count('Agnes'))