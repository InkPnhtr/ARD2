import socket
import sys
import thread
import time

secs=0
loopcount=0
#AppLstnHost = "127.0.0.1"
#AppLstnHost = "192.168.43.238"
AppLstnHost = '186.19.244.182'
AppTcpftpPrtLst = 5581
AppTcpCtrPrtLst = 5589
AppTcpVidRecPrtLst = 5583
AppTcpVidPrtLst = 5585
AppTcpAuthPrtLst = 5582
AppTcpPrnFPrtLst = 5588
AppTcpRwCapPrtLst = 5587
AppUdpCtrlPrtLst = 5584
AppUdpNavDtaPrtLst = 5586
AppUdpRwCapLst = 5587

#FlRlyTgtHost = "186.19.72.63"
FlRlyTgtHost = '192.168.43.238'
#FlRlyTgtHost = "127.0.0.1"
FlRlyTcpftpPrtTrgt = 5551
AppTcpCtrPrtTrgt = 5559
AppTcpVidRecPrtTrgt = 5553
FlRlyTcpVidPrtTrgt = 5555
FlRlyTcpAuthPrtTrgt = 5552
AppTcpPrnFPrtTrgt = 5558
AppTcpRwCapPrtTrgt = 5557
FlRlyUdpCtrlPrtTrgt = 5554
FlRlyUdpNavDtaPrtTrgt = 5556
AppUdpRwCapTrgt = 5557
I= 0
j=0
tcpdata=' '
TcpSktLst= []
UdpSktLst= []
TgtTcpSkt= []
TgtUdpSkt= []

def main():
    server()
    lock = thread.allocate_lock()
    lock.acquire()
    lock.acquire()

def server(*settings):
#    try:
	def TcpLsn(LstnHost, TcpPrtLst, TgtHost, TgtTcpPrt):
		global TcpSktLst
		global TgtTcpSkt
		msg='frlyblubbtcp'
		global I
		print 'I=',I
		TcpSktLst.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
		TcpSktLst[I]. connect((LstnHost, TcpPrtLst)) # listen
		#TcpSktLst[I].listen(5)
		TcpSktLst[I].send(msg) # listen
		print 'FRLY: sent hs blubbtcp to:', LstnHost, TcpPrtLst
		#print "NOT sent hs blubbtcp to: %i %s:%i" % (I, LstnHost, TcpPrtLst )
		
		#TcpSktLst[I].listen(5)
		#print "*** listening tcp on %i %s:%i" % (I, LstnHost, TcpPrtLst )
		TgtTcpSkt.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
		TgtTcpSkt[I].connect((TgtHost, TgtTcpPrt))
		I = I+1

#	TcpLsn(AppLstnHost, AppTcpftpPrtLst, FlRlyTgtHost, FlRlyTcpftpPrtTrgt)

	TcpLsn(AppLstnHost, AppTcpVidPrtLst, FlRlyTgtHost, FlRlyTcpVidPrtTrgt)

#	TcpLsn(AppLstnHost, AppTcpAuthPrtLst, FlRlyTgtHost, FlRlyTcpAuthPrtTrgt)

#	TcpLsn(AppLstnHost, AppTcpVidRecPrtLst, FlRlyTgtHost, AppTcpVidRecPrtTrgt)

#	TcpLsn(AppLstnHost, AppTcpPrnFPrtLst, FlRlyTgtHost, AppTcpPrnFPrtTrgt)

#	TcpLsn(AppLstnHost, AppTcpRwCapPrtLst, FlRlyTgtHost, AppTcpRwCapPrtTrgt)


	def  datayy (sour, tgt):
		print'in datayy'

		datay=' '
		while datay:
			try:
				datay = sour.recv(1024)
				print'datay: ',datay
				tgt.sendall(datay)
			except socket.error, e:
				if isinstance(e.args, tuple):
					print "errno is %d" % e[0]
					if e[0] == errno.EPIPE:
						# remote peer disconnected
						print "Detected remote disconnect"

						#shutdown(socket.SHUT_RDWR)

						sour.shutdown(socket.SHUT_RDWR)
						#tgt.shutdown(socket.SHUT_RDWR)
						#TcpSktLst[x].shutdown(socket.SHUT_RDWR)
						#TgtTcpSkt[x].shutdown(socket.SHUT_RDWR)
						#time.sleep(10)
	
						break

						sour.close()
						#tgt.close()
						#TcpSktLst[x].close()
						#TgtTcpSkt[x].close()
						time.sleep(5)
						#server()
						#pass
						break
					else:
               					# determine and handle different error
						sour.shutdown(socket.SHUT_RDWR)
						sour.close()
               					#pass
						break
				else:
					print "socket error ", e
					sour.close()
					sour.shutdown(socket.SHUT_RDWR)
					break
    			except IOError, e:
				# Hmmm, Can IOError actually be raised by the socket module?
				print "Got IOError: ", e
				break			


	def  dataxx (sour, tgt):
		print'in dataxx'
				
		datax=' '
		c=0
		while datax:
			c=c+1
			print'Iter Nbr:',c
			try:
				datax = sour.recv(1024)
				print'datax: ',datax
				tgt.sendall(datax)
			except socket.error, e:
				if isinstance(e.args, tuple):
					print "datax errno is %d" % e[0]
					if e[0] == errno.EPIPE:
						# remote peer disconnected
						print "Detected remote disconnect"
						print'wtf'
						sour.shutdown(socket.SHUT_RDWR)
						#tgt.shutdown(socket.SHUT_RDWR)
						#TcpSktLst[x].shutdown(socket.SHUT_RDWR)
						#TgtTcpSkt[x].shutdown(socket.SHUT_RDWR)
						#time.sleep(5)
						sour.close()
						#tgt.close()
						#TcpSktLst[x].close()
						#TgtTcpSkt[x].close()
						#time.sleep(5)
						#server()
						#pass
						print'eif'
						break
					else:
               					# determine and handle different error
						#sour.shutdown(socket.SHUT_RDWR)
						sour.close()
						#tgt.close()
               					#pass
						break
				else:
					print "socket error ", e
					sour.close()
					tgt.close()
					#sour.shutdown(socket.SHUT_RDWR)
					print 'todo closedx'
					break
    			except IOError, e:
				# Hmmm, Can IOError actually be raised by the socket module?
				print "Got IOError: ", e
				break

		print'eow'
		acceptr()


	def acceptr ():
		print'bfloop'
		for x in range(0, I):

			print 'loop x=',x
			
			print'sourc=', TcpSktLst[x].getsockname()
			print'dest=', TgtTcpSkt[x].getsockname()
			
			TcpSktLstnAcceptr, TcpSktLstnAcceptrAddr = (TcpSktLst[x].accept())


			TcpSktTgttAcceptr, TcpSktTgttAcceptrAddr = (TgtTcpSkt[x].accept())

			thread.start_new_thread(datayy,(TcpSktTgttAcceptr, TcpSktLstnAcceptr))
			thread.start_new_thread(dataxx,(TcpSktLstnAcceptr, TcpSktTgttAcceptr))
			print'eol'

	acceptr()
		
	print'the end'

if __name__ == '__main__':
    main()
