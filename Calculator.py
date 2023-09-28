name = input("Please enter your name: ")
greeting  = 'Hello '
print(greeting + name)
print()

print("Available operations: ")
operations =  {'A': 'Addition', 'B': 'Subtraction', 'C': 'Multiplication', 'D':'Division'}

#display the contents of the dictionary
for i in operations:
    print(i,":", operations[i])
print()

print("NOTE: Number 1 > Number 2")
num1 = int(input("Please enter number 1:  "))
num2 = int(input("Please enter number 2: "))
print()

operator = input("Please choose an option: ")

if operator.upper() == 'A':
    print('Adding...')
    print()
    print(name, ", the sum of the two numbers is: ", num1 + num2)
    print()
elif operator.upper() == 'B':
    print('Subtracting...')
    print()
    print(name, ", the difference of the two numbers is: ", num1 - num2)
    print()
elif operator.upper() == 'C':
    print('Multiplying...')
    print()
    print(name, ", the product of the two numbers is: ", num1 * num2)
    print() 
elif operator.upper() == 'D':
    print('Dividing...')
    print()
    print(name, ", the division of the two numbers is: ", num1 / num2)
    print()
else:
    print("ERROR! Enter valid option!")







