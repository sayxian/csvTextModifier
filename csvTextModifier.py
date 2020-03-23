#!/usr/bin/env python

from __future__ import with_statement
import sys
import random
import re

'''
argv[1] as file to import
argv[2] as file to write
argv[3] as item to match, i.e. mds
argv[4] as regex field, i.e. */USD
argv[5] as min
argv[6] as max
argv[7] as decimal place
argv[8] onwards as fields
'''

with open(sys.argv[1]) as imp, open(sys.argv[2],'w') as outp :
    impList = [[word.strip('\n').strip().strip('\"') for word in line.split(',')]
        for line in imp
        ]
    headerList = impList[0]
    print(headerList)
    searchField = headerList.index(sys.argv[3])
    listIndex = []
    for ind in sys.argv[8:]:
        listIndex.append(headerList.index(ind))
    for ln, line in enumerate(impList):
        if re.match(sys.argv[4],line[searchField]):
            for iter in listIndex:
                randNo = random.random()*(int(sys.argv[6])-int(sys.argv[5])) + int(sys.argv[5])
                line[iter]=str(randNo)[:len(str(randNo).split('.')[0])+int(sys.argv[7])+2]
    outp.write('\n'.join(','.join(w
                                for w in line)
                    for line in impList))