#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from fasttest.driver import *

def openUrl(url=''):
    '''
    Safari 打开url
    :param url:
    :return:
    '''
    # 点击标签页
    lable_button = driver.element_by_name('标签页')
    lable_button.click()

    # 新建标签页
    add_lable_button = driver.element_by_name('新建标签页')
    add_lable_button.click()

    # 输入url
    time.sleep(2)
    input_url = driver.element_by_name('URL')
    input_url.send_keys(url)

    time.sleep(5)
    my_button = driver.element_by_name('我的淘宝')
    my_button.click()


