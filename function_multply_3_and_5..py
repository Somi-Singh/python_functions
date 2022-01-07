#multiple of 3&5#
def limit(num):
    i=1
    while i<=num:
        if i%5==0 and i%3==0:
            print(i)
        i+=1
limit(num=int(input("enter your number")))