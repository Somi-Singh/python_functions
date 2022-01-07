#make prime  number function#
def prime(num):
    i=1
    c=0
    while i<=num:
        if num%i==0:
            c+=1
        i+=1
    if c==2:
        return(num, "is prime number")
    return(num, "is not prime number")
number=prime(num=int(input("enter number")))
print(number)

# prime numbers#1 to 100

def prime_num(num):
    for i in range(1,num):
        for j in range(2,i):
            if i%j==0:
                print("eqaul",i*j)
                break
        else:
            print(i, " is prime number")
number=int(input("enter number"))
prime_num(number) 

