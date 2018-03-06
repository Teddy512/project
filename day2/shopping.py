#authon ：teddy

production_list=[('Iphone',5800),('Mac Pro',9800),('Bike',800),('watch',10600),('coffee',31),('alex python',120)]
shopping_list=[]
salary=input("input you salary:")
if salary.isdigit():
   salary=int(salary)
   while True:
       for index,item in enumerate(production_list):
            print (index,item)
       user_choise=input("选择要买吗？》》》：")
       if user_choise.isdigit():
           user_choise=int(user_choise)
           if user_choise<len(production_list)and user_choise>=0:
               p_item=production_list[user_choise]
               if p_item[1]<=salary:#买的起
                  shopping_list.append(p_item)
                  salary-=p_item[1]
                  print ("Adden %s into shopping cart,your current balance is \033[31;1m%s\033[0m"%(p_item,salary))
               else:
                   print ("\033[41:1m你的余额只剩【%s】了，请充值！\033[0m"%(salary))
           else:
               print("product  code [%s] is not exist "% user_choise)
       elif user_choise=='q':
                print ("-------shopping list---------")
                for p in shopping_list:
                    print(p)
                print ("Your current balance :",salary)
                exit()
       else:
               print ("Invalid option")


