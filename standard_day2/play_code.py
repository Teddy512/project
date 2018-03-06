#authon :teddy
# 购物车类型的项目，使用input 列表，元组，while循环实现功能，能够自动加减数据，返回你已经选中的列表，
# 加入到列表里面

product_list = [
    ('Iphone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('Alex Python',120),
]

shopping_list=[]
salary=input("input you salary:")
if salary.isdigit():
    salary=int(salary)
    while True:
        #找到产品索引，和对应的里面的元素 例如 0 ('Iphone', 5800)
        for index,item  in enumerate(product_list):
             print (index,item)
        user_choice=input("选择要买吗？》》》：")
        if user_choice.isdigit():
            user_choice=int(user_choice)
            #当列表里面数据在范围内的时候，就进行选择
            if user_choice<len(product_list) and user_choice>=0:
                p_item=product_list[user_choice]
                #P_item[1] 是对应产品的价格
                if p_item[1]<=salary:
                    #如果价格小于余额则将列表里面的数据放到购物车里面
                    shopping_list.append(p_item)
                    #同时salary减少对应的金额
                    salary-=p_item[1]
                    print("Added %s into shopping cart ,your current balance is \033[31;1m%s\033[0m"%(p_item,salary))
                else:
                    #如果余额小于商品价格，则print这句话
                    print ("\033[41;1m你的余额只剩[%s]啦，还买个毛线\033[0m" % salary)
            else:
                    print("product code [%s] is not exist!" % user_choice)
        elif  user_choice=='q':
              print("-------shopping list-------")
              for p  in shopping_list:
                  print (p)
              print ("your current balance:",salary)
              exit()
        else:
            print ("invalid option")

