import socket
import sys
import thread
import time
from threading import Thread

secs=0
loopcount=0
#AppLstnHost = "192.168.43.1"
AppLstnHost = "127.0.0.1"
AppTcpftpPrtLst = 5551
AppTcpCtrPrtLst = 5559
AppTcpVidRecPrtLst = 5553
AppTcpVidPrtLst = 5555
AppTcpAuthPrtLst = 5552
AppTcpPrnFPrtLst = 5558
AppTcpRwCapPrtLst = 5557
AppUdpCtrlPrtLst = 5574
AppUdpNavDtaPrtLst = 5576
AppUdpRwCapLst = 5557

#FlRlyTgtHost = "192.168.43.1"
FlRlyTgtHost = "127.0.0.1"
FlRlyTcpftpPrtTrgt = 5551
AppTcpCtrPrtTrgt = 5559
AppTcpVidRecPrtTrgt = 5553
FlRlyTcpVidPrtTrgt = 5555
FlRlyTcpAuthPrtTrgt = 5552
AppTcpPrnFPrtTrgt = 5558
AppTcpRwCapPrtTrgt = 5557
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

        def UdpLsn(LstnHost, UdpPrtLst, TgtHost, TgtUdpPrt):
            global UdpSktLst
            global TgtUdpSkt
            global j
            print j
            UdpSktLst.append(socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP))
            UdpSktLst[j].bind((LstnHost, UdpPrtLst)) # listen
            #UdpSktLst[j].sendto(m,(TgtHost, TgtUdpPrt)) # listen
            #print'sent  m to:', TgtHost, TgtUdpPrt
            #AppUdpCtrlSktLst.listen(5)
            print "***DrnDmmy listening Udp on %i %s:%i" % (j, LstnHost, UdpPrtLst )
#       TgtUdpSkt.append(TgtUdpPrt)
            #TgtUdpSkt[j].bind((TgtHost, TgtUdpPrt)) # listen
#       print TgtUdpSkt[j]
            j= j+1

        UdpLsn(AppLstnHost, AppUdpCtrlPrtLst, FlRlyTgtHost, FlRlyUdpCtrlPrtTrgt)

        UdpLsn(AppLstnHost, AppUdpNavDtaPrtLst, FlRlyTgtHost, FlRlyUdpNavDtaPrtTrgt)

#   UdpLsn(AppLstnHost, AppUdpRwCapLst, FlRlyTgtHost, AppUdpRwCapTrgt)

#   UdpLsn(AppLstnHost, AppUdpXPrtLst, FlRlyTgtHost, FlRlyUdpXPrtTrgt)


        def UdpFd (UdpSktLsn, TgtUdpSkt):

            UdpFwd(UdpSktLsn, TgtUdpSkt)
            print 'fwd to:', TgtUdpSkt

#       thread.start_new_thread(UdpFwd(UdpSktLsn, TgtUdpSkt))
        print'j=', j

#   while True:
        for x in range(0, I):
            print x
            #tcptgpt=5571+x
            #TcpFwd (TcpSktLst[x])
        for y in range(0, j):
            print "y=",y
            thread.start_new_thread(UdpFwd,(UdpSktLst[y],))
            #UdpFwd (UdpSktLst[y])

    finally:
#        thread.start_new_thread(server, () )
            print 'out'

def UdpFwd (UdpCSktLst):
	data=' '

	data, addr = UdpCSktLst.recvfrom(1024)
	m='HloFrmUDPTX2019'
	print'Rcvd:', data
	UdpCSktLst.sendto(m,(addr)) # send m
	print'sent  m to:', addr
	print'Rcvd:', data
	data=' '
#   print'hxll', data
#   knownClnt = None
#   knownServer = (FlRlyTgtHost, FlRlyUdpX)
	sys.stderr.write('UdpFwd')     
	while data:
		print'in'
		foo = None

		def check():
			while  foo  == None:
				time.sleep(1)
				#if foo != None:
				print "Too Slow"
				UdpCSktLst.sendto("Too Sl00ow",(addr)) # send m
				#source.send(("Too Sl00ow"))
				data = UdpCSktLst.recvfrom(1024)
				print "RcvdUDP:%s: %s" % ( addr, data )


				return
		
		Thread(target = check).start()

		#answer = raw_input("Input something: ")
		#foo=raw_input('Please enter a value another?:')
		foo=('SUPALEX')
		foox='Mica+'+str(foo)

		#source.send((foox))

		UdpCSktLst.sendto(foox,(addr)) # send m

		data, addr = UdpCSktLst.recvfrom(1024)
		#datax, addr = sock.recvfrom(1024)
		print 'd,aRx=',data, addr
		#UdpCSktLst.sendto('Ack', addr)
#           
	print'bye'
#       if knownClnt is None:
#           knownClnt = addr
#       if addr == knownClnt:
#           UdpCSktLst.sendto(data, knownServer)
#           print'to tgt:',data, knownServer
#       else:
#           UdpCSktLst.sendto(data, knownClnt)
#           print'frmTgt',data, knownClnt


if __name__ == '__main__':
	main()
