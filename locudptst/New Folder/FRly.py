import socket
import sys
import thread
import time
from threading import Thread
import errno

secs=0
loopcount=0
#AppRlyHost = '186.19.244.182'
AppRlyHost = "127.0.0.1"

NavRcvPrt = 5564
CtrlRcvPrt = 5566
RwVidCapRcvPrt = 5557

#DrnHost = "192.168.43.238"
DrnHost = "127.0.0.1"

NavSndPrt = 5574
CtrlSndPrt = 5576
RwVidCapSndPrt = 5557

I= 0
j=0

#NavRcvrSkt= ''
#NavSndrSkt= ''

#CtrRcvrSkt= ''
#CtrSndrSkt= ''
NavRcvrSkt=(socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP))
NavSndrSkt=(socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP))

CtrRcvrSkt=(socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP))
CtrSndrSkt=(socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP))


def main():
	#thread.start_new_thread(server, () )
	server()
	print 'server Call'
	#lock = thread.allocate_lock()
	#lock.acquire()
	#lock.acquire()

def server(*settings):
	try:

		print 'in server'
		NavRcvrSkt.sendto('blubb',(AppRlyHost, NavRcvPrt))
		NavSndrSkt.sendto('blubb',(DrnHost, NavSndPrt))

		CtrRcvrSkt.sendto('blubb',(AppRlyHost, CtrlRcvPrt))
		CtrSndrSkt.sendto('blubb',(DrnHost, CtrlSndPrt))


		NavRcvrSktNm=NavRcvrSkt.getsockname()
		NavSndrSktNm=NavSndrSkt.getsockname()

		CtrRcvrSktNm=CtrRcvrSkt.getsockname()
		CtrSndrSktNm=CtrSndrSkt.getsockname()



		print'NavRcvrSktNm: ', NavRcvrSktNm
		print'NavSndrSktNm: ', NavSndrSktNm

		print'CtrRcvrSktNm: ', CtrRcvrSktNm
		print'CtrSndrSktNm: ', CtrSndrSktNm


		#thread.start_new_thread( print_time, () )

		thread.start_new_thread(NavPipe,())
		print 'NavPipe Called'
		#thread.start_new_thread(CtrlPipe(CtrRcvrSkt, CtrSndrSkt,))
		print'CtrlPipe Called'


	finally:
		#thread.start_new_thread(server, () )
		print'end'
		#end



def check():
	i=0
	print'watch'
	while  data  == None and i<1:
		print'no data!'
		time.sleep(1)
			
		print "Udp T Ou"
		i=i+1
	print 'known server=', knownServer
	UdpCSktLst.sendto('blubb',(knownServer))
	print'... blubb'




def  NavPipe():


	data=' 1'
	print'Navdata= ', data
	AppSkt = None
	Drn = (DrnHost, NavSndPrt)
	sys.stderr.write('All settt Nav?...\n')

	while data:
		#foo = None


		#Thread(target = check).start()
		#data=None

		try:
			data, addr = NavRcvrSkt.recvfrom(1024)
			print'Pass rcv!'
			print'data, addr' ,data, addr
			if AppSkt is None:
				AppSkt = addr
			if addr == AppSkt:
				NavSndrSkt.sendto(data,Drn)
				print'Nav To Drn:',data, Drn
			else:
				NavRcvrSkt.sendto(data, AppSkt)
				print'Nav To AppRly:',data, AppSkt


		except socket.error, e:
			if isinstance(e.args, tuple):
				print "Nav Pipe  errno is %d" % e[0]
				if e[0] == errno.EPIPE:
					# remote peer disconnected
					print "Detected remote disconnect"
					print'wtf'
					print'eif'
					break
				else:
					print'err'
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
		#data=None
		#acceptr()
	print'done'



	
def  CtrlPipe():


	data=' '
	print'Ctrldata= ', data
	AppSkt = None
	Drn = (DrnHost, CtrlSndPrt)
	sys.stderr.write('All settt Ctrl?...\n')
	     
	while data:
		#foo = None

		
		
		#Thread(target = check).start()
		#data=None
		
		try:
			data, addr = AppRlySkt.recvfrom(1024)
			if AppSkt is None:
				AppSkt = addr
			if addr == AppSkt:
				DrnSkt.sendto(data,Drn)
				print'Ctr To Drn:',data, Drn
			else:
				AppRlySkt.sendto(data, AppSkt)
				print'Ctr To AppRly:',data, AppSkt

	
		except socket.error, e:
			if isinstance(e.args, tuple):
				print "Ctrl Pipe  errno is %d" % e[0]
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
		#data=None

	print'CTR done'



if __name__ == '__main__':
    main()
