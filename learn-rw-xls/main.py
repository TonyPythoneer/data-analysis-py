#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date    20160724
# @date          20160724
'''main

2522 files (178.2MB)

main
exec_time: 26.2685010433

main_no_unicodecsv
exec_time: 29.3475270271
'''
from multiprocessing import Pool
import codecs

import xlrd
import unicodecsv as csv

from decorators import timer
from utils.directory_parser import DirectoryParser
from utils.io_processer import process_file
from utils.process_bar import ProcessBar


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
            csvwriter = csv.writer(csvfile, encoding='utf-8')
            for row_index in range(sheet.nrows):
                csvwriter.writerow(sheet.row_values(row_index))


if __name__ == '__main__':
    main()
