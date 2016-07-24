#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date    20160723
# @date          20160723
'''To show process bar on terminal
'''
import time
from threading import Thread
from sys import stdout


class ProcessBar(Thread):
    '''
    example:
    >>> [===       ] ... 30%
    '''
    TEMPLATE = "\r[{remaining:<10}] ... {percentage:<4}"

    def __init__(self, participant, attr):
        '''
        participant (instance)
        attr (str)
        '''
        Thread.__init__(self)
        self.participant = participant
        self.attr = attr

    def __call__(self, func):
        '''To be used a decorator'''
        def decorated_func(*args, **kwargs):
            self.start()
            # Excute func
            func(*args, **kwargs)
            self.join()
        return decorated_func

    def run(self):
        '''print'''
        while True:
            # Print process bar
            remaining = "=" * int(self.percentage * 10)
            percentage = str(int(self.percentage * 100)) + "%"
            print self.TEMPLATE.format(remaining=remaining,
                                       percentage=percentage),

            # Leave loop
            if self.is_complete:
                break

            # System process
            stdout.flush()
            time.sleep(.01)
        print '\n',

    @property
    def percentage(self):
        '''The number ranges from 0 to 1'''
        return getattr(self.participant, self.attr)

    @property
    def is_complete(self):
        '''The bar is complete or not '''
        return self.percentage >= 1
