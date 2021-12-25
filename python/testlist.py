#! /usr/bin/env python3

import json

# name = ["tess", "monty", "mercia", "jenny"]
# # name.append('tom')
# # name.insert(1, 'mark')
# # del name[0]
# name_pop = name.pop()
#
# print(name)
# print(name_pop)

# colore={"蓝色": "blue", "红色": "red", "黄色": "yellow"}
# colore_json = json.dumps(colore)
# data = json.loads(colore_json)
# print(colore)
# print(colore_json)
# print(data)

# import re
#
# print(re.match('wang','wangyufang').span())

# a = {'1', '2', '3', '4', '5'}
# a.pop()
# '1' in a

# list1 = ['mercia', 'tess', 'monty', 'jenny']
# print(list1[0])
# list1[0] = 'tom'
# print(list1)
# list1.append('hhhh')
# print(list1)
# del list1[10]
# print(list1)
# list1.remove('jenny')
# print(list1)

# list1 = ['mercia', 'tess', 'monty', 'jenny']
# list2 = ['qq', 'ww', 'monty', 'jenny']
# a = [list1, list2]
# b = a[0][0]
# print(b)
# import time
#
# def get_time(f):
#
#     def inner(*arg,**kwarg):
#         s_time = time.time()
#         res = f(*arg,**kwarg)
#         e_time = time.time()
#         print('耗时：{}秒'.format(e_time - s_time))
#         return res
#     return inner
# #
# @get_time
# def test1():
#     s = ''
#     for n in range(1,100000):
#         s += str(n)
# test1()
#
# @get_time
# def test2():
#     l = []
#     for n in range(1, 100000):
#         l.append(str(n))
#     s = ''.join(l)
# test2()

# def hi(greet="hi"):
#     return greet + "tess"
#
# print(hi())

# list = [['1', '1', '3'], ['ee', 'vv', 'ff']]
# print(list[0][2])
#
# tuple = (('1', '1', '3'), ('ee', 'vv', 'ff'))
# print(tuple[0][2])

from timeit import timeit

# print("\033[1;35m*** expression is completed! \033[0m")


import json

data = '{(1,2),"大大大"}'
new_data = json.dumps(data, skipkeys=True)
print(new_data)