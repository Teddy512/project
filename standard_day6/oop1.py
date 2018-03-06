#authon :teddy


# 例1：
class myclass:      # 用关键字class进行类的定义  即 “class 类名：”
    def __init__(self):
        # 类中定义的函数叫做 “方法”  __init__ 方法是构造方法 根据类创建对象时自动执行
        # self为实例化的对象本身  即即将被实例化的对象obj
        print("this is my class")

obj = myclass()  # 实例化类 创建对象 会自动执行类中的 __init__ 运行结果：this is my class



# 例2：
#  __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上
class myclass:
    def __init__(self, name1, age1):
        self.name = name1
        self.age = age1
# 因为会自动执行类中的 __init__方法，且该方法中有参数，所以实例化对象时需要传递参数
# self是一个形式参数, 当执行下句代码时，实例化对象obj1,那么self就等于obj1这个对象
obj1 = myclass("IKTP", 22)
# 当执行下句代码时，实例化对象obj2,那么self就等于obj2
# 且这两个对象同都拥有两个属性：name,age
obj2 = myclass("hahaha", 23)
# 当需要调用对象的属性时，即name和age属性，可以直接用对象名字后打点调用需要的属性，例如：
print(obj1.name)  # 执行结果：IKTP
print(obj1.age)  # 执行结果：22
print(obj2.name)  # 执行结果：hahaha
print(obj2.age)  # 执行结果：23





# 例3：方法分为三种：实例方法，类方法，静态方法
class myclass:
    public_var = "this is public_var"

    def __init__(self, name1, age1):
        self.name = name1
        self.age = age1

    #  在类里面定义的函数，统称为方法，方法参数自定义，可在方法中实现相关的操作
    #  创建实例方法时，参数必须包括self，即必须有实例化对象才能引用该方法，引用时不需要传递self实参
    def speak(self):
        print("this is def speak.%s 说：我今年%d岁。" % (self.name, self.age))

    #  我们要写一个只在类中运行而不在实例中运行的方法. 如果我们想让方法不在实例中运行
    #  比如我们需要类中的基础字段public_var,根本不需要实例化对象就可以拿到该字段
    #  这时就需要装饰器@classmethod来创建类方法，至于classmethod的使用场合，会在下篇文章介绍
    #  创建类方法时，参数必须包括cls，即必须用类来引用该方法，引用时不需要传递cls实参
    @classmethod
    def speak2(cls):
        print("this is classmethod")
        return cls.public_var

    #  经常有一些跟类有关系的功能但在运行时又不需要实例和类参与的情况下需要用到静态方法
    #  写在类里的方法,必须用类来调用(极少数情况下使用,一般都在全局里直接写函数了)
    @staticmethod
    def speak3(name2, age2):
        print("this is staticmethod.%s 说：我今年%d岁。" % (name2, age2))


obj = myclass("IKTP", 22)
# 无论是类方法、静态方法还是普通方法都可以被实例化的对象调用
# 但是静态方法和类方法可以不用对象进行调用
obj.speak()  # 执行结果：this is def speak.IKTP 说：我今年22岁。
var = obj.speak2()  # 执行结果：this is classmethod
print(var)  # 执行结果： this is public_var
obj.speak3("liu", 23)  # 执行结果：this is staticmethod.liu 说：我今年23岁。

myclass.speak()  # 报错，实例方法不能直接被调用，必须需要实例化的对象调用
var2 = myclass.speak2()  # 不需要实例化对象即可拿到该字段
print(var2)  # 不需要实例化对象即可拿到该字段
myclass.speak3("abc", 12)  # 不需要实例化对象即可执行





# 例4：继承是面向对象的重要特征之一，
# 继承是两个类或者多个类之间的父子关系，子类继承了父类的所有公有实例变量和方法
class father:
    father_var = "this is father_var"

    def father_def(self):
        print("this is father_def")


class son(father):  # 括号里有类名，代表该类是子类（派生类），继承自父类（基类）father
    pass


obj = son()
# son子类中没有father_var 则去父类father中寻找
print(obj.father_var)  # 执行结果：this is father_var
# son子类中没有father_def方法 则去父类father中寻找
obj.father_def()  # 执行结果：this is father_def


'''
如果父类中有构造方法且子类也有构造方法，则在子类中必须亲自调用且传递相对应的参数
'''



# 如果父类中有构造方法且子类也有构造方法，则在子类中必须亲自调用且传递相对应的参数
# 否则无法找到在父类中定义的属性
# ##############################错误方式##################################
class father:
    def __init__(self, n):
        self.name = n


class son(father):
    def __init__(self):
        print("aaaaa")


obj = son()
# 子类中没有name属性，且没有在子类中调用并传递相对应的参数给父类的构造方法，所以找不到name属性 报错
print(obj.name)


########################################################################
# #########################正确方式######################################
class father:
    def __init__(self, n):
        self.name = n


class son(father):
    def __init__(self):
        father.__init__(self, "6666")


obj = son()
print(obj.name)  # 执行结果 6666
########################################################################

'''
如果父类中没有构造方法
则不必调用
如果父类中有构造方法但子类中没有构造方法，则在实例化子类对象的时候需要传递父类中的构造参数
'''


class father:
    def __init__(self, n):
        print("bbbbbbbb")
        self.name = n


class son(father):
    def speak(self):
        print("aaaaa")


obj = son()  # 报错 因为子类没有构造方法，所以会执行父类的构造方法，但是没有给父类的构造方法传递参数
obj = son("IKTP")
print(obj.name)  # 执行结果： IKTP


# 在子类中调用父类的方法



class father:
    def speak(self):
        print("this is father speak")


class son(father):
    def speak2(self):
        # ######调用父类的speak方法的三种方式######

        father.speak(self)  # 直接类名后打点调用方法，需要传递self
        super().speak()  # super()代指父类
        super(son, self).speak()

        ########################################
        print("this is son speak2")


obj = son()
obj.speak2()
# 运行结果：this is father speak
#          this is father speak
#          this is father speak
#          this is son speak2


# 覆盖（重写）父类方法


class father:
    def speak(self):
        print("this is father speak")

    def speak2(self):
        print("this is father speak2")


class son(father):
    def speak2(self):
        print("this is son speak2")


obj = son()
obj.speak2()  # 运行结果：this is son speak2

# 对象总会先在实例化该对象的类里寻找属性字段或者方法，
# 如果有则执行，如果该类里没有，则再去父类里寻找
# 由于父类本来拥有speak2方法，但是子类里又写了一个speak2方法
# 所以obj不会去父类里寻找该方法，只会执行子类里的speak2方法，这样就称为覆盖或重写


'''
多继承

 一个类可同时继承多个类，与多个类具有继承关系，则这个类可调用所有父类中的方法和字段
'''

class father1():
    father1_var = "this is father1_var"

    def father1_def(self):
        print("this is father1_def")


class father2():
    father2_var = "this is father2_var"

    def father2_def(self):
        print("this is father2_def")


class son(father1, father2):  # son类同时继承father1类和father2类
    def son_def(self):
        print("this is son_def")


obj = son()
print(obj.father1_var)
print(obj.father2_var)
obj.father1_def()
obj.father2_def()
# 执行结果：
# this is father1_var
# this is father2_var
# this is father1_def
# this is father2_def
# 例5：