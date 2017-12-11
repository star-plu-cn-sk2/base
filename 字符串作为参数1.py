#!/usr/bin/env python
#-*- coding:utf-8 -*-
def try_to_change(n):
    n = 'Mr. Gumby'
    print(n)
#    return n
name = 'Mrs. Entity'
a = try_to_change(name)
print(a)
print(name)
'''
Mr. Gumby
None
Mrs. Entity
外部变量为字符串时作为参数，在函数内为参数赋予新值，外部变量值不会被改变
'''