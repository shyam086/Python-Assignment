''' 
Task 2: Using the Math Module for Calculations
 
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.

 Expected Output:
 For example, if the user enters 25, the output should be:

Enter a number: 25
Square root: 5.0
Logarithm: 3.2188758248682006
Sine: -0.13235175009777303
'''

number = int(input("Enter a number :"))

import math

square_root = math.sqrt(number)
logarithm = math.log(number)
sine = math.sin(number)

print("Square root :", square_root)
print("Logarithm :", logarithm)
print("Sine :", sine)
