#!/usr/bin/python3
"""
Module 0-read_file.py
"""


def read_file(filename=""):
    """ function that reads a text file """
    with open(filename) as f:
        readfile = f.read()
    return readfile
