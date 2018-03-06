# -*-coding：utf-8 -*-
name=input("name")
password=input("password")
age=int(input("age"))  #强制类型转换  str（age）  type（name）
job=input("job")
salary=int(input("salary"))
# print (name,password)


msg='''-----------info of %s----------
    name:%s
    
    age:%d
    
    job:%s
    
    salary:%d
    
'''%(name,name,age,job,salary)

print (msg)

msg2 = '''-----------info of {_name}----------
    name:{_name}

    age:{_age}

    job:{_job}
    salary:{_salary}

'''.format(
           _name=name,
           _age=age,
           _job=job,
           _salary=salary)
print(msg2)

msg3 = '''-----------info of {0}----------
    name:{0}

    age:{1}

    job:{2}
    salary:{3}

'''.format(
            name,
           age,
           job,
           salary)

print(msg3)

