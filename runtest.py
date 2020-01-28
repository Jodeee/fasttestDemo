#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from oktest import *
from concurrent import futures

if __name__ == '__main__':

    project = Project()

    project.start()

# def test(test,test1):
#     print(test,test1)
#     return '{}'.format(test+test1)
#
# ex = futures.ThreadPoolExecutor()
# worker_list = []
# worker_list.append(ex.submit(test(test1=1,test=2)))
# for f in futures.as_completed(worker_list):
#     # if f.result() is not None:
#     print(f)
