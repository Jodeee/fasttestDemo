#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fasttest.driver import *

def find_elements_by_id(name):
    '''
    直接调用appium、macaca底层api
    :param name:
    :return:
    '''
    try:
        if Var.driver == 'appium':
            return Var.instance.find_elements_by_id(name)
        elif Var.driver == 'macaca':
            return Var.instance.wait_for_elements_by_id(name)
    except Exception as e:
        raise e

def getText(id):
    '''
    调用已封装api
    :param id:
    :return:
    '''
    text = None
    elements = Driver.wait_for_elements_by_id(id)
    if elements:
        text = elements[0].text
    else:
        raise Exception("Can't find element {}".format(id))
    return text
