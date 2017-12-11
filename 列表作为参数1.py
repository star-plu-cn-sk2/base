#!/usr/bin/env python
#-*- coding:utf-8 -*-
def change(n):
    n[0] = 'Mr. Gumby'
    return n
names = ['Mr. Entity', 'Mrs. Thing']
name = change(names)
print name 
print names
'''
['Mr. Gumby', 'Mrs. Thing']
列表作为参数时可以被修改i.两个变量同时引用一个列表时，他们时在同时使用一个列表。
'''