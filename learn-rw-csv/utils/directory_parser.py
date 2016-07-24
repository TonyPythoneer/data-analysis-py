#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date    20160723
# @date          20160723
'''To get source and distribution directories of filename
'''
import os
import logging

import configs


def _isdir(path):
    '''Check the directories of the class variables exist or not'''
    if not os.path.isdir(path):
        logging.error('The `%s` doesn\'t exist', path)
        raise IOError


def _check_src_and_dict_dirs(src_dir, dist_dir):
    '''Check the dir exists or not'''
    _isdir(src_dir)
    try:
        _isdir(dist_dir)
    except IOError:
        print "Create `dist` directory"
        os.mkdir(dist_dir)


class DirectoryParser(object):
    src_dir = configs.SRC_DIR
    dist_dir = configs.DIST_DIR

    def __init__(self):
        # Check the dir exists or not
        _check_src_and_dict_dirs(self.src_dir, self.dist_dir)

        # Init instance variables
        self.filename_list = os.listdir(self.src_dir)

        # For process bar
        self.total_file_num = len(self.filename_list)
        self.processed_file_num = 0

    def __iter__(self):
        # Get path of every CSV file
        for filename in self.filename_list:
            self.processed_file_num += 1
            _, ext = os.path.splitext(filename)
            if ext.lower() == '.csv':
                src_filename_path = os.path.join(self.src_dir, filename)
                dist_filename_path = os.path.join(self.dist_dir, filename)
                yield src_filename_path, dist_filename_path

    @property
    def process_percentage(self):
        '''The number ranges from 0 to 1'''
        return self.processed_file_num / float(self.total_file_num)
