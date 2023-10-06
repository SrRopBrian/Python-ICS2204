#SCT211-0078/2022 BRIAN KIPNG'ENO
#Age calculator 

#importing date class from datetime module
from datetime import date

name = input("Please enter your name: ")
print("Hello " + name)
print()

#user's input of year and the output the entered value
birthyear = int(input("Please enter your year of birth: "))
print("You were born in ", birthyear)
print()

today = date.today()

#calculate age in years, months and days
year_age = (today.year)-(birthyear)
months_age = year_age*12
days_age = year_age*365

#display user's age 
print ("Dear ",  name, ", you are", year_age, " years old or ", months_age, " months old or ", days_age, " days old.")