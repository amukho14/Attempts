__author__ = 'amukhopadhyay'

import threading

TOTAL = 0
MY_LOCK = threading.Lock()


class CountThread(threading.Thread):
    def run(self):
        global TOTAL
        path = "C:\\Users\\amukhopadhyay\\Desktop\\threadFile.txt"
        for i in range(1000):
            MY_LOCK.acquire()
            with open(path, 'w') as f:
                f.write(str(TOTAL) +'\n')
                TOTAL+=1
                f.close()
            MY_LOCK.release()
        print('%s\n' % (TOTAL))

a = CountThread()
b = CountThread()
c = CountThread()
a.start()
b.start()
c.start()
# c.start()
# b.start()