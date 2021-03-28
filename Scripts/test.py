#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from fasttest.driver import wd

def test_scripts(name):
    '''
    macaca 查找元素
    :param name:
    :return:
    '''
    element = wd.driver.find_elements_by_class_name(name)
    return element

def test_randint():
    '''
    获取随机数
    :return:
    '''
    num = random.randint(0, 9)
    return num

if __name__ == '__main__':
    num = test_randint()
    print(num)