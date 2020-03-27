string01 = 'Bratislava'
string02 = 'Budapest'

diff = set(string01) ^ set(string02)
all = set(string01) | set(string02)

print('Different characters:', diff)
print('All characters:', all)