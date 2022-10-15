#BMI Calculator
# use float instead int

weight = float(input("your weight in kg= "))
height = float(input("your height in cm= "))

#BMI formula in python (V)
#BMI = (weight /(height * height)) __ is wrong
#BMI = weight / (height/100)**2 __ is right

bmi = weight / (height/100)**2

print ("Your BMI is : ",bmi)
           
if bmi <= 18.4:
    print("You are underweight.")
elif bmi <= 24.9:
    print("You are healthy.")
elif bmi <= 29.9:
    print("You are over weight.")
elif bmi <= 34.9:
    print("You are severely over weight.")
elif bmi <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")


#'if' goes first
#'elif' ,use if theres another option for output'
#'else'goes last
