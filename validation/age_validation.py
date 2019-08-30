# validation workflow
#age = input("Enter age: ")
def ageCheck(age):
    
    if len(age) == 0:
        #print("Empty input")
        return False
    # data type check
    elif not age.isdigit():
        #print("Age must be a number")
        return False
    # range check
    elif not 0 < int(age) < 100:
        #print("Age must be between 1 and 99")
        return False
    # valid age
    return True