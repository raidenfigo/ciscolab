# coding=utf-8
__author__ = 'feiwan2'

def func(*str):
    maxstr=''
    for i in str:

        if len(i)> len(maxstr):
            maxstr = i
    return maxstr
a=func('12312314dddddddddddd14','wsdffa','2d','123123123sssdssssss')
print(a)
assert a == '112312314dddddddddddd14'
