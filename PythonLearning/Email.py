
#gmail which takes input firstname and last name and return
# example nagendra,avr
# output: nagendra.avr@gmail.com

#ex dhana,aaradhya
# output : dhana.aarahdya@gmail.com

def emailgmail(x,y):
    print("enter the firstname " + x)
    print("enter the lastname " + y)
    z=(x + "." + y +"@gmail.com")
    return z

#2. which takes input firstname and last name and return
# example nagendra,avr
# output: nagendra-avr@yahoo.com

#ex dhana,aaradhya
# output : dhana-aarahdya@yahoo.com

def emailyahoo(x,y):
    print("enter the firstname " + x)
    print("enter the lastname " + y)
    z=(x + "." + y +"@yahoo.com")
    return z