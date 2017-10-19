'''
Let's imagine , we have a tone of logs files, 
If we used a for loop on the log file, this can take a while and a lot of memory
Instead of loop to every elemnt, we could process on line at a time before reading the next on into mem
'''

import sys

inname = sys.argv[1]
outname = sys.argv[2]


with open(inname) as infile:  #this represent the actual log file
    with open(outname, "w") as outfile:  #we will rigth all the warning on this file
        warnings = (l for l in infile if 'WARNING' in l)  #loop to all the file and return a generator(one element at time)
        for l in warnings:  #As we already have the generator, we can loop on it to get the file
            outfile.write(l)




