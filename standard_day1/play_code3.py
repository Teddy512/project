#authon :teddy

import getpass
_username="teddy"
_password="abc123"
username=input("username")
password=input("password")
if _username==username  and _password==password:
    print ("welcome user {name} login".format(name=username))
else:
    print ("invalid username or password")

