#speed of driver is gratarthan 70 show points  after 70 1 point aftar  5 it take incriment#
def speed_driver():
    speed=int(input("enter your speed"))
    if speed<=70:
        print("ok")
    elif speed>70:
        i=70
        c=0
        while i<speed:
            c+=1
            i=i+5
        print(c,"points")
        if c>12:
            print("licesenced failed")
(speed_driver())