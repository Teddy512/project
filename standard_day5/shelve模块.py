__author__ = "Alex Li"

import shelve
import datetime

'''

    python中的shelve模块，可以提供一些简单的数据操作
    他和python中的dbm很相似。

    区别如下：
    都是以键值对的形式保存数据，不过在shelve模块中，
    key必须为字符串，而值可以是python所支持的数据
    类型。在dbm模块中，键值对都必须为字符串类型。
'''
d = shelve.open('shelve_test')  # 打开一个文件
print(d.get("name"))
# 删除shelve对象中的某个键值对
# del d['info']
print(d.get("info"))
print(d.get("date"))

info =  {'age':22,"job":'it'}

name = ["alex", "rain", "test"]
d["name"] = name  # 持久化列表
d["info"] = info  # 持久dict
d['date'] = datetime.datetime.now()
print (d.get('name'))
print (d['name'])
d.close()



'''
    python中的shelve模块，可以提供一些简单的数据操作
    他和python中的dbm很相似。

    区别如下：
    都是以键值对的形式保存数据，不过在shelve模块中，
    key必须为字符串，而值可以是python所支持的数据
    类型。在dbm模块中，键值对都必须为字符串类型。

    sh['a'] = 'a'
    sh['c'] = [11, 234, 'a']
    sh['t'] = ('1', '2', '3')
    sh['d'] = {'a':'2', 'name':'Hongte' }
    sh['b'] = 'b'
    sh['i'] = 23

    我们可以获取一个shelve对象
    sh = shelve.open('c:\\test\\hongten.dat', 'c')

    删除shelve对象中的某个键值对
    del sh['d']

    遍历所有数据
    for item in sh.items():
        print('键[{}] = 值[{}]'.format(item[0], sh[item[0]]))

    获取某个键值对
    print(sh['a'])

    关闭shelve对象:
    sh.close()

  
          API中强调
    Do not rely on the shelf being closed automatically;
    always call close() explicitly when you don’t need
    it any more, or use a with statement with
    contextlib.closing().

'''