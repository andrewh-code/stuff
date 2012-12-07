#!/usr/bin/python

#import dictionaries
import sys
import itertools

class Process:
    def __init__(self):
        self.search_string = ''
    
    #============================================================
    # Takes the user input (tile set, with the blanks) and replaces the blank with each letter in the alphabet.
    # The function takes permutations of each new possible search string input and appends the set to a collection
    # ie) a_b_ ==> aaba, aabb, aabc, aabd,...azbx, azby, azbz (26x26 combinations in total, then take a permutation of each combination)
    # Input: search_string
    # Output: blank_permutation_lst
    #============================================================
    def blankTileProcessing(self, search_string):
        
        self.search_string = search_string
        blank_count = 0
        blank_position = 0
        tile = ''
        letter1 = ''
        letter2 = ''
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        blank_position_lst = []     #hold max 2 elements
        search_string_lst = []
        blank_permutation_set = ()
        blank_permutation_lst = []
        
        search_string_lst = list(search_string)
        #TO DO: NOT NECESSARY - When using reordered_search_string variable
        for tile in search_string:                      
            if (tile == '_'):
                blank_count += 1
                blank_position_lst.append(blank_position)
            blank_position += 1
        
        if (blank_count == 2):
            for letter1 in alphabet:
                search_string_lst[blank_position_lst[0]] = letter1
                for letter2 in alphabet:
                    search_string_lst[blank_position_lst[1]] = letter2
                    #blank_permutation_set = set(list(map("".join, itertools.permutations(search_string_lst))))
                    blank_permutation_lst.append("".join(search_string_lst))
        elif (blank_count == 1):
            for letter2 in alphabet:
                search_string_lst[blank_position_lst[0]] = letter2
                blank_permutation_lst.append("".join(search_string_lst))
        else:
            print "ERROR: Wrong number of blank tiles inputted, please make sure there is at least 1 and maximum 2 blank tiles in the search string."
            sys.exit()
        
        return blank_permutation_lst
    
    #==================================================
    # This function takes in the search string entered and finds all possible permutations of the letters.
    # For now, takes up to 10 letters (or tiles)
    # Input: search_string
    # Output:
    #==================================================
    def stringPermutations(self, search_string):
    
        self.search_string = search_string
        self.permutation_list = []
        self.temp_set = set()
        self.permutation_set = set()
        
        #starting from 2 letter words (no one letter words) up until the number of tiles inputted 
        for x in range(2, len(self.search_string)+1):
            self.temp_set = set(map("".join, itertools.permutations(self.search_string, x)))
            self.permutation_set = self.permutation_set.union(self.temp_set)
            self.permutation_list = list(self.permutation_set)

        return self.permutation_list
        
    #========================================
    # takes the alphabetized list of tiles and from there, extracts the dictionary segments (pages) based on those tiles
    # and ouputs them into a big list
    # Input: reordered_search_string
    # Output: content
    #========================================
    def collectDictionarySegments(self, reordered_search_string):
        #TO DO: check for nothing inputted, should be taken care of by checkInput though
        self.reordered_search_string = reordered_search_string
        self.new_set = set()
        self.content = []
        self.file_name = ''
        
        """
        #deprecated with the use of set() data structure
        #removing duplicate tiles from set to avoid collecting the same segment(s) again
        self.new_set.append(self.reordered_search_string[1])  #always insert the very first element of the list into the new set
        for x in range(1, len(self.reordered_search_string)):
            if (self.reordered_search_string[x] != self.reordered_search_string[x-1]):
                self.new_set.append(self.reordered_search_string[x])
        """
        
        self.new_set = set(reordered_search_string)
        #go through tiles and collect their respective dictionary segments, append results into one giant list
        #TO DO: Error checking for opening/reading file
        for char in self.new_set:
            self.file_name = '../data/' + char + '.txt'
            try:
                search_file = open(self.file_name)
                for line in search_file:
                    self.content.append(line.strip())
            except IOError:
                print "Error: Can't find", char, "dictionary section"

            search_file.close()
            
        #print self.content
        return self.content
        
    #========================================
    # Takes the list of tile permutations and the collected dictionary segments. Searches for each unique permutation 
    # in the dictionary segments
    # Input: permutation_list, filtered_content
    # Output: final_word_list (sorted in alphabetical order and length)
    #========================================
    def findWords(self, permutation_list, filtered_content):
        
        self.permutation_list = permutation_list
        self.filtered_content = filtered_content
        self.final_word_list = []
        
        #TO DO: Is this check necessary?
        if (len(self.permutation_list) > len(self.filtered_content)):
            print "Error: list of possible words to search is greater than the amount being searched"
            sys.exit()
        
        #TO DO: find a way to optimize this - DONE (use of union for sets in stringPermutations())
        #       find a way to optimize this EVEN MOAR (binary search? local search? use index?
        for str in self.permutation_list:
            for str_content in self.filtered_content:    #basic/easiest algorithm for search
                    if (str == str_content):            
                        self.final_word_list.append(str)
                        break
        
        return sorted(self.final_word_list)
        
    #========================================
    # Function used for finding words that contain the search string, or words taht start with the search string, or
    # words that end in the search string
    # Input: search_string, filtered_content, option/case
    # Output: final_word_list
    #========================================
    def findWordsContaining(self, search_string, filtered_content, option):
        
        #define/initialize variables
        self.exact_string = search_string
        self.filtered_content = filtered_content
        self.final_word_list = []
        self.option = option
        
        if (option == 4):   #search for words containing the search string
            for str_content in self.filtered_content:
                if ((len(search_string) <= len(str_content)) and (search_string in str_content)):
                    self.final_word_list.append(str_content)
        elif (option == 2):  #if search_string is in the word at the beginning
            for str_content in self.filtered_content:
                if ((len(search_string) <= len(str_content) and (search_string == str_content[0:len(search_string)]))):   #last condition might be redundant, check to see
                    self.final_word_list.append(str_content)
        elif (option == 3):   #if search_string is at the end of the word
            for str_content in self.filtered_content:
                if (((len(search_string) <= len(str_content)) and (search_string == str_content[-(len(search_string)):]))):   #last condition might be redundant, check to see
                    self.final_word_list.append(str_content)
        else:
            print "Error: case option not set correctly, can not continue searching for words"
            sys.exit()

        return self.final_word_list

