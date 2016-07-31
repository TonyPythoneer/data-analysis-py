#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date    20160730
# @date          20160730
'''main

2522 files (178.2MB)

main
exec_time: 26.2685010433

main_no_unicodecsv
exec_time: 29.3475270271
'''
from decorators import timer
from utils.directory_parser import DirectoryParser
from utils.covert_processer import covert_file


@timer
def main():
    '''main'''
    # Start to parse directory
    parser = DirectoryParser(read_exts=('xls', 'xlsx'), write_ext='csv')

    for src_fn_path, dist_fn_path in parser:
        covert_file(src_fn_path, dist_fn_path)


if __name__ == '__main__':
    main()
