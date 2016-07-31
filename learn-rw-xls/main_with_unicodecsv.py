#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date    20160730
# @date          20160730
'''main
'''
from decorators import timer
from utils.directory_parser import DirectoryParser
from utils.covert_processer import (
    covert_file, convert_by_unicodecsv
)


@timer
def main():
    '''main'''
    # Start to parse directory
    parser = DirectoryParser(read_exts=('xls', 'xlsx'), write_ext='csv')
    for src_fn_path, dist_fn_path in parser:
        covert_file(src_fn_path, dist_fn_path, convert_by_unicodecsv)


if __name__ == '__main__':
    main()
