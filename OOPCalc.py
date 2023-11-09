#BRIAN KIPNG'ENO SCT211-0078/2022
#simple calculator that performs additions of two integers
#refactored to apply OOP Principles

#the addition calculator class
class Calc():
    def __init__(self, name, int1, int2) -> None:
        self._name = name
        self._int1 = int1
        self._int2 = int2
    def greet(self):
        print("Hello there ", self._name)
    def add(self):
        print("The sum of ", self._int1, " and ", self._int2, " is ", (self._int1+self._int2))
   
#take in input to be used
name_input = input("Please enter your name: ")
int1_input = int(input("Enter integer 1: "))
int2_input = int(input("Enter integer 2: "))
 
#create the object   
ADD = Calc(name_input, int1_input, int2_input)
ADD.greet()  
ADD.add()    