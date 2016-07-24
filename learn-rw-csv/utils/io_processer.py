#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date    20160723
# @date          20160723
'''io processer
'''
import codecs
import chardet


def parse_encoding(byte):
    '''parse encoding'''
    detect_result_dict = chardet.detect(byte)
    encoding = detect_result_dict['encoding']
    return encoding


def encoding_string_coverter(orginal_encoding, target_encoding):
    '''To decide input and ouput of the encoding converter'''
    def covert_string_encoding(string):
        '''Start to convert the encoding'''
        decoded_str = string.decode(orginal_encoding, errors="ignore")
        encoded_str = decoded_str.encode(target_encoding)
        return encoded_str
    return covert_string_encoding


def process_file(src_filename_path, dist_filename_path):
    '''process file'''
    # Read source file
    with codecs.open(src_filename_path, 'rb') as src_file:
        # Build utf8 encoding coverter
        src_byte = src_file.readline()
        src_encoding = parse_encoding(src_byte)
        to_utf8 = encoding_string_coverter(src_encoding, 'utf-8')

        # Write dist file
        with codecs.open(dist_filename_path, 'wb') as dist_file:
            while src_byte:
                # Write dist file, and then read next line of source file
                dist_file.write(to_utf8(src_byte))
                src_byte = src_file.readline()
