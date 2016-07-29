#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160706
#  @date          20160706
'''Record excute time of function
'''
import time


def timer(func):
    '''timer as a decorator '''
    def args_wrapper(*args, **kwargs):
        '''timer wrapper'''
        # Record excute time
        start = time.time()
        func_result = func(*args, **kwargs)
        end = time.time()

        # Report excute time
        print "=== START ==="
        print "func_name: %s" % func.__name__
        print "exec_time: %s" % str(end-start)
        print "=== END ==="

        return func_result
    return args_wrapper
