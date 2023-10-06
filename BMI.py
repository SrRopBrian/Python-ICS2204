#SCT211-0078/2022 BRIAN KIPNG'ENO
#Simple BMI Calculator

weight = float(input("Please enter your weight in kilograms: "))
height = float(input("Please enter your height in metres: "))

bmi = (weight / pow(height,2))

if bmi < 18.5:
   print("Hello, you have a BMI of {:.2f} and therefore you're underweight." .format(bmi))
elif bmi >= 18.5 and bmi <= 24.9:
   print("Hello, you have a BMI of {:.2f} and therefore you're at the normal weight." .format(bmi))
else :
   print("Hello, you have a BMI of {:.2f} and therefore you're overweight." .format(bmi))