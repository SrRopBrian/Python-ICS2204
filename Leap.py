#SCT211-0078/2022 BRIAN KIPNG'ENO
#Program that checks whether a year is leap or not

year = int(input("Please enter the year: "))
print()
if (year % 4) == 0:
    print("The year ", year, " is a leap year.")
elif (year % 4) != 0:
    print("The year ", year, " is not a leap year.")
else:
    print("ERROR! Please enter a valid year.")