def iseven(list1):
    even_num=[]
    for n in list1:
        if n%2==0:
            even_num.append(n)
    return even_num
even_num=iseven([2,3,42,51,62,70])
print("even numbers are:",even_num)
