#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date    20160724
# @date          20160724
'''main no multiprocessing
'''
from decorators import timer
from utils.directory_parser import DirectoryParser
from utils.io_processer import process_file


@timer
def main():
    '''main'''
    # Start to parse directory
    directory_parser = DirectoryParser()

    # Wrap func in ProcessBar
    for args in directory_parser:
        process_file(*args)


if __name__ == '__main__':
    main()
