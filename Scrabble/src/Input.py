#!/usr/bin/python

#import libraries
import sys

class Input:
    def __init__(self):
        self.input = ''

    def basicInput():
        permutation_list = process.stringPermutations(reordered_search_string)
        filtered_content = process.collectDictionarySegments(reordered_search_string)
        sorted_results = findWords(permutation_list, filtered_content)
        final_results = associatePointScore(sorted_results)
        
    def startsWith():
        search_string = ''
        filtered_content = process.collectDictionarySegments(search_string[0])  #get first letter int he word being searched
        sorted_results = findWords(search_string, filtered_content, 1)
        final_results = associatePointScore(filtered_content)
    
    #TO DO: figure out how to optimize this. Most likely not enough memory in stack to hold all 83000 words in dictionary
    def endsWith():
        search_string = ''
        string = 'abcdefghijklmnopqrstuvwxyz'
        filtered_content = process.collectDictionarySegments(string)
        sorted_results = findWords(search_string, filtered_content, 2)
        final_results = associatePointScore(sorted_results)

    def contains():
        search_string = ''
        string = 'abcdefghijklmnopqrstuvwxyz'
        filtered_content = process.collectDictionarySegments(string)
        sorted_results = findWords(search_string, filtered_content, 0)
        final_results = associatePointScore(sorted_results)
        
    def containsBlanks():
    
    