#!/usr/bin/python
# -*- coding: cp936 -*-
# -*- coding: encoding -*-

#map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
a=map(str,[1,2,3])
print type(a)
def fun(x):
    return x*x
b=map(fun,[1,2,3,4])
print b
#reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def fun1(x,y):
    return x+y
c=reduce(fun1,[1,2,3,4])#相当于1+2+3+4
print c
