# perfect number its divisible by sum of divisor#
def perfect(num):
    sum_num=0
    for i in range(1,num):
        if num%i==0:
            sum_num=sum_num+i
    if num==sum_num:
        print(num,"it is perfect number")
    else:
        print(num,"its is not prfect number")
perfect(2) 