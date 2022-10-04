from datetime import date
today =date.today
today_v = today()
print(today)
print(today_v)

your_age=int(input("Enter age"))
solution = today_v.year - your_age
print((solution))

your_y=int(input("Enter y"))
your_m =int(input("Enter m"))
your_d =int(input("Enter d"))
solution = today_v - date(your_y,your_m,your_d)
print((solution))



print("You were probably born in", solution)