#!/usr/bin/env python
#-*- coding:utf-8 -*-
def change(n):
    n[0] = 'Mr. Gumby'
    return n
names1 = ['Mr. Entity', 'Mrs. Thing']
names2 = names1[:]    #复制一个列表
change(names1)
print names1 
print names2
'''
['Mr. Gumby', 'Mrs. Thing']
['Mr. Entity', 'Mrs. Thing']
复制列表之后修改原来列表的值，新的列表值不会变化
'''