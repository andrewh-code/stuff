#!/usr/bin/python

# ============================================================
# Name:             Andrew H
# Course:           Software Engineering 4C03
# Assignment:       1
# Date:             February 17, 2012
#
# Notes:
#   Documentation:  Refer to documentation_a1.txt
#   Dependencies:   input.txt
#                   radix_tree.py  source: http://code.google.com/p/python-radix-tree/source/browse/trunk/radix_tree.py?spec=svn3&r=3)
#                                  author: gschwa74@gmail.com
# ============================================================

#import libraries/modules
import sys
import os
from radix_tree import RadixTree, DuplicateKeyError

#declare global variables
global psd
rt = RadixTree()   

def GetPortsAndCache():    
        global total_ports, cache_size, f, filepath
        
        filepath = os.getcwd()
        filepath = filepath + "/" + "input.txt"
        f = open(filepath, 'r')

        
        total_ports = (f.readline()[:-1])
        cache_size = (f.readline()[:-1])

        if (total_ports.isdigit() == True):
            total_ports = int(total_ports)
        else:
            total_ports = 128
            print "total_ports error, setting to default port number: 128"
        if (cache_size.isdigit() == True):
            cache_size = int(cache_size)
        else:
            cache_size = 32
            print "cache size error, setting to default cache size: 32"

def GetPSD():
    psd = f.readline()
    list_psd = []

    #DESIGN DECISION: Make sure the file does not have a \n character after the last line
    if (psd != ''):
        list_psd = psd.split()
        list_psd[0] = int(list_psd[0])
        list_psd[1] = list_psd[1]       #.replace(':','')
        list_psd[2] = list_psd[2]       #.replace(':','')
        #print list_psd
        return list_psd
    else:
        print "Reached end of file, now exiting\n"
        return False

def Populate():    

    """
    While processing the input file, if a source or 
    destination in a given line is already in the cache,
    it should be put in the most recently-used position
    """
    if (rt.contains(psd_data[1])):
        index_of_duplicate_in_trie = rt.find(psd_data[1])
        
        #find the index of the cache where the duplicate entry is
        for cache_index, temp in enumerate(cache):
            if (temp[1] == index_of_duplicate_in_trie):
                break

        temp_cache_tuple = cache[cache_index]
        temp_dest = temp_cache_tuple[0]
        #DESIGN DECISION: 
            #decide to override the old port number with the most recent port number

        #temp_port = psd_data[0]     
        temp_port = temp_cache_tuple[1]
        
        cache.pop(cache_index)
        cache.append((temp_dest, temp_port))
        
        #updating trie accordingly, 
        rt.delete(temp_dest)
        rt.insert(temp_dest, temp_port)
        #print "after duplicate entry found, re-ordering of trie:"
        #print(rt.debug())
        print "\n"
    else:
        if (len(cache) < cache_size):
            cache.append((psd_data[1], psd_data[0]))
            rt.insert(psd_data[1], psd_data[0])
            #print "append address to cache, less than cache_size"
            #print cache
        else:
            #update the list
            temp_cache_tuple = cache[0]
            temp_dest = temp_cache_tuple[0]
            cache.pop(0)
            cache.append((psd_data[1], psd_data[0]))
            
            #update the trie
            rt.delete(temp_dest)
            rt.insert(psd_data[1], psd_data[0])

    if (rt.contains(psd_data[2])):
    #if the trie (which contains the source MAC address and port) contains the destination address
        count = 1
        psd_dest = psd_data[2]
        temp_port = rt.find(psd_dest)
        print "temp_port is", temp_port
        
        #print "check destination in source\n"
        #print(rt.debug())
        #print "rt complete before while loop", rt.complete(psd_dest[:count])
        print psd_dest, "Root -->", 
        while True:
            if (rt.complete(psd_dest[:count]) == psd_dest):
                #print "rt inside while loop", rt.complete(psd_dest[:count])
                break
            else:
                print psd_dest[:count], "-->",
                count += 1
        print temp_port #psd_data[0]
    else:
        print psd_data[2], "all ports except", psd_data[0]

def main():
    global psd_data, cache               #initialize flag check for reading the file
    psd_data = ()
    cache = []  #initialize and create cache ([2,cache_size] array )
    
    GetPortsAndCache()
    
    while (psd_data != False):
        psd_data = GetPSD()
        if (psd_data == False):
            break
        else:
            Populate()
   
    print(rt.debug())
    print cache, "\n"   
    
if __name__ == '__main__':
    main()
