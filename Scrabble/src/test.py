#!/usr/bin/python

import itertools
import re
import itertools
from Process import*

p = Process()

s = "abc__"
t = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
blank_positions = []
count_blank = 0
position = 0

collected_lst = []
lst = list(s)

for c in s:
    if (c == "_"):
        count_blank += 1
        blank_positions.append(position)
    position +=1

if (count_blank > 2):
    print "error"
elif (count_blank == 2):
    for char_1 in alphabet:
        lst[blank_positions[0]] = char_1
        for char_2 in alphabet:
            lst[blank_positions[1]] = char_2
            
            #temp_s = "".join(lst)
            #collected_lst.append(temp_s)
            collected_lst.append(p.stringPermutations(lst))
            
elif (count_blank == 1):
    for char_1 in alphabet:
        lst[blank_positions[0]] = char_1
        temp_s = "".join(lst)
        collected_lst.append(temp_s)

permutation_list = []

for str in collected_lst:
    print str
    #permutation_list.append(p.stringPermutations(str))
    print p.stringPermutations(str)
    
print len(permutation_lst)
