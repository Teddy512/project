# Author:Alex Li
import getpass

_username = 'alex'
_password = 'abc123'
username = input("username:")
#password = getpass.getpass("password:")
password = input("password:")
if _username == username and _password == password:
    print("Welcome user {name} login...".format(name=username))
else:
    print("Invalid username or password!")






'''
for i in range(10):
    if i <3:
        print ("loop",1)
    else:
        continue
    print ("hehe....")
    
'''


for i in range(10):
    print ('----------')
    for j in range(10):
        print(j)
        if j>5:
            break