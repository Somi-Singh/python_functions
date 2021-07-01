def check_num():
    i=0
    while i<len(list1):
        if list1[i]%2==0 and list2[i]%2==0:
            print("dono even hai")
            print("--------------------")
        else:
            print("dono odd hai")
            print("---------------------")
        i+=1
list1=[2,6,18,10,3,75]
list2=[6,19,24,12,3,27]
check_num()