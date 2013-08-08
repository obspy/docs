#!/usr/bin/env python
"""
Created on Aug 27, 2012

@author: behry
"""

# Write a function that takes a list of program 
# names as input and returns a dictionary with 
# the programs' complete path on the current computer
# system as values. Programs that are not found should
# have the value None.

import os

def findprograms(proglist):
    outdict = {}
    dirlist = os.environ['PATH'].split(":")
    for prog in proglist:
        for dir in dirlist:
            fname = os.path.join(dir, prog)
            if os.path.isfile(fname):
                outdict[prog] = fname
        if prog not in outdict.keys():
            outdict[prog] = None
    return outdict


if __name__ == '__main__':
    print findprograms(['psxy', 'emacs', 'blub', 'blub'])
