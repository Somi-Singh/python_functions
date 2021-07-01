def prime(num):
    i=2
    while i<num:
        if num%2==0:
            print("not prime number")
            break
        else:
            print("prime number")
        i=i+1
num=int(input("enter the number="))
prime(num)