import socket
import sys
import thread
import time
import errno

secs=0
loopcount=0
#AppLstnHost = "192.168.0.13"
#AppLstnHost = "192.168.43.238"
AppLstnHost = "127.0.0.1"
AppTcpftpPrtLst = 5551
AppTcpCtrPrtLst = 5559
AppTcpVidRecPrtLst = 5553
AppTcpVidPrtLst = 5555
AppTcpAuthPrtLst = 5552
AppTcpPrnFPrtLst = 5558
AppTcpRwCapPrtLst = 5557
AppUdpCtrlPrtLst = 5554
AppUdpNavDtaPrtLst = 5556
AppUdpRwCapLst = 5557

#FlRlyTgtHost = "192.168.0.13"
#FlRlyTgtHost = "192.168.43.238"
FlRlyTgtHost = "127.0.0.1"
FlRlyTcpftpPrtTrgt = 5581
AppTcpCtrPrtTrgt = 5589
AppTcpVidRecPrtTrgt = 5583
FlRlyTcpVidPrtTrgt = 5585
FlRlyTcpAuthPrtTrgt = 5582
AppTcpPrnFPrtTrgt = 5588
AppTcpRwCapPrtTrgt = 5587
FlRlyUdpCtrlPrtTrgt = 5584
FlRlyUdpNavDtaPrtTrgt = 5586
AppUdpRwCapTrgt = 5587
I= 0
j=0
tcpdata=' '
TcpSktLst= []
UdpSktLst= []
TgtTcpSkt= []
TgtUdpSkt= []
#TcpSktLstnAcceptr=[]
#TcpSktTgttAcceptr=[]
#TcpSktLstnAcceptrAddr=[]
#TcpSktTgttAcceptrAddr=[]

def main():
    server()
#    thread.start_new_thread(server, () )
    lock = thread.allocate_lock()
    lock.acquire()
    lock.acquire()

def server(*settings):
#    try:
	def TcpLsn(LstnHost, TcpPrtLst, TgtHost, TgtTcpPrt):
		global TcpSktLst
		global TgtTcpSkt
		msg='blubbtcp'
		global I
		print 'I=',I
		TcpSktLst.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
		TcpSktLst[I].setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		#TcpSktLst[I].setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT,)
		TcpSktLst[I].settimeout(555)
		TcpSktLst[I].bind((LstnHost, TcpPrtLst)) # listen
		TcpSktLst[I].listen(5)
		print "ARLY> listening tcp on %i %s:%i" % (I, LstnHost, TcpPrtLst )
		
		#TcpSktLst[I].send(msg) # listen
		#print 'sent hs blubbtcp to:', LstnHost, TcpPrtLst
		#print "NOT sent hs blubbtcp to: %i %s:%i" % (I, LstnHost, TcpPrtLst )
		
		#TcpSktLst[I].listen(5)
		TgtTcpSkt.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
		TgtTcpSkt[I].setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		TgtTcpSkt[I].settimeout(555)
		TgtTcpSkt[I].bind((TgtHost, TgtTcpPrt))
		TgtTcpSkt[I].listen(5)
		print "ARLY*** listening tcp on %i %s:%i" % (I, TgtHost, TgtTcpPrt )
		
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
	


						sour.close()
						#tgt.close()
						#TcpSktLst[x].close()
						#TgtTcpSkt[x].close()
						time.sleep(5)
						#server()
						#pass

					else:
               					# determine and handle different error
						sour.shutdown(socket.SHUT_RDWR)
						sour.close()
               					#pass
				else:
					print "socket error ", e
					sour.close()
					sour.shutdown(socket.SHUT_RDWR)
				#break
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
