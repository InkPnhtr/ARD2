#!/usr/bin/python

import thread
import time

# Define a function for the thread
def print_time():
   threadName='I'
   delay=1


   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )

# Create two threads as follows
try: 
   thread.start_new_thread( print_time, () )
   print't1 on'
   thread.start_new_thread( print_time, () )
   print't2 on'
except:
   print "Error: unable to start thread"

while 1:
   pass
