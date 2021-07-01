def calculate (num1,num2,symble):
    if symble=="+":
        print(num1+num2)
    elif symble=="-":
        print(num1-num2)
    elif symble=="*":
        print(num1*num2)
    elif symble=="//":
        print(num1//num2)
    elif symble=="%":
        print(num1%num2)
    elif symble=="**":
        print(num1**num2)
    else:
        print(num1/num2)
num1=int(input("enter the number="))
num2=int(input("enter the number="))
symble=input("enter the number=")
calculate(num1,num2,symble)