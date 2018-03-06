#Authon:teddy
# 版本1
age_od_gay=56

count=0
while True:
    if count==3:
       break
    age_old=int(input("age"))

    if age_od_gay==age_old:
        print ("yes,you got it")
        break
    elif age_od_gay>age_old:
        print("think small")
    else:
        print("think big")
    count+=1

# 版本2
count=0
while count<3:
    age_old=int(input("age"))

    if age_od_gay==age_old:
        print ("yes,you got it")
        break
    elif age_od_gay>age_old:
        print("think small")
    else:
        print("think big")
    count+=1

else:
    print("you input many times,please...get out")



# 版本3
# count = 0
for i in range(3):
    age_old = int(input("age"))

    if age_od_gay == age_old:
        print("yes,you got it")
        break
    elif age_od_gay > age_old:
        print("think small")
    else:
        print("think big")
    # count += 1

else:
    print("you input many times,please...get out")