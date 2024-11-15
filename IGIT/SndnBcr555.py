import socket
import sys
import thread
import time
from threading import Thread

secs=0
loopcount=0
#AppLstnHost = "192.168.43.1"
AppLstnHost = "127.0.0.1"
#AppLstnHost = "186.19.72.63"
AppTcpftpPrtLst = 5581
AppTcpCtrPrtLst = 5589
AppTcpVidRecPrtLst = 5583
AppTcpVidPrtLst = 5575
AppTcpAuthPrtLst = 5582
AppTcpPrnFPrtLst = 5588
AppTcpRwCapPrtLst = 5587
AppUdpCtrlPrtLst = 5584
AppUdpNavDtaPrtLst = 5586
AppUdpRwCapLst = 5587

#FlRlyTgtHost = "192.168.43.1"
#FlRlyTgtHost = "186.19.72.63"
FlRlyTgtHost = "127.0.0.1"
FlRlyTcpftpPrtTrgt = 5551
AppTcpCtrPrtTrgt = 5559
AppTcpVidRecPrtTrgt = 5553
FlRlyTcpVidPrtTrgt = 5575
FlRlyTcpAuthPrtTrgt = 5552
AppTcpPrnFPrtTrgt = 5558
AppTcpRwCapPrtTrgt = 5557
FlRlyUdpCtrlPrtTrgt = 5554
FlRlyUdpNavDtaPrtTrgt = 5556
AppUdpRwCapTrgt = 5557
I= 0
j=0
TcpSktLst= []
UdpSktLst= []
TgtTcpSkt= []
TgtUdpSkt= []

def main():
    thread.start_new_thread(server, () )
    lock = thread.allocate_lock()
    lock.acquire()
    lock.acquire()




def server(*settings):
    try:
	def TcpLsn(LstnHost, TcpPrtLst, TgtHost, TgtTcpPrt):
		global TcpSktLst
		global TgtTcpSkt

		global I
		print I


		TcpSktLst.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
		m='HELLO MICA!!!'
		TcpSktLst[I].bind((LstnHost, TcpPrtLst)) # listen
		TcpSktLst[I].listen(5)
		#TcpSktLst[I].connect((TgtHost, TgtTcpPrt)) # listen
		skt=TcpSktLst[I].getsockname()
		print'skt=',skt



#		TcpSktLst[I].connect((LstnHost, TcpPrtLst)) # listen
#		TcpSktLst[I].listen(5)
		#for f in range (0,1):	
		#	TcpSktLst[I].send((m)) # listen
	

		print "zzz*** listening tcp on %i %s:%i" % (I, LstnHost, TcpPrtLst )
#		TgtTcpSkt.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
#		TgtTcpSkt[I].connect((TgtHost, TgtTcpPrt))
		I = I+1

#	TcpLsn(AppLstnHost, AppTcpftpPrtLst, FlRlyTgtHost, FlRlyTcpftpPrtTrgt)

	TcpLsn(AppLstnHost, AppTcpVidPrtLst, FlRlyTgtHost, FlRlyTcpVidPrtTrgt)

#	TcpLsn(AppLstnHost, AppTcpAuthPrtLst, FlRlyTgtHost, FlRlyTcpAuthPrtTrgt)

	#TcpLsn(AppLstnHost, AppTcpVidRecPrtLst, FlRlyTgtHost, AppTcpVidRecPrtTrgt)

#	TcpLsn(AppLstnHost, AppTcpPrnFPrtLst, FlRlyTgtHost, AppTcpPrnFPrtTrgt)

	#TcpLsn(AppLstnHost, AppTcpRwCapPrtLst, FlRlyTgtHost, AppTcpRwCapPrtTrgt)

	def TcpFwd (TcpSktLsn):

		skt=TcpSktLsn.getsockname()
		print'skt=',skt
		TcpSktLstnAcceptr, TcpSktLstnAcceptrAddr= (TcpSktLsn.accept())
		#print "*** from %s:%i to %s:%i" % ( TcpSktLstnAcceptrAddr, TcpPtLst, TgtHost, TgtPrt )
		thread.start_new_thread(forward, (TcpSktLstnAcceptr, "TcpSktLstnAcceptr -> TgtTcpSkt" ))
#		thread.start_new_thread(forward, (TgtTcpSkt, TcpSktLstnAcceptr, "TgtTcpSkt -> TcpSktLstnAcceptr" ))



	for x in range(0, I):

		TcpFwd (TcpSktLst[x])
		#thread.start_new_thread(forward, (TcpSktLst[x], "TcpSktLstn -> TgtTcpSkt" ))
		print'x=', x

    finally:
#        thread.start_new_thread(server, () )
	print 'out'


def smsg ():
	TcpSktLst[I].send((m)) # snd

def forward(source, description):
	skt=source.getsockname()
	print'skt=',skt
	data = ' '
	while data:
		foo = None

		def check():
			while  foo  == None:
				time.sleep(5)
 				#if foo != None:
				print "Too Slow"
				source.send(("Too Sl00ow"))
				data = source.recv(1024)
				print "RcvdTCP:%s: %s" % ( description, data )


       			return
		
		Thread(target = check).start()

		#answer = raw_input("Input something: ")
		foo=raw_input('Please enter a value another?:')
		foox='Mica+'+str(foo)
		source.send((foox))
		data = source.recv(1024)
		print "RcvdTCP:%s: %s" % ( description, data )
	
	print'out of data loop!'

if __name__ == '__main__':
    main()
