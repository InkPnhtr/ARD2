import socket
import sys
import thread
import time

secs=0
loopcount=0
#AppLstnHost = "192.168.43.1"
AppLstnHost = "127.0.0.1"
AppTcpftpPrtLst = 5571
AppTcpCtrPrtLst = 5579
AppTcpVidRecPrtLst = 5573
AppTcpVidPrtLst = 5575
AppTcpAuthPrtLst = 5572
AppTcpPrnFPrtLst = 5578
AppTcpRwCapPrtLst = 5577
AppUdpCtrlPrtLst = 5574
AppUdpNavDtaPrtLst = 5576
AppUdpRwCapLst = 5577

#FlRlyTgtHost = "192.168.43.1"
FlRlyTgtHost = "127.0.0.1"
FlRlyTcpftpPrtTrgt = 5571
AppTcpCtrPrtTrgt = 5559
AppTcpVidRecPrtTrgt = 5553
FlRlyTcpVidPrtTrgt = 5575
FlRlyTcpAuthPrtTrgt = 5572
AppTcpPrnFPrtTrgt = 5558
AppTcpRwCapPrtTrgt = 5557
FlRlyUdpCtrlPrtTrgt = 5574
FlRlyUdpNavDtaPrtTrgt = 5576
AppUdpRwCapTrgt = 5577
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
		TcpSktLst[I].bind((LstnHost, TcpPrtLst)) # listen
		TcpSktLst[I].listen(5)
		print "*** listening tcp on %i %s:%i" % (I, LstnHost, TcpPrtLst )
#		TgtTcpSkt.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
		#TgtTcpSkt[I].connect((TgtHost, TgtTcpPrt))
		I = I+1

#	TcpLsn(AppLstnHost, AppTcpftpPrtLst, FlRlyTgtHost, FlRlyTcpftpPrtTrgt)

	TcpLsn(AppLstnHost, AppTcpVidPrtLst, FlRlyTgtHost, FlRlyTcpVidPrtTrgt)

#	TcpLsn(AppLstnHost, AppTcpAuthPrtLst, FlRlyTgtHost, FlRlyTcpAuthPrtTrgt)

#	TcpLsn(AppLstnHost, AppTcpVidRecPrtLst, FlRlyTgtHost, AppTcpVidRecPrtTrgt)

#	TcpLsn(AppLstnHost, AppTcpPrnFPrtLst, FlRlyTgtHost, AppTcpPrnFPrtTrgt)

	TcpLsn(AppLstnHost, AppTcpRwCapPrtLst, FlRlyTgtHost, AppTcpRwCapPrtTrgt)

	def UdpLsn(LstnHost, UdpPrtLst, TgtHost, TgtUdpPrt):
		global UdpSktLst
		global TgtUdpSkt
		global j
#		print j
		UdpSktLst.append(socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP))
		UdpSktLst[j].bind((LstnHost, UdpPrtLst)) # listen
		#AppUdpCtrlSktLst.listen(5)
		print "*** listening Udp on %i %s:%i" % (j, LstnHost, UdpPrtLst )
		TgtUdpSkt.append(TgtUdpPrt)
		#TgtUdpSkt[j].bind((TgtHost, TgtUdpPrt)) # listen
		print"To>>", TgtUdpSkt[j]
		j= j+1

#	UdpLsn(AppLstnHost, AppUdpCtrlPrtLst, FlRlyTgtHost, FlRlyUdpCtrlPrtTrgt)

#	UdpLsn(AppLstnHost, AppUdpNavDtaPrtLst, FlRlyTgtHost, FlRlyUdpNavDtaPrtTrgt)

#	UdpLsn(AppLstnHost, AppUdpRwCapLst, FlRlyTgtHost, AppUdpRwCapTrgt)

#	UdpLsn(AppLstnHost, AppUdpXPrtLst, FlRlyTgtHost, FlRlyUdpXPrtTrgt)



	def TcpFwd (TcpSktLsn):


		TcpSktLstnAcceptr, TcpSktLstnAcceptrAddr= (TcpSktLsn.accept())
		#print "*** from %s:%i to %s:%i" % ( TcpSktLstnAcceptrAddr, TcpPtLst, TgtHost, TgtPrt )
		thread.start_new_thread(forward, (TcpSktLstnAcceptr, "TcpSktLstnAcceptr -> TgtTcpSkt" ))
#		thread.start_new_thread(forward, (TgtTcpSkt, TcpSktLstnAcceptr, "TgtTcpSkt -> TcpSktLstnAcceptr" ))



	def UdpFd (UdpSktLsn, TgtUdpSkt):

		UdpFwd(UdpSktLsn, TgtUdpSkt)
		print 'fwd to:', TgtUdpSkt

#		thread.start_new_thread(UdpFwd(UdpSktLsn, TgtUdpSkt))
#	print'j=', j

	while True:
		for x in range(0, I):
			print x
			#tcptgpt=5571+x
			TcpFwd (TcpSktLst[x])
		for y in range(0, j):
			print "y=",y
			thread.start_new_thread(UdpFwd, (UdpSktLst[y], TgtUdpSkt[y]))
#			UdpFwd (UdpSktLst[y], TgtUdpSkt[y])

    finally:
        thread.start_new_thread(server, () )

def forward(source, description):
    data = ' '
    while data:
        data = source.recv(1024)
        print "fwdngTCP:%s: %s" % ( description, data )
        if data:
            source.sendall(data)
#        else:
#            source.shutdown(socket.SHUT_RD)
#            destination.shutdown(socket.SHUT_WR)

def UdpFwd (UdpCSktLst, FlRlyUdpX):
	data=' '
	print'hll', data
	knownClnt = None
	knownServer = (FlRlyTgtHost, FlRlyUdpX)
	sys.stderr.write('All settt.\n')     
	while data:

		data, addr = UdpCSktLst.recvfrom(1024)
		#datax, addr = sock.recvfrom(1024)
		print 'd,a=',data, addr
		if knownClnt is None:
			knownClnt = addr
# 		if addr == knownClnt:
#			UdpCSktLst.sendto(data, knownServer)
#			print'to tgt:',data, knownServer
#		else:
			UdpCSktLst.sendto(data, knownClnt)
			print'Boing',data, knownClnt


if __name__ == '__main__':
    main()