# 90 - Grade A
# 75-90 - Grade B
# 60-75 - Grade C
# 35-60 - Grade D
# less than 35 - fail
def grading(subject):
    if subject > 90:
        print("You got Grade A..")
    elif subject > 75 and subject < 90:
        print("you got Grade B")
    elif subject > 60:
        print("you got Grade C")
    elif subject >35 :
        print("you got Grade D")
    else:
        print("you failed")

#Input : two names
#output : names equal or not
def name_check(name1,name2):
    if name1 == name2:
        print("both names are equal")
    else:
        print("Not equal")


def not_equal_test(address1,address2):
    if address1 != address2:
        print("courier delivered")
    else:
        print("Not delivered")

def file_exists(filename):
    #Open the file
    if open(filename):
        return True
    else:
        return False

grading(33)
name_check("dhana","dhana")
name_check("dhana","aaradhya")
not_equal_test("chandanagar","serilingampaly")

if file_exists("C:/Users/dhana/PycharmProjects/python-training/training/operators_test.py"):
    print("File found")
else:
    print("File not found")

if False:
    print("Yes true")
elif True:
    print("NO false")
