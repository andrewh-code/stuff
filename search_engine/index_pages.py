#!/usr/bin/python

import sys

#define global variables
#index = []

#==================================================
# input: index (list), keyword (string), url (string)
# output: 
# Find the keyword in the list and add the associated URL to its associated URL list.
# If the keyword is not in the index, then append the keyword and its associated URL to the end of the list
#==================================================
def AddToIndex(index, keyword, url):
    #format for index = [[keyword, [url, count]], [keyword, [url, count]]]
    #if keyword already in index, add url to the index list
    for entry in index:
        #if the keyword is already in the index, add the url to the keyword
        #if the url is already associated with the keyword, don't add in the url again
        if (keyword == entry[0]):
            for elements in entry[1]:
                if elements[0] == url
                    return 
                entry[1].append([url, 0])
            return
    #if keyword is not in the index, add the keyword and url to the list
    index.append([keyword, [url, 0]])

#==================================================
# input: index (list), keyword (string)
# output: list 
# lookup a specific keyword and output the URLs associated with the keyword
# If keyword is not found, return nothing
#==================================================
def Lookup(index, keyword):
    #output: list of URLs associated with keyword
    for entry in index:
        if (keyword == entry[0]):
            return entry[1]
    #if keyword not in index, return empty list
    return []

#==================================================
# input: index (list), url (string), content (string)s
# update the index to include all the word occurences found
# in the page content
# add to the keyword's associated url list
#==================================================
def AddPageToIndex(index, url, content):

    temp_words = content.split()
    for x in temp_words:
        AddToIndex(index, x, url)

#==================================================
# input: source (string), splitlist (string)
# output: list of the source separated by the chars in the splitlist
# split the content of a page based on the list of chars to 
# split the sentences into keywords
#
#==================================================
def SplitString(source, splitlist):
    output = []
    atsplit = True
    for character in source:
        if character in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(character)
                atsplit = False
            else:
                output[-1] = output[-1] + character
    return output
    
def main():
    #index = []
    index = [['udacity', ['http://udacity.com', 'http://npr.org']],
             ['computing', ['http://acm.org']]]
    
    AddToIndex(index, "hello", "http://www.google.ca")
    print Lookup(index, "udacity")
    

if __name__ == "__main__":
    main()