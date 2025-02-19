import math

height      = int(input("Enter height: "))
first_base  = int(input("Enter width:  "))
second_base = int(input("Enter height: "))

midle = (first_base + second_base) / 2
area  = midle * height

print(f"Area of trapezoid is {area}")
