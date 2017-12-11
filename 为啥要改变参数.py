#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
'''
6.4.2 我能改变参数吗
1.为什么要修改参数
没看懂这节要说啥。。。。
'''
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def lookup(data, label, name):
    return data[label].get(name)

def store(data, full_name):
    names = full_name.split()
    if len(names) == 2:names.insert(1, '')
    lables = 'first','middle','last'
    for lable, name in zip(lables, names):
        people = lookup(data, lable, name)
        if people:
            people.append(full_name)
        else:
            data[lable][name] = [full_name]

MyNames = {}
init(MyNames)        
print(MyNames)
store(MyNames, 'Maguns Lie Heland')
print(lookup(MyNames, 'middle', 'Lie'))

