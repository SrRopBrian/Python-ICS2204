#SCT211-0078/2022 BRIAN KIPNG'ENO
#Simple tip calculator
#Assumption is that the currency used is the Kenyan Shilling

amount = int(input("Hello! The total bill amount is Ksh. "))
num = int(input("Please enter the number of people splitting the bill: "))
print()

#dictionary containing tip options in percentages
options = {'A': '10%', 'B': '12%', 'C':'15%'}

#display the available tip options   
print("You can tip either of the following options in percentages:")
for i in options:
    print(i, ":", options[i])
print() 

percent = input("Please select a percentage tip amount suitable for you from the options: ")

if percent.upper() == 'A':
    tip = ((0.1*amount)+(amount))/num
    print("Each person should contribute Ksh. {:.02f} to foot the bill.".format(tip))
elif percent.upper() == 'B':
    tip = ((0.12*amount)+(amount))/num
    print("Each person should contribute Ksh. {:.02f} to foot the bill.".format(tip))
elif percent.upper() == 'C':
    tip = ((0.15*amount)+(amount))/num
    print("Each person should contribute Ksh. {:.02f} to foot the bill.".format(tip))
else:
    print("You have selected an invalid option.")