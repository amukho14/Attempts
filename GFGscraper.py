__author__ = 'amukhopadhyay'


from mechanize import Browser
from bs4 import BeautifulSoup

def getOneExperience(url):
    br = Browser()
    br.set_handle_robots(False)
    br.set_handle_equiv(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    # url= raw_input("givepath:")
    url = "http://www.geeksforgeeks.org/amazon-interview-experience-set-158-off-campus/"
    br.open(url)

    soup = BeautifulSoup(br.response().read())

    for i in soup.find_all('h2',{'class':'post-title'}):
        # print i.string
        with open("C:\\Users\\amukhopadhyay\\Desktop\\gfg.html", 'w') as f:
            f.write("<h2>"+str(i.string)+"</h2>")
            f.close()
    for i in soup.find_all('div',{'id':'content'}):
        # print i.prettify()
        soup2 = BeautifulSoup(i.prettify())
        for j in soup2.find_all('p'):
            # print j.contents, j.string, (j.contents)[0]
            if j.string is not None:
                if len(j.string.strip()) >25:
                    if j.string.strip()[:25] == "If you like GeeksforGeeks":
                        exit()
                    # print j.string.strip()[:25]
            # print j.string
            # print j.string.strip()[:25]
            # raw_input("wait")
            with open("C:\\Users\\amukhopadhyay\\Desktop\\gfg.html", 'a') as f:
                # f.write((i.prettify()).encode('utf-8'))
                f.write(str(j))
                f.close()

