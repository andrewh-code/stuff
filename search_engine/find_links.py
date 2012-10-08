#!/usr/bin/python

import sys
import urllib

#define global variables
global index
index = []

#==================================================
# input: url (string)
# output: string representation of page or none
# get page contents of url inputted
#==================================================
def GetPage(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""
        
#==================================================
# input: none
# output: file_contents (html code of a page)
# Temporary function to simulate GetPage
#==================================================
def GetFileContents():
    
    with open('D:\python_stuff\search_engine\udacity_sample.htm', 'r') as f:
        file_contents = f.read()
    f.closed
    
    return file_contents


def GetNextTarget(page):
    #self.page = page
    
    start_link = page.find('<a href=')
    if (start_link < 0):
        return None, 0
    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote+1)
        url_address = page[start_quote + 1:end_quote]
        
        return url_address, end_quote


def GetAllLinks(page):
    link_list = []
    
    while True:
        url, end_quote_position = GetNextTarget(page)
        if url:
            link_list.append(url)
            page = page[end_quote_position:]
        else:
            break
        print url, end_quote_position
        
    return link_list

def CrawlWeb(seed):
    to_crawl = [seed]
    crawled = []
    index = []
    page_content
    
    while to_crawl:
        page = to_crawl.pop()
        if page not in crawled:
            
            #get content from the page being crawled; add page to the index of pages
            content = GetPage(page)
            AddPageToIndex(index, page, page_content)
            
            union(to_crawl, GetAllLinks(page))
            crawled.append(page)
        #return crawled
        return index

#Unit 4
#=================================================================================


def AddToIndex(index, keyword, url):
    #if keyword already in index, add url to the index list
    for entry in index:
        if (keyword == entry[0]):
            entry[1].append(url)
            return
    #if keyword is not in the index, add the keyword and url to the list
    index.append([keyword, [url]])

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
            

#=================================================================================

def main():
    page = GetFileContents()
    link_list = []
    
    link_list = GetAllLinks(page)
    

if __name__ == "__main__":
    main()