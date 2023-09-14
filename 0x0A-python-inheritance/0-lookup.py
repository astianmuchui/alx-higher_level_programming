#!/usr/bin/python3

'''
    Returns the list of available attributes and methods in an obj
'''


def lookup(obj):
    '''
    Returns the list of available attributes and methods in an obj
    '''
    return (dir(obj))
