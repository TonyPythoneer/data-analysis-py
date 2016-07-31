#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date    20160730
# @date          20160730
'''To get source and distribution directories of filename
'''
import os

import configs


class DirectoryParser(object):
    _src_dir = configs.SRC_DIR
    _dist_dir = configs.DIST_DIR

    def __init__(self, read_exts=("csv",), write_ext="csv"):
        # Pre init
        self._pre_init()

        # Init instance variables
        self.filename_list = os.listdir(self._src_dir)
        self._init_read_exts(read_exts)
        self._write_ext = write_ext

        # For process bar
        self.total_file_num = len(self.filename_list)

    def __iter__(self):
        '''Return src_filename_path, dist_filename_path'''
        for fn in self.filename_list:
            name, ext = os.path.splitext(fn)  # Get 'abc' and '.txt'
            ext = ext[1:].lower()  # Exclude dot
            if ext in self._read_exts:
                dist_fn = name + '.' + self._write_ext
                src_fn_path = os.path.join(self._src_dir, fn)
                dist_fn_path = os.path.join(self._dist_dir, dist_fn)
                yield src_fn_path, dist_fn_path

    def _pre_init(self):
        '''Check the dir exists or not'''
        # Verify src dir, otherwise rasing error
        if not os.path.isdir(self._src_dir):
            raise IOError('src folder not found')

        # Verify dist dir, otherwise creating the directory
        if not os.path.isdir(self._dist_dir):
            print "Create `dist` directory"
            os.mkdir(self._dist_dir)

    def _init_read_exts(self, exts):
        '''This property only accepts string, list and tuple of type'''
        # Verify type of proerty
        if isinstance(exts, str):
            self._read_exts = (exts,)
        elif isinstance(exts, (list, tuple)):
            self._read_exts = exts
        else:
            # Raise error
            raise TypeError('read_exts only accepts string, list and tuple')
