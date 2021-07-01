def perfect_num(num):
    i=1
    s=0
    while i<num:
        if num%i==0:
            s=s+i
        i+=1
    if s==num:
        print("it is perfect number")
    else:
        print("it is not perfect number")
num=int(input("enter the number"))
perfect_num(num)