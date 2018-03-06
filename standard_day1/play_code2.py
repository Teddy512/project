#  authon :teddy
names=input ("please input you name")
age=int (input("age"))
job=input("you job")
salary=input("you salary")

info ='''-----info of %s------
      name:%s
      age:%s
      job:%s
      salary:%s
      

'''%(names,names,age,job,salary)


info2='''-----info of {_name}-------
     name:{_name}
     age:{_age}
     job:{_job}
     salary{_salary}
     

'''.format(_name=names,_age=age,_job=job,_salary=salary)


info3='''----=info of {0}------
         name:{0}
         age:{1}
         job:{2}
         salary:{3}
'''.format(names,names,age,job,salary)

print (info)
print ("1111")
print (info2)
print ("555")
print (info3)