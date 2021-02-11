# Making a BMI Calculator
# Thursday 11th February 2021 - 14:48
# George Koundouri

print("Welcome to my BMI calculator!")  # A message that welcomes the user to the BMI Calculator

name = input("What is your name?: ")  # Assigns name to the users name
height_m = float(input("What is your height in meters?: "))  # Assigns height_m to the users height in meters
weight_kg = float(input("What is your weight in KG?: "))  # Assigns weight_kg to the users weight in KG

# Calculates the BMI
bmi = weight_kg / (height_m ** 2)  # To calculate BMI it is: BMI = weight / height * height
round(bmi)
print("Your BMI is: " + str(round(bmi, 2)))  # Prints what the users BMI is to 2dp (Decimal Places)

if bmi < 18.5:
    print(name + " your BMI falls in underweight range")
elif bmi >= 18.6 < 25:
    print(name + " your BMI falls in the normal range")
elif bmi >= 25.1 < 30:
    print(name + " your BMI falls in the overweight range")
elif bmi >= 30.1 < 35:
    print(name + " your BMI falls in the obese range")
    print("You are classified in the Class 1 obese category")
elif bmi >= 35.1 < 40:
    print(name + " your BMI falls in the obese range")
    print("You are classified in the Class 2 obese category")
else:
    if bmi >= 41:
        print(name + " your BMI falls in the obese range")
        print("You are classified in the Class 3 obese category")

print("Thank you for using my BMI calculator!")
