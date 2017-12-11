#!/usr/bin/env python
#-*- coding:utf-8 -*-
def try_to_change(n):
    n[2] = 'y'
name = 'Mrs. Entity'
a = try_to_change(name)
print(a)
print(name)
'''
Traceback (most recent call last):
  File "字符串作为参数2.py", line 6, in <module>
    a = try_to_change(name)
  File "字符串作为参数2.py", line 4, in try_to_change
    n[2] = 'y'
TypeError: 'str' object does not support item assignment
外部变量为字符串时作为参数，在函数内为参数赋予新值，外部变量值不会被改变
'''