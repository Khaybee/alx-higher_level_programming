#!/usr/bin/python3

"""Define a text file reading function"""


def read_file(filename=""):
    """Reads and prints the contents of a text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
