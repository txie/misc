#!/bin/env python
# -*- coding: utf-8 -*-
import getopt
import sys

"""
➜  misc git:(master) ✗ python GetOptTest.py -i a -o b c d e f
opts:  [('-i', 'a'), ('-o', 'b')]
args:  ['c', 'd', 'e', 'f']
input file:  a
output file:  b

➜  misc git:(master) ✗ python GetOptTest.py 1234 -i a -o b
opts:  []
args:  ['1234', '-i', 'a', '-o', 'b']
input file:
output file:

"""

if __name__ == '__main__':
    argv = sys.argv[1:]
    input_file = ''
    output_file = ''
    try:
        (opts, args) = getopt.getopt(argv, 'hi:o:', ['input_file=', 'output_file'])
    except getopt.GetoptError:
        print 'GetOptTest -i <input file> -o <output file>'
        sys.exit(2)

    print 'opts: ', opts
    print 'args: ', args
    for opt, arg in opts:
        if opt == '-h':
            print 'GetOptTest -i <input file> -o <output file>'
            sys.exit()
        elif opt in ('-i', '--input-file'):
            input_file = arg
        elif opt in ('-o', '--output-file'):
            output_file = arg

    print 'input file: ', input_file
    print 'output file: ', output_file

