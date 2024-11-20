import socket
import sys
import thread
import time

secs=0
loopcount=0
#AppLstnHost = '100.111.206.102'
AppLstnHost = "127.0.0.1"
AppTcpftpPrtLst = 5561
AppTcpCtrPrtLst = 5569
AppTcpVidRecPrtLst = 5563
AppTcpVidPrtLst = 5565
AppTcpAuthPrtLst = 5562
AppTcpPrnFPrtLst = 5568
AppTcpRwCapPrtLst = 5567
AppUdpCtrlPrtLst = 5564
AppUdpNavDtaPrtLst = 5566
AppUdpRwCapLst = 5567

#FlRlyTgtHost = "192.168.43.5"
FlRlyTgtHost = "127.0.0.1"
FlRlyTcpftpPrtTrgt = 5561
AppTcpCtrPrtTrgt = 5569
AppTcpVidRecPrtTrgt = 5563
FlRlyTcpVidPrtTrgt = 5565
FlRlyTcpAuthPrtTrgt = 5562
AppTcpPrnFPrtTrgt = 5568
AppTcpRwCapPrtTrgt = 5567
FlRlyUdpCtrlPrtTrgt = 5564
FlRlyUdpNavDtaPrtTrgt = 5566
AppUdpRwCapTrgt = 5567
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
            TgtTcpSkt.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
            TgtTcpSkt[I].connect((TgtHost, TgtTcpPrt))
            I = I+1

        def UdpLsn(LstnHost, UdpPrtLst, TgtHost, TgtUdpPrt):
            global UdpSktLst
            global TgtUdpSkt
            global j
            print j
            UdpSktLst.append(socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP))
            UdpSktLst[j].bind((LstnHost, UdpPrtLst)) # listen
            #UdpSktLst[j].sendto((LstnHost, UdpPrtLst))
            #AppUdpCtrlSktLst.listen(5)
            print "*** listening Udp on %i %s:%i" % (j, LstnHost, UdpPrtLst )
            TgtUdpSkt.append(TgtUdpPrt)
            #TgtUdpSkt[j].bind((TgtHost, TgtUdpPrt)) # listen
            print 'tgt=', TgtUdpSkt[j]
            j= j+1

        UdpLsn(AppLstnHost, AppUdpCtrlPrtLst, FlRlyTgtHost, FlRlyUdpCtrlPrtTrgt)

        UdpLsn(AppLstnHost, AppUdpNavDtaPrtLst, FlRlyTgtHost, FlRlyUdpNavDtaPrtTrgt)

#	UdpLsn(AppLstnHost, AppUdpRwCapLst, FlRlyTgtHost, AppUdpRwCapTrgt)

#	UdpLsn(AppLstnHost, AppUdpXPrtLst, FlRlyTgtHost, FlRlyUdpXPrtTrgt)



        def TcpFwd (TcpSktLsn, TgtTcpSkt):


                TcpSktLstnAcceptr, TcpSktLstnAcceptrAddr= (TcpSktLsn.accept())
                #print "*** from %s:%i to %s:%i" % ( TcpSktLstnAcceptrAddr, TcpPtLst, TgtHost, TgtPrt )
                thread.start_new_thread(forward, (TcpSktLstnAcceptr, TgtTcpSkt, TcpSktLstnAcceptrAddr))
                thread.start_new_thread(forward, (TgtTcpSkt, TcpSktLstnAcceptr, "TgtTcpSkt -> TcpSktLstnAcceptr" ))



        def UdpFd (UdpSktLsn, TgtUdpSkt):

                UdpFwd(UdpSktLsn, TgtUdpSkt)
                print 'fwd to:', TgtUdpSkt

#		thread.start_new_thread(UdpFwd(UdpSktLsn, TgtUdpSkt))
        print'j=', j

#	while True:
        for x in range(0, I):
                print x
                #tcptgpt=5571+x
                #thread.start_new_thread(TcpFwd, (TcpSktLst[x], TgtTcpSkt[x]))
        for y in range(0, j):
                print "yloop=",y
                thread.start_new_thread(UdpFwd, (UdpSktLst[y], TgtUdpSkt[y]))
                #UdpFwd (UdpSktLst[y], TgtUdpSkt[y])

    finally:
        #thread.start_new_thread(server, () )
        print'end'

def forward(source, destination, description):
	data = ' '
	while data:
		data = source.recv(1024)
		print "fwdngTCP:%s: %s" % ( description, data )
		if data:
			destination.sendall(data)
#        else:
#            source.shutdown(socket.SHUT_RD)
#            destination.shutdown(socket.SHUT_WR)

def UdpFwd (UdpCSktLst, FlRlyUdpX):
	data=' '
	print'hll', data
	knownClnt = None
	flag=' '
	knownServer = (FlRlyTgtHost, FlRlyUdpX)
	sys.stderr.write('All settt.\n')     
	while data:

		data, addr = UdpCSktLst.recvfrom(1024)
		if data == 'blubb' :
			knownServer = (addr)
			print 'tgt/hs. knownServer=', knownServer
			#flag='blubb
		#datax, addr = sock.recvfrom(1024)
		print 'd,a=',data, addr
		if knownClnt is None and data != 'blubb':
			knownClnt = addr
		if addr == knownClnt or data == 'blubb': 
			UdpCSktLst.sendto(data, knownServer)
			print'to tgt:',data, knownServer
		else:
			UdpCSktLst.sendto(data, knownClnt)
			print'frmTgt',data, knownClnt


if __name__ == '__main__':
	main()
