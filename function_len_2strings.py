# both string  is eqal or not#
def user(name,name2):
    if len(name)>len(name2):
        return("lenth oh name one is grater name2")
    elif len(name)==len(name2):
        return("the bot name has same lenth")
    else:
        return("name2 lent grater than name")
a=user("shireen","shireen")
print(a)



#lenth of eliments,#
def user(names):
    for i in names:
        print(i,len(i))
user(["abc","shah","perfect"])