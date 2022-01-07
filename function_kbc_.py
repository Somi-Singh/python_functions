def printing_q(qutision_list,i):
    print(qutision_list[i])
def printing_option(option_a,i):
    print(option_a[i])
def printing_salution(salutions,i):
    print(salutions[i])
def printing_lifline_o(lifeline_option,i):
    print(lifeline_option[i])
def printing_l_s(lifeline_solution,i):
    print(lifeline_solution[i])
    
qutision_q=[
    "How many continents are there?",              
    "What is the capital of India?",            
    "NG mei kaun se course padhaya jaata hai?"  
]
option_a=[
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
salutions=["3", "4", "1"] 
lifeline_option=[["four","seven"],["channai","dellhi"],
["softoware", "counseling"]]
lifeline_solution=["2","2","1"]
i=0
c=0
while i<len(qutision_q):
    printing_q(qutision_q,i)
    printing_option(option_a,i)
    answer=input("enter your answer")
    if answer==salutions[i]:
        print("your answer is wright")
        i=i+1
    elif answer=="5050":
        if c==0:
            printing_lifline_o(lifeline_option,i)
            user1=input("enter your answer")
            if user1==lifeline_solution[i]:
                print("your annswer is right")
                c=c+1
                i=i+1
            else:
                print("wrong")
                break
        else:
            print("you alrady use this lifline")

    else:    
        printing_lifline_o(lifeline_option,i)
        user1=input("enter your answer")
        if user1==lifeline_solution[i]:
            print("your annswer is right")
            break
            i=i+1
        else:
            print("wrong")
            break
        print("you alrady use this")
        i=i+1
