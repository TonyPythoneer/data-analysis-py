#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date    20160706
# @date          20160618
'''manage
'''
import sys
from subprocess import call


COMMANDS = ('run', 'profile', 'pstats')


def print_hint(commands):
    print 'Please input the command as follow:'
    print 'Example: python manage.py run'
    for index, command in enumerate(commands):
        print '    {}. {}'.format(index+1, command)


def main():
    if len(sys.argv) < 2:
        print_hint(COMMANDS)
        return

    cmd_args = sys.argv[1:]
    first_arg = cmd_args[0]
    if first_arg == 'run':
        call('python main.py', shell=True)
    elif first_arg == 'profile':
        import cProfile
        cProfile.run('from main import main;main()', filename='main.profile')
    elif first_arg == 'pstats':
        import pstats
        p = pstats.Stats("main.profile")
        p.strip_dirs().sort_stats("cumulative", "name").print_stats(0.5)
    else:
        print_hint(COMMANDS)


if __name__ == '__main__':
    main()
