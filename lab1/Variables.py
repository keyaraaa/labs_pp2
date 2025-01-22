#Variables
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Output Variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#Global Variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()