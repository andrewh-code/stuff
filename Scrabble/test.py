import sys
import itertools

permutation_set = ()
permutation_list = []
search_string = "abcdd"
for x in range(2, len(search_string)+1):
            permutation_set = list(set(map("".join, itertools.permutations(search_string, x))))
            permutation_list.append(permutation_set)
print permutation_list

