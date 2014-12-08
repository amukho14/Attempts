__author__ = 'amukhopadhyay'

from mechanize import Browser
from bs4 import BeautifulSoup


def generateSentence(var):
    br = Browser()
    br.set_handle_robots(False)
    br.set_handle_equiv(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    url= 'http://www.oxforddictionaries.com/definition/english/' + str(var)
    # url= 'https://www.google.co.in/search?q=define+utilitarian'
    try:
        br.open(url)
    except:
        print "what word is this, man? " + var
        return
    soup = BeautifulSoup(br.response().read())
    sentence=""
    counter=0
    for i in soup.find_all('ul',{'class':'sentence_dictionary'}):
        if i is not None:
            soup2 = BeautifulSoup(str(i))
            for j in soup2.find_all('li',{'class':'sentence'}):
                if j is not None:
                    sentence = sentence + str(counter+1)+") "+j.string.replace(',',' ').strip()+"\n"
                    counter+=1
                    if counter == 2:
                        return sentence
    return sentence

path = "C:\\Users\\amukhopadhyay\\Desktop\\starredFromQLet.txt"
writePath = "C:\\Users\\amukhopadhyay\\Desktop\\starredFromQLetCorrected2.txt"
# ins = open( path, "r" )
with open(path, 'r') as content_file:
    content = content_file.read()
starredList = content.split('---')
totalWords = content.count('---')
print totalWords
# print starredList
# print (starredList[0]).split(" ",1))[0],"\n"
#
# print (((content.split('---'))[0]).split(" ",1))[1]
# print (starredList[0].split(" ",1))[0]

with open(writePath, 'w') as f:
    i=0
    while i <= totalWords:
        f.write(((starredList[i]).split(" ",1))[0] + "--")
        f.write(((starredList[i]).split(" ",1))[1]+"\n")
        if generateSentence((((starredList[i]).split(" ",1))[0]).strip()) is not None:
            f.write("\n" + generateSentence((((starredList[i]).split(" ",1))[0]).strip()).encode("utf-8")+";;\n")
        else:
            print "what stupidity is this word " + starredList[i].split(" ",1)[0]
        # f.write(((starredList[i]).split(" ",1))[1]+";;")
        # print ((starredList[i]).split(" ",1))[0] + "--","\n" + generateSentence(((starredList[i]).split(" ",1)[0]).strip())+"\n",((starredList[i]).split(" ",1))[1]+";;", i
        i+=1
    f.close()



# from getMnemonics import returnMnemonics
# import csv
# import re
# import json
# import os
# import os

# var = raw_input("Please enter word: ")




