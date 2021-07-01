def rev(a):
    c=[]
    i=len(a)-1
    while i>=0:
        c.append(a[i])
        i-=1
    print(c)
rev([2,4,6,3,5,2,6,43])