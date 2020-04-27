
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

myvar='john'
MY_VAR="tom"
print myvar
print MY_VAR

# assigneing values to multiple variables

x,xy,dg='orange',"apple","tiger"
print(x)
print(xy)
print(dg)
#assigning same value to multiple variables
x=y=z="orange"
print(x)
print(y)
print(z)

#output variables
# python print statement is often used to output variables
#To combine both text and a varibale , python uses a + character

x="awesome"
print( "the python is " + x)

x = "script is "
y = "awesome"
z =  x + y
print(z)

# for numbers, + acts as mathematical operator

x = 5
y = 10
print(x + y)

x = 5
y = 25
print(x + y)

# Global variables
# variables created outside the function are called as global variables.
# Global variables are used by everyone both inside and outside of the functions
#Create a variable outside of a function, and use it inside the function
x="awesome"
def myfunc():
    print( "my func is "+ x)
myfunc()

#Create a variable inside a function, with the same name as the global variable

x="global hi"
def myfunc():
    x="local hi"
    print(" the x is "+ x)
myfunc()

print("The outside x " +x)

# the global keyword

def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "changed global"

myfunc()

print("Python is " + x)

