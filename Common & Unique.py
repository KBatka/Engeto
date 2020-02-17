string01 = 'Bratislava'
string02 = 'Budapest'

set(string01)
set(string02)

common_characters = set(string01) & set(string02)
unique_characters = set(string01) - set(string02)

print("common characters", common_characters)
print("unique characters", unique_characters)
