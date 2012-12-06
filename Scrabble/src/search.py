#!/usr/bin/python

"""
        A Python Scrabble Search Engine

This program has 5 options for users. The ability to search for words with the tiles they choose,
search for words starting with a specific substring/char, search for words ending with a specific 
subsring/char, search for words containing a specific substring/char, and the option to include
blank tiles in the search. The blank tiles are represented by underscores during the user's input.

The program uses a built in (offline) dictionary containing around 83000 words that is traversed
everytime the user searches for their words.

File structure:
Scrabble\
    __init__.py
    todo.txt
    
    data\
        {a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z} .txt
    src\
        Constants.py
        input.py    #maybe include?
        Points.py
        Preprocess.py
        Process.py
        search.py   #main file
        
    tools\
        delete_dict.py
        extract_words.py
        indexer.py
"""

#import libraries
import sys
import time
from Preprocess import *
from Process import *
from Points import *

def Output(final_results,t2):

    print "word", "\t|   ", "points"
    print "========================="
    for x in range(0, len(final_results)):
        print final_results[x][0], '\t\t', final_results[x][1]
    
    print "\n--------------------\nTotal time taken: ", t2, 'seconds'
    print "Total words: ", len(final_results)

"""
def Input(search_string, option):
    if (option == 0):   #no option chosen
        print "ERROR: No option chosen, exiting."
        sys.exit()
    elif(option == 1):
        print "Searching for words..."
        permutation_list = process.stringPermutations(reordered_search_string)
        filtered_content = process.collectDictionarySegments(reordered_search_string)
        sorted_results = process.findWords(permutation_list, filtered_content)
        final_results = points.associatePointScore(sorted_results)
    elif(option == 2):
        print "Searching for words starting with: ", search_string
        filtered_content = process.collectDictionarySegments(search_string[0])  #get first letter int he word being searched
        sorted_results = process.findWordsContaining(search_string, filtered_content, option)
        final_results = points.associatePointScore(sorted_results)
    elif(option == 3):
        print "Searching for words ending in: ", search_string
        string = 'abcdefghijklmnopqrstuvwxyz'
        filtered_content = process.collectDictionarySegments(string)
        sorted_results = process.findWordsContaining(search_string, filtered_content, option)
        final_results = points.associatePointScore(sorted_results)
    elif(option == 4):
        print "Searching for words containing: ", search_string
        string = 'abcdefghijklmnopqrstuvwxyz'
        filtered_content = process.collectDictionarySegments(string)
        sorted_results = process.findWordsContaining(search_string, filtered_content, option)
        final_results = points.associatePointScore(sorted_results)
    elif(option == 5):
        print "Searching with blank tiles"
        blank_permutation_list = process.blankTileProcessing(search_string)
        print blank_permutation_list
    else:
        print "ERROR: Please choose an option between 1-5"
        sys.exit()
"""

def main():
    
    #define new objects
    preprocess = Preprocess()
    process = Process()
    points = Points()
    
    #declare and initialize variables
    search_string = ''
    option = 0
    count2 = 0      #delete this
    reordered_search_string = ''
    permutation_list = []     #2D list
    blank_permutation_list = []
    filtered_content = []
    sorted_results = []
    final_results = []
    

    #menu options
    print "\nSearch options:\n"
    print "1. Search for words" 
    print "2. Search for words starting with"
    print "3. Search for words ending with"
    print "4. Search for words containing"
    print "5. Search with blank tiles (use the underscore character to represent blanks)\n"
    #option = int(raw_input("Choose option:"))
    option = 5
    #search_string = raw_input('Please input tiles for search: ').lower()
    search_string = "a_b_"
    
    #basic input check
    if (preprocess.checkInput(search_string)):
        reordered_search_string = preprocess.reorderString(search_string) #alphabetize tiles
    else:
        sys.exit()

    t1 = time.time()    #diagnostics
    #Input(search_string, option)    #turned into function for testing purposes
    if (option == 0):   #no option chosen
        print "ERROR: No option chosen, exiting."
        sys.exit()
    elif(option == 1):
        print "Searching for words..."
        permutation_list = process.stringPermutations(reordered_search_string)
        filtered_content = process.collectDictionarySegments(reordered_search_string)
        sorted_results = process.findWords(permutation_list, filtered_content)
        final_results = points.associatePointScore(sorted_results)
    elif(option == 2):
        print "Searching for words starting with: ", search_string
        filtered_content = process.collectDictionarySegments(search_string[0])  #get first letter int he word being searched
        sorted_results = process.findWordsContaining(search_string, filtered_content, option)
        final_results = points.associatePointScore(sorted_results)
    elif(option == 3):
        print "Searching for words ending in: ", search_string
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        filtered_content = process.collectDictionarySegments(alphabet)
        sorted_results = process.findWordsContaining(search_string, filtered_content, option)
        final_results = points.associatePointScore(sorted_results)
    elif(option == 4):
        print "Searching for words containing: ", search_string
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        filtered_content = process.collectDictionarySegments(alphabet)
        sorted_results = process.findWordsContaining(search_string, filtered_content, option)
        final_results = points.associatePointScore(sorted_results)
    elif(option == 5):
        print "Searching with blank tiles"
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        blank_permutation_list = process.blankTileProcessing(reordered_search_string)        
        filtered_content = process.collectDictionarySegments(alphabet)
        
        print "blank_permutation_list: \n"
        print blank_permutation_list
        print len(blank_permutation_list)
        print "\n\n"
        
        #TO DO: Creates a 2D list, gotta convert to 1D list
        #TO DO: find way to use union keyword to take out duplicates, it will take care of one nested for loop in findWords function
        for blank_permutation_string in blank_permutation_list:
            print blank_permutation_string
            print (process.stringPermutations(blank_permutation_string))
            permutation_list.append(process.stringPermutations(blank_permutation_string))
        print permutation_list
        
        sorted_results = process.findWords(permutation_list, filtered_content)
        final_results = points.associatePointScore(sorted_results)
    else:
        print "ERROR: Please choose an option between 1-5"
        sys.exit()
    t2 = time.time() - t1   #diagnostics
    
    Output(final_results, t2)
    
if __name__ == "__main__":
    main()