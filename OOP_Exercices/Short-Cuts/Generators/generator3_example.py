'''
Yield  like run , return something
the != with return, if recall the functiona , yield will return the next element where is left
previously
'''

import sys
iname, outname = sys.argv[1: 3]



def warnings_filter(insequence):
    for l in insequence:
        if 'WARNING' in l:
            yield l.replace('\tWARNING', '')






with open(inname) as infile:
    with open(outname, 'w') as outfile:
        filter = warnings_filter(infile)
        for l in filter:
            outfile.write(l)