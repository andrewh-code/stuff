#!/usr/bin/python


#define libraries and constants
import sys 


""" 
1. get the page, read contents into object
2. parse object, find specific words needed
3. look at every href link, find specified '/word/' keyword
4. loop through string until find next '/'. Needed word is in between, /word/<needed word>/
5. Get word and store in data structure (array, list, dictionary?)
6. count the words 
7. append the words into a file
8. open connection to database, and load the words into a table
"""

#==================================================
# Gets file contents from the targetted pages
# Arguments: none
# Return: file_contents
#==================================================
def readFile(char):

	#TO DO: Find appropriate folder location for the files to be extracted
    file_name = "../data/www.scrabblefinder.com starts-with-" + char + ".htm"
	#define file object
    f = open(file_name, 'r')
    file_contents = f.read()
    f.close()
    return file_contents

#==================================================
# Finds the targeted word in the string/file object
# Locates the position of the targetted word in the string. Finds the '/words/' and the next '/'. In between is the word needed
# Arguments: file_contents
# Return: extracted_word, end_word_position 
#==================================================
def extractWord(file_contents):
    #self.file_contents = file_contents
    
    target_link = file_contents.find('/word/')
    if (target_link < 0):
        return None, 0
    else:
        start_word_position = file_contents.find('/', target_link+1)
        end_word_position = file_contents.find('/', start_word_position+1)
        extracted_word = file_contents[start_word_position + 1: end_word_position]
    
    return extracted_word, end_word_position

#==================================================
# Loops through the entire file contents and appends extracted words into a list
# returns the file_contents back to extractWord() function stripping anything before the end_word
# Arguments: file_contents
# Return: list
#==================================================s
def retrieveWords(file_contents):
    list = []
    
    while True:
        word, end_word = extractWord(file_contents)
        if word: #if word is found
            list.append(word)
            file_contents = file_contents[end_word:]
        else:
            break
    
    return list
#==================================================
# Writes the contents of word_list into a new file (.txt format)
# Arguments:
# Return
#==================================================
def outputFile(word_list, char):

    write_file_name = '../data/' + char + '.txt'
    f = open(write_file_name, 'w')
    for x in (word_list):
        f.write(x + '\n')
    f.close()
    
def main():
    
    word_list = []
    sum = 0
    
    #define list, with all the letters in the alphabet (lowercase)
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for char in alphabet_list:
        print "extracting words starting with the letter: " + char 
        file_contents = readFile(char)
        word_list = retrieveWords(file_contents)
        print len(word_list)
        sum += int(len(word_list))
        outputFile(word_list, char)
        word_list = []  #clear list after writing to a file, get ready for the next letter
    print "total number of words extracted:", sum
    
    
if __name__ == "__main__":
    main()