# #authon teddy
import time
user,passwd='teddy','abc123'
def auth(auth_type):
    print ("auth func:",auth_type)
    def outer_wrapper(func):
        def wrapper(*args,**kwargs):
            print ("wrapper func  args:",*args,**kwargs)
            if auth_type=="local":
               username=input("Username:").strip()
               password=input("password:").strip()
               if user==username  and passwd==password:
                   print ("\033[32;1mUser has passed authentication\033[0m")
                   res=func(*args,**kwargs)
                   print ("---after authentication---")
                   return res
               else:
                   exit("\033[31;1mInvalid username or password\033[0m")
            elif auth_type=="ldap":
                 print ("ldap不会")
        return  wrapper
    return  outer_wrapper

def index():
    print ("welcome  to index page")
@auth(auth_type="local")
def home():
    print ("welcome to home page")
    return "from home "
@auth(auth_type="ldap")
def bbs():
    print ("welcome to bbs page ")


index()
home()
bbs()

# 执行结果：
# auth func: local
# auth func: ldap
# welcome  to index page
# wrapper func  args:
# Username:teddy
# password:abc123
# User has passed authentication
# welcome to home page
# ---after authentication---
# from home
# wrapper func  args:
# ldap不会