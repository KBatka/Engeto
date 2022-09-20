
handler = open('www.py')
print(handler)
print(type(handler))

def read_specific_line(file_path, line_number: int)->str:
    handler = open(file_path, 'r')
    current_line= 'špatné číslo'
    current_line_number = 0
    while current_line_number<line_number:
        current_line = handler.readline()
        current_line_number += 1



print(current_line)