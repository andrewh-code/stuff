#!/usr/bin/python

#import libraries
import sys

def readFile(char):
    
    content_lst = []
    count = 0
    index_pt = ''
    index_count = 0
    
    file_location = '../data/' + char + '.txt'
    file = open(file_location, 'r')
    
    word = file.readline().strip()  #read first line of file
    content_lst.append(word)
    
    for line in file:
        count += 1
        
        word = line.strip()
        
        if content_lst[count-1][1] != word[1]:
            index_pt = '--' + char + word[1] + '--'
            content_lst.append(index_pt)   #example: --aa, --ab, --ac, ..., -az
            count+=1
            index_count += 1
        content_lst.append(word)  

    file.close()

    #print count+1
    return content_lst, index_count
    
def writeFile(lst, char):
    
    file_location = '../data/' + char + '.txt'
    print file_location
    file = open(file_location, 'w')
    
    for word in lst:
        file.write("%s\n" % word)
    file.close()
    
#def findIndexPoints(lst):
    
    
    
#def writeFile():
    
def main():
    
    lst = []
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    index_count = 0
    
    for char in alphabet_list:
        print "indexing of", char, "dictionary segment"
        lst, index_count = readFile(char)
        print index_count, "indexes were created"
        writeFile(lst, char)
    
    #findIndexPoints(lst)


if __name__ == "__main__":
    main()