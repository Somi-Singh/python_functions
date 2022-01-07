#age is gretarthan18 than only he or she elegible forr vot#
def eligible_for_vote(age,gender):
    if age==18 or age>18:
        return("you can give vot")
    return("you are not alegeble")
result=eligible_for_vote(age=int(input("enter number")),gender=input("enter your gender"))
print(result)