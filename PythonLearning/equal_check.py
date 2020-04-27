
#1. Write a function to take 2 input variables and check wheter they are equal or not. If equal then return true else return false.
#Caller - Call the above for 2 different values using if else

def equalcheck(a,b):
    if a==b:
        print("true")
    else:
        print("false")

equalcheck(35,3)
equalcheck(9,9)

#3. Write a function to take 1 input variable and check whether variable is equal to "hyderabad". Case insensitive.

def stringsensitive(string1):
    if string1== string1.lower():
        print(string1.lower() + "The strings are the same (case insensitive)")
    else:
        print("The strings are NOT the same (case insensitive)")

stringsensitive("apple")

#4. Write a function to take 1 input variable and check whether variable is equal to "hyderabad". Case sensitive.

def stringsensitive(string1):
    if string1!= string1.lower():
        print("The strings are the same (case insensitive)")
    else:
        print("The strings are NOT the same (case insensitive)")

stringsensitive("APPLE")
#22. Write a function to take 2 input variables and check whether first string is substring of second one.
#Example : nag,nagendra - True
#Example : abc,nagendra - False
def matchstring(a,b):
        if (a.find(b) != -1):
            print ("true")
        else:
            print(a.find(b))

matchstring("nag", "nagendra")


