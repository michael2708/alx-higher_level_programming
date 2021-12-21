#!/usr/bin/python3
"""
Module 1-write_file.py
"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file """
    with open(filename, encoding="utf-8") as f:
        count = 0
        for line in f:
            count += 1
    return count
