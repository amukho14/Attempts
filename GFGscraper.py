__author__ = 'amukhopadhyay'


from mechanize import Browser
from bs4 import BeautifulSoup
from bs4.dammit import EntitySubstitution
from Queue import Queue
from threading import Thread
import threading





def substitute_html_entities(str):
    # return EntitySubstitution.substitute_html(str)
    # return EntitySubstitution.substitute_html(str).replace("&acirc;&euro;&trade;","\'").replace("&acirc;&euro;&oelig;","\"").replace("&acirc;&euro;","\"").replace("&gt",">")\
    return EntitySubstitution.substitute_html(str).replace("&ldquo;","\"").replace("&rdquo;","\"").replace("&rsquo;","'")



def getOneExperience(q):
    url = q.get()
    print url
    pathToFile = "C:\\Users\\amukhopadhyay\\Desktop\\gfg.html"
    writeToFile=""
    while True:
        br = Browser()
        br.set_handle_robots(False)
        br.set_handle_equiv(False)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        # url= raw_input("givepath:")
        # url = "http://www.geeksforgeeks.org/amazon-interview-experience-set-158-off-campus/"
        br.open(url)

        soup = BeautifulSoup(str(br.response().read()), from_encoding="utf-8")
        # print(soup.prettify(formatter=substitute_html_entities))
        soup = BeautifulSoup(soup.prettify(formatter=substitute_html_entities))

        for i in soup.find_all('h2',{'class':'post-title'}, limit=1):
            # print i.string
            # with open(pathToFile, 'w') as f:
            #     f.write("<h2>"+str(i.string)+"</h2>")
            #     f.close()
            writeToFile +="<h2>"+str(i.string)+"</h2>"
            print writeToFile
        flag=0
        for i in soup.find_all('div',{'id':'content'}):
            # print i.prettify()
            soup2 = BeautifulSoup(i.prettify())
            if flag == 1:
                break
            for j in soup2.find_all('p'):
                # print j.contents, j.string, (j.contents)[0]
                if flag == 1:
                    break
                if j.string is not None:
                    if len(j.string.strip()) >25:
                        if j.string.strip()[:25] == "If you like GeeksforGeeks":
                            flag=1
                writeToFile+=(j.encode('utf-8').replace("\'",""))
        # print writeToFile+"yp"

    MY_LOCK.acquire()
    with open(pathToFile, 'a') as f:
        f.write(writeToFile)
        f.close()
        print"wrote"
    MY_LOCK.release()
    q.task_done()

def hitPage(url = "http://www.geeksforgeeks.org/tag/amazon/"):
    #from the page extract all the interviewExperiencesLinks
    br = Browser()
    br.set_handle_robots(False)
    br.set_handle_equiv(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    # url= raw_input("givepath:")
    # url = "http://www.geeksforgeeks.org/amazon-interview-experience-set-158-off-campus/"
    br.open(url)
    #different thread for link on same page
    #same thread to iterate of each of the pages
    q = Queue(maxsize=0)


    #thirteen links on each page and of course, lucky number thirteen.
    num_threads = 1
    soup = BeautifulSoup(str(br.response().read()), from_encoding="utf-8")

    for i in soup.find_all('h2',{'class':'post-title'}):
        soup2=BeautifulSoup(i.prettify())
        for j in soup2.find_all('a', limit=3):
            q.put(str(j.get('href')))
        q.join()
    # print q.get()
    # print q.get()
    # print q.get(), q.get(), q.get()
    for i in range(num_threads):
        worker = Thread(target=getOneExperience(q))
        worker.setDaemon(True)
        worker.start()




    soup = BeautifulSoup(str(br.response().read()))

    #extract the links and add it to the queue


# url = raw_input("enter url" )
# url = "http://www.geeksforgeeks.org/amazon-interview-experience-set-158-off-campus/" #set your own URL
path = "C:\\Users\\amukhopadhyay\\Desktop\\gfg.html" #set your own path
MY_LOCK = threading.Lock()
hitPage()


#all the places where the words DON'T WON'T etc are there, it's messing up that word a little
# getOneExperience(url, path)

