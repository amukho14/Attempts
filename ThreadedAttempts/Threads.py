__author__ = 'amukhopadhyay'

import threading
import time



class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        print_time(self.name, self.counter, 7)
        print "Exiting " + self.name

def print_time(threadName, delay, counter):
    global exitFlag
    print threadName, delay, counter, exitFlag


    while counter:
        if counter == 5:
            print "counter for", threadName, " = 5 so setting exitFlag"
            exitFlag = 1
        if exitFlag:
            return
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time())), "\n"
        counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
exitFlag = 0
# Start new Threads
thread1.start()
thread2.start()

print "Exiting Main Thread"
