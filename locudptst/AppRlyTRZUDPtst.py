import socket
import sys
import thread
import time

secs=0
loopcount=0
AppLstnHost = '192.168.0.13'
#AppLstnHost = "127.0.0.1"
AppTcpftpPrtLst = 5561
AppTcpCtrPrtLst = 5569
AppTcpVidRecPrtLst = 5563
AppTcpVidPrtLst = 5555
AppTcpAuthPrtLst = 5562
AppTcpPrnFPrtLst = 5568
AppTcpRwCapPrtLst = 5567
AppUdpCtrlPrtLst = 5554
AppUdpNavDtaPrtLst = 5556
AppUdpRwCapLst = 5557

FlRlyTgtHost = "192.168.0.13"
#FlRlyTgtHost = "127.0.0.1"
FlRlyTcpftpPrtTrgt = 5561
AppTcpCtrPrtTrgt = 5569
AppTcpVidRecPrtTrgt = 5563
FlRlyTcpVidPrtTrgt = 5565
FlRlyTcpAuthPrtTrgt = 5562
AppTcpPrnFPrtTrgt = 5568
AppTcpRwCapPrtTrgt = 5567
FlRlyUdpCtrlPrtTrgt = 5554
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
		#TgtUdpSkt.append(TgtUdpPrt)
		TgtUdpSkt.append(socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP))
				
		#TgtUdpSkt[j].bind((TgtHost, TgtUdpPrt)) # listen
		print 'tgt=', TgtUdpSkt[j]
		j= j+1

	UdpLsn(AppLstnHost, AppUdpCtrlPrtLst, FlRlyTgtHost, FlRlyUdpCtrlPrtTrgt)

	UdpLsn(AppLstnHost, AppUdpNavDtaPrtLst, FlRlyTgtHost, FlRlyUdpNavDtaPrtTrgt)

	#UdpLsn(AppLstnHost, AppUdpRwCapLst, FlRlyTgtHost, AppUdpRwCapTrgt)

#	UdpLsn(AppLstnHost, AppUdpXPrtLst, FlRlyTgtHost, FlRlyUdpXPrtTrgt)




	def UdpFd (UdpSktLsn, TgtUdpSkt):

		UdpFwd(UdpSktLsn, TgtUdpSkt)
		print 'fwd to:', TgtUdpSkt

#		thread.start_new_thread(UdpFwd(UdpSktLsn, TgtUdpSkt))
	print'j=', j

#	while True:
	for y in range(0, j):
		print "yloop=",y
		thread.start_new_thread(UdpFwd, (UdpSktLst[y], TgtUdpSkt[y]))
		#UdpFwd (UdpSktLst[y], TgtUdpSkt[y])

    finally:
        #thread.start_new_thread(server, () )
	print'end'


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



	def check():
		i=0
		print'watch'
		while  data  == None and i<10:
			print'no data!'
			time.sleep(1)
 			
			print "Udp T Ou"
			i=i+1
		print 'known server=', knownServer
		UdpCSktLst.sendto('blubb',(knownServer))
		print'... blubb'
		#UdpCSktLst.close()
		#print'UdpCSktLst closed'

		#server()
		#UdpLsn(AppLstnHost, AppUdpCtrlPrtLst, FlRlyTgtHost, FlRlyUdpCtrlPrtTrgt)

		#UdpLsn(AppLstnHost, AppUdpNavDtaPrtLst, FlRlyTgtHost, FlRlyUdpNavDtaPrtTrgt)
	
       		return

	data=' '
	print'hll', data
	knownClnt = None
	knownServer = (FlRlyTgtHost, FlRlyUdpX)
	sys.stderr.write('All settt.\n')
	     
	while data:
	#foo = None

		
		
		Thread(target = check).start()
		data=None
		
		try:
			data, addr = UdpCSktLst.recvfrom(1024)
			if knownClnt is None:
				knownClnt = addr
 			if addr == knownClnt:
				UdpCSktLst.sendto(data, knownServer)
				print'to tgt:',data, knownServer
			else:
				UdpCSktLst.sendto(data, knownClnt)
				print'frmTgt',data, knownClnt



		except socket.error, e:
			if isinstance(e.args, tuple):
				print "datax errno is %d" % e[0]
				if e[0] == errno.EPIPE:
					# remote peer disconnected
					print "Detected remote disconnect"
					print'wtf'
					print'eif'
					break
				else:
               				# determine and handle different error
					#sour.shutdown(socket.SHUT_RDWR)
					#sour.close()
					#tgt.close()
               				#pass
					break
			else:
				print "socket error ", e
				#sour.close()
				#tgt.close()
				#sour.shutdown(socket.SHUT_RDWR)
				print 'sock errr closedx'
				break
    		except IOError, e:
			# Hmmm, Can IOError actually be raised by the socket module?
			print "Got IOError: ", e
			break

	print'error eo Try w '
	#acceptr()

