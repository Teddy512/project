# -*- coding: utf-8 -*-
#    authon:teddy


''''''

class Role(object): #定义一个类， class是定义类的语法，Role是类名，(object)是新式类的写法，必须这样写，以后再讲为什么
      def __init__(self,name,role,weapon,life_value=100,money=15000): #初始化函数，在生成一个角色时要初始化的一些属性就填写在这里
        self.name = name #__init__中的第一个参数self,和这里的self都 是什么意思？ 看下面解释
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money


      def short(self):
          print ("shotting.....")



      def got_shot(self):
        print("ah...,I got shot...")

      def buy_gun(self,gun_name):
        print("just bought %s" %gun_name)

r1 = Role('Alex','police','AK47')
r2 = Role('Jack','terrorist','B22')




'''类的语法


class Dog(object):

    print("hello,I am a dog!")


d = Dog() #实例化这个类，
#此时的d就是类Dog的实例化对象

#实例化，其实就是以Dog类为模版，在内存里开辟一块空间，存上数据，赋值成一个变量名'''
'''

class Role(object): #定义一个类， class是定义类的语法，Role是类名，(object)是新式类的写法，必须这样写，以后再讲为什么
    def __init__(self,name,role,weapon,life_value=100,money=15000): #初始化函数，在生成一个角色时要初始化的一些属性就填写在这里
        self.name = name #__init__中的第一个参数self,和这里的self都 是什么意思？ 看下面解释
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

上面的这个__init__()叫做初始化方法(或构造方法)， 在类被调用时，这个方法(虽然它是函数形式，但在类中就不叫函数了,叫方法)会自动执行，进行一些初始化的动作，所以我们这里写的__init__(self,name,role,weapon,life_value=100,money=15000)就是要在创建一个角色时给它设置这些属性，那么这第一个参数self是干毛用的呢？

初始化一个角色，就需要调用这个类一次：

r1 = Role('Alex','police','AK47’) #生成一个角色 , 会自动把参数传给Role下面的__init__(...)方法
r2 = Role('Jack','terrorist','B22’)  #生成一个角色

我们看到，上面的创建角色时，我们并没有给__init__传值，程序也没未报错，是因为，类在调用它自己的__init__(…)时自己帮你给self参数赋值了，

r1 = Role('Alex','police','AK47’) #此时self 相当于 r1 ,  Role(r1,'Alex','police','AK47’)
r2 = Role('Jack','terrorist','B22’)#此时self 相当于 r2, Role(r2,'Jack','terrorist','B22’)'''

'''总结一下2点：

    上面的这个r1 = Role('Alex','police','AK47’)动作，叫做类的“实例化”， 就是把一个虚拟的抽象的类，通过这个动作，变成了一个具体的对象了， 这个对象就叫做实例
    刚才定义的这个类体现了面向对象的第一个基本特性，封装，其实就是使用构造方法将内容封装到某个具体对象中，然后通过对象直接或者self间接获取被封装的内容
'''













