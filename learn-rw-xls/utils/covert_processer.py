#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date    20160723
# @date          20160723
'''covert processer
'''
import codecs
import csv

import xlrd
import unicodecsv


def __unicode_to_utf8(unicode_):
    # Exclude null string and non-unicode
    if not (unicode_ and isinstance(unicode_, unicode)):
        return unicode_
    return unicode_.encode('utf-8')


def convert_by_csv(csvfile, sheet):
    '''The csv is standard python module'''
    csvwriter = csv.writer(csvfile)
    for row_index in xrange(sheet.nrows):
        row = sheet.row_values(row_index)
        csvwriter.writerow(map(__unicode_to_utf8, row))


def convert_by_unicodecsv(csvfile, sheet):
    '''The unicode is standard python module'''
    csvwriter = unicodecsv.writer(csvfile, encoding='utf-8')
    for row_index in xrange(sheet.nrows):
        row = sheet.row_values(row_index)
        csvwriter.writerow(row)


def covert_file(src_fn_path, dist_fn_path, convert_csv_func=convert_by_csv):
    '''covert file'''
    # Read source xls file
    book = xlrd.open_workbook(src_fn_path)
    sheet = book.sheet_by_index(0)

    # Write dist csv file
    with codecs.open(dist_fn_path, 'wb') as csvfile:
        convert_csv_func(csvfile, sheet)
