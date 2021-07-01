def checkdiv(x,y):
    if x>=y:
        if x%y==0:
            print(x,"is divisible by",y)
        else:
            print(x,"is not divisible by",y)
    else:
        print("enter first number greater than or equal to second number")
checkdiv(4,2)
checkdiv(4,3)
checkdiv(2,4)