def eligible_for_vote():
    if user>=18:
        print("eligible")
    else:
        print("not eligible")
user=int(input("enter any age"))
eligible_for_vote()
