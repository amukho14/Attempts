__author__ = 'amukhopadhyay'


from mechanize import Browser
from bs4 import BeautifulSoup

br = Browser()
br.set_handle_robots(False)
br.set_handle_equiv(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
url= 'http://www.chomsky.info/articles.htm'
br.open(url)

soup = BeautifulSoup(br.response().read())

# <div style="padding-top: 10px;">
# count_mn=0
# mnemonics=""
for i in soup.find_all('div',{'class':'lk'}):

    soup2 = BeautifulSoup(str(i))
    for j in soup2.find_all('a'):
        link = j['href']
        if link[-3:] == 'htm':
            print "http://www.chomsky.info/"+j['href']
            br.open("http://www.chomsky.info/"+j['href'])
            soup3 = BeautifulSoup(br.response().read())
            soup4 = soup3.find('td',{'class':'body2'})
            print soup3.find('div',{'class','title'}).string
            # print soup4.prettify
            blah = raw_input("wait here")
            with open('C:\\Users\\amukhopadhyay\\Desktop\\chomsky.html', 'a') as f:
                f.write("<h>"+soup3.find('div',{'class':'title'}).string+"+</h>")
                f.write((soup4.prettify()).encode('utf-8')+",")
                f.write("<br>________________________________________________________ <br>")
                f.close()
        else:
            print "pdf, let's read this later"
    # buildDef = ""
    # print soup2.prettify()
    # for x in soup2.find_all('div', {'class':'row-fluid'}):
    #     soup3 = BeautifulSoup(str(x))

