#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date    20160730
# @date          20160730
'''main
'''
import codecs
import pandas as pd

from decorators import timer
from utils.directory_parser import DirectoryParser


@timer
def main():
    '''main'''
    # Start to parse directory
    parser = DirectoryParser(read_exts=('xls', 'xlsx'), write_ext='csv')
    for src_fn_path, dist_fn_path in parser:
        with codecs.open(src_fn_path, 'rb') as src_file:
            xls_file = pd.read_excel(src_file)
            xls_file.to_csv(dist_fn_path, encoding='utf-8')
            '''
            with codecs.open(dist_fn_path, 'wb') as dist_file:
                csvwriter = csv.writer(dist_file)
                for _, row in xls_file.iterrows():
                    # import pdb;pdb.set_trace()
                    csvwriter.writerow(map(unicode_to_utf8, row))
            '''


if __name__ == '__main__':
    main()
