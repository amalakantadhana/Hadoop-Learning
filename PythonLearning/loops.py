
#"if statement" is written by using the if keyword.

a=35
b=34
if(a>b):
    print( "a is greater than b")

#Indentation
#Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
# Other programming languages often use curly-brackets for this purpose.

a=200
b=33
if(b>a):
    print("b is greater than a")
else:
    print("a is greater than b")


#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

a=45
b=45
if(b>a):
    print("b is greater than a")
elif(a==b):
    print("a and b are equal")

# using if, elif and else

a = 200
b = 33
if b > a:
  print("b is greater than aa")
elif a == b:
  print("a and bb are equal")
else:
  print("a is greater than bb")

#a = 330
#b = 330
#print("A") if a > b else print("=") if a == b else print("B")

# nested if

x=33

if(x>10):
    ("above 10")
    if(x>20):
        print("and also above 20!")
    else:
        print("not above 20")