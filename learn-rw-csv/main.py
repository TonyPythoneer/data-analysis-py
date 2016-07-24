#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date    20160724
# @date          20160724
'''main
This is ten time faster than that without multiprocessing

(main)       exec_time: 0.0770001411438
(main_no_mp) exec_time: 1.09500002861
'''
from multiprocessing import Pool

from decorators import timer
from utils.directory_parser import DirectoryParser
from utils.io_processer import process_file
from utils.process_bar import ProcessBar


@timer
def main():
    '''main'''
    # Start to parse directory
    directory_parser = DirectoryParser()

    # Wrap func in ProcessBar
    @ProcessBar(participant=directory_parser, attr='process_percentage')
    def do_tasks_with_pool(iterator, func):
        '''do_tasks_with_pool'''
        pool = Pool()
        for args in iterator:
            pool.apply_async(func, args=args)
        pool.close()
    do_tasks_with_pool(iterator=directory_parser, func=process_file)


if __name__ == '__main__':
    main()
