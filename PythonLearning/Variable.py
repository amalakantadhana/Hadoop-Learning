from PythonLearning import calculator, Email

age=25
name='dhanna'
print age
print name

# second one
x=4 # x is type of int
x="sallyy" # x is type of str
print(x)
print(x+x)

# third
x = "John"
# is the same as
x = 'John'
print x

output=calculator.sum(10,30)
print ("the final output is " + str(output))

output=calculator.sum(50,40)
print ("the final output is " + str(output))

output=calculator.sub(40,30)
print ("the final output is " + str(output))

output=calculator.mul(40,30)
print ("the final output is " + str(output))

output=calculator.div(40,30)
print ("the final output is " + str(output))

output=Email.emailgmail("dhana","lakshmi")
print ("the final output is " + str(output))

output=Email.emailgmail("nagi","avr")
print ("the final output is " + str(output))

output=Email.emailyahoo("dhana","lakshmi")
print ("the final output is " + str(output))

output=Email.emailyahoo("nagi","avr")
print ("the final output is " + str(output))