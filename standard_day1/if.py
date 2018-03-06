#Authon：teddy
import  getpass

_username="teddy"
_password="1314520"

username=input("username")
password=input("password")
# password=getpass.getpass("password")


if _username==username and _password==password:
    print("welcome,user {name} login.......".format(name=username))
else:
    print("invalid username and password")