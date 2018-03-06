#authon :teddy
age_oldboy=56

count =0
while count <3:
    guese_age=int (input("guess you  age "))
    if guese_age==age_oldboy:
        print("yes,you got it")
        break
    elif guese_age>age_oldboy:
        print ("think small")
    else:
        print ("think big")

    count+=1
    if count==3:
        countinue_confirm=input("do  you want to keep  guessing ..?")
        if countinue_confirm!='n':
            continue
        else:
            break



print ("you have tried too many time  ..fuck  you  too...%s?"%count)


