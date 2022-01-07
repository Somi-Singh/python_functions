#even and odd number#
def showNumber(num):
    i=1
    while i<=num:
        if i%2!=0:
            print(i,"odd")
        else:
            print(i,"even")
        i+=1
number=showNumber(num=int(input("enter number")))