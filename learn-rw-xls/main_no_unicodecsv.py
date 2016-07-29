#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date    20160724
# @date          20160724
'''main

func_name: main
exec_time: 0.0265839099884
'''
#from multiprocessing import Pool
import codecs
import csv

import xlrd

from decorators import timer
from utils.directory_parser import DirectoryParser


@timer
def main():
    '''main'''
    # Start to parse directory
    directory_parser = DirectoryParser(extension='xls')

    for src_fn_path, dist_fn_path in directory_parser:
        # Read xls file
        book = xlrd.open_workbook(src_fn_path)
        sheet = book.sheet_by_index(0)

        # Write csv file
        with codecs.open(dist_fn_path, 'wb') as csvfile:
            csvwriter = csv.writer(csvfile)
            for row_index in range(sheet.nrows):
                row = sheet.row_values(row_index)
                csvwriter.writerow(map(unicode_to_utf8, row))

            '''
            csvwriter = csv.writer(csvfile, encoding='utf-8')
            for row_index in range(sheet.nrows):
                csvwriter.writerow(sheet.row_values(row_index))
            '''


def unicode_to_utf8(unicode_):
    # Exclude null string and non-unicode
    if not (unicode_ and isinstance(unicode_, unicode)):
        return unicode_
    return unicode_.encode('utf-8')


if __name__ == '__main__':
    main()
