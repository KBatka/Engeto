# Conversion rates
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

# Amount of units for conversion.
kg_amount=80
km_amount=54
l_amount=5

# Results
kg_result = kg_lb*kg_amount
km_result = km_mile*km_amount
l_result = l_gal*l_amount

# Final answers
print("80kg = ",kg_result,"lb")
print("54km = ",km_result,"miles")
print("5l = ",l_result, "galons")

#auta
mercedes    = 150
rolls_royce = '400'

prevod_na_cislo=int(rolls_royce)

print("Mercedes", mercedes, "Rolls-royce", rolls_royce)

price_for_two_mercedeses = mercedes*2
print("price for 2 merc...=", price_for_two_mercedeses)

merced_and_rolls = mercedes+prevod_na_cislo
print ("price for merc and rolls = ", merced_and_rolls)

extra=int(input("please set price of extra equipment"))
two_rolls_with_extra_each=2*(prevod_na_cislo+extra)
print("Price of 2 rolls with extra, total=",two_rolls_with_extra_each,", 1 rolls=", prevod_na_cislo,", extra=", extra)

opt_eqp=int(input("please insert cost of optional equipment"))
mercedes_with_opt_eqp= mercedes+opt_eqp
print("merc with optional eqp is", mercedes_with_opt_eqp)

print("price for 2 merc...=", price_for_two_mercedeses)
print ("price for merc and rolls = ", merced_and_rolls)
print("Price of 2 rolls with extra, total=",two_rolls_with_extra_each,", 1 rolls=", prevod_na_cislo,", extra=", extra)
print("merc with optional eqp is", mercedes_with_opt_eqp)


my_str="indexing"
list(my_str)


# Extract and print first 5 letters

first_five = my_str[:5]

# Extract and print last 5 letters

last_five = my_str [3:]

# Extract and print each 3rd letter

each_third = my_str[0::3]

print("First five letters:" + first_five)
print("Last five letters:" + last_five)
print("Each third letter:"+ each_third)