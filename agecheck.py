def over18(number):
    if(int(number)>=18): return True;
    return False;

def printverification(boolean):
    if(boolean): print ("Das Alter " +str(age) +" ist über 18")
    else: print ("Das Alter " +str(age) +" ist nicht über 18")

age=input("please enter an age")
verification=over18(age)
printverification(verification)