import socket
import sys
import thread
import errno
import time
#global client_socketAcceptr
global client_socketAcceptr, client_sockeAcceptrAddr


#listen_host = "127.0.0.1"
dr = "192.168.0.4"

dr_port = 5555
listen_port1 = 5551
listen_port2 = 5552
listen_port3 = 5585

#target_host = "127.0.0.1"
aprly = "192.168.0.4"

aprly_port = 5585

i=0
t1=0
t2=0
s=0

def main():
	cnt()
	#thread.start_new_thread(server, () )
	server ()
	lock = thread.allocate_lock()
	lock.acquire()
	lock.acquire()

def cnt():

	global t1
	global client_socketAcceptr, client_sockeAcceptrAddr





	print'i=',i

	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	client_socket.bind((listen_host, listen_port)) # listen
	client_socket.listen(55)
	#client_socket.connect((listen_host, listen_port)) # listen


	#client_socket.send(msg) # listen
	print 'cntArly: listening on:', listen_host, listen_port


	#client_socket.listen(5)
	#client_socket.settimeout(20)

	#print "*** listening on %s:%i" % ( listen_host, listen_port )
	#while True:
	#client_socket, client_address = dock_socket.accept()
	#client_socket.settimeout(15)


	#print "*** from %s:%i to %s:%i" % ( client_address, listen_port, target_host, target_port )
	client_socketAcceptr, client_sockeAcceptrAddr= client_socket.accept()
	print' cnt_client_sockeAcceptrAddr=',  client_sockeAcceptrAddr
	#csn=client_socketAcceptr. getsocketname()
	#print'csn',csn



def server(*settings):
	global i
	global s
	global t1
	global t2
	global server_socket

	global server_socketAcceptr, server_socketAcceptrAddr

	try:
		#if i>0:
		#	server_socket.close ()
		msg='frlyblubbtcp'

		aprly_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		aprly_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		aprly_socket. connect((aprly, aprly_port)) # listen
		aprly_socket.listen(55)
		print 'serverArly:  hsng on:', target_host, target_port

		#aprly_socket.connect((target_host, target_port))

		aprly_socket.settimeout(25)
		#aprly_socket.send(msg) # listen
		print'i=',i

		#if i>1:
		print  'server-server socket', repr(aprly_socket)
		#print 'server socket', server_socket

		aprly_socketAcceptr, server_socketAcceptrAddr= server_socket.accept()
		aprly_socketAcceptr.settimeout(25)
		print' server-server_socketAcceptrAddr=',  server_socketAcceptrAddr
		print' cnt_client_sockeAcceptrAddr=',  client_sockeAcceptrAddr

		t1=t1+1
		print'aprly-thread clntA to serverD',t1
		#csn=client_socketAcceptr. getsocketname()
		#print't1CtS csn=',csn
		thread.start_new_thread(forwardAtFr, (client_socketAcceptr, server_socketAcceptr, "client -> server" ))
		t2=t2+1
		print'serverthread server to client', t2
		#csn=client_socketAcceptr. getsocketname()
		#print't2StC csn=',csn
		thread.start_new_thread(forwardFrtA, (server_socketAcceptr, client_socketAcceptr, "server -> client" ))

	except socket.error, e:
		if isinstance(e.args, tuple):
			print "SERVER Pipe  errno is :" , e
			if e[0] == errno.EPIPE:
				# remote peer disconnected
				print "serverDetected remote disconnect"
				print'SRVR wtf'
				print'servereif'
				#client_socket.close()
				#server_socket.close()


				#break
			else:
				print'serverr!!! X Errorr re-lunch s=',s
				#client_socket.close()
				#server_socket.shutdown(socket.SHUT_RDWR)
				m1='sty alv'
				server_socket.shutdown(socket.SHUT_RDWR)
				server_socket.close()
				time.sleep(15)
				client_socketAcceptr.sendall(m1)

				server()
				# determine and handle different error
				#sour.shutdown(socket.SHUT_RDWR)
				#sour.close()
				#tgt.close()
				#pass
				#break
		else:
			print "serversocket error ", e
			#sour.close()
			#tgt.close()
			#sour.shutdown(socket.SHUT_RDWR)
			print 'serversock errr closedx'
			#break
	except IOError, e:
		# Hmmm, Can IOError actually be raised by the socket module?
		print "serverGot IOError: ", e
		#break
		#print'Nav error eo data /Try w? '
		#data=None
		#acceptr()
		#break
		print'serverServdataEow= ', data
		print'serverSrrvPipe done'


	#finally:
	m1='sty alv'
	i=i+1
		#csn=client_socketAcceptr. getsockname()
		#print't1CtS csn=',csn
		#client_socketAcceptr.sendall(m1)

	print'serverfinally',i
	#server_socket.close()
	#time.sleep(5)
	#server()

		#thread.start_new_thread(server, () )

def forwardAtFr(source, destination, description):
	#source.settimeout(10)
	#destination.settimeout(20)


	global s
	data = 'x'
	#print 'source', source
	#print'destination', destination
	print'AtFrdescription', description
	
	s=s+1
	while data:
		try:
			m1='AtFrsty alv'
			#source.sendall(m1)
			#destination.sendall(m1)
			foo= source.gettimeout()
			print'AtFrtrying To=', foo
			print'AtFrrcv 1024 block', description
			data = source.recv(1024)
			print "AtFr*** %s: %s" % ( description, data )
			#destination.sendall(data)
			if data:
				destination.sendall(data)
			else:
				source.sendall(m1)
				#destination.sendall(m1)
				#ssn=source.getsocketname()
				#dsn=destination.getsocketname()
				#print'ssn',ssn
				#print'dsn',dsn

				print'AtFrVp_ood!', data
				#source.shutdown(socket.SHUT_RD)
				#destination.shutdown(socket.SHUT_WR)
				#print'Pass rcv!'
				#print'data', data
		except socket.error, e:
			if isinstance(e.args, tuple):
				print "AtFrNav Pipe  errno is :" , e
				if e[0] == errno.EPIPE:
					# remote peer disconnected
					print "AtFrDetected remote disconnect"
					print'AtFrwtf'
					print'AtFreif'
					destination.shutdown(socket.SHUT_RDWR)
					server_socket.shutdown(socket.SHUT_RDWR)

					destination.close()
					server_socket.close()
					time.sleep(15)

					#server ()
					break
				else:
					print'AtFrsome err re-lunch s=',s
					# determine and handle different error
					#source.close()
					#server_socketAcceptr.close()
					destination.shutdown(socket.SHUT_RDWR)
					server_socket.shutdown(socket.SHUT_RDWR)

					destination.close()
					server_socket.close()
					#destination.close()
					#source.shutdown(socket.SHUT_RDWR)
					#destination.shutdown(socket.SHUT_RDWR)
					time.sleep(15)
					#server()

					#pass
					break
			else:
				print "AtFrsocket error ", e
				#sour.close()
				#tgt.close()
				#sour.shutdown(socket.SHUT_RDWR)
				print 'AtFrsock errr closedx'
				#break
		except IOError, e:
			# Hmmm, Can IOError actually be raised by the socket module?
			print "AtFrGot IOError: ", e
			#break
			#print'Nav error eo data /Try w? '
			#data=None
			#acceptr()
			#break
			print'AtFrNavdataEow= ', data
			print'AtFrNavPipe done'

	print'AtFrNavdataOow=? '
	
	#server_socketAcceptr.close()

	#thread.exit()
	#time.sleep(5)
	server()
	#thread.start_new_thread(server, ())
	#thread.exit()

def forwardFrtA(source, destination, description):
	#source.settimeout(20)
	#destination.settimeout(10)


	global s
	data = 'x'
	#print 'source', source
	#print'destination', destination
	print'FrtAdescription', description
	
	s=s+1
	while data:
		try:
			m1='FrtAsty alv'
			#source.sendall(m1)
			#destination.sendall(m1)
			foo= source.gettimeout()
			print'FrtAtrying To=', foo
			print'FrtArcv 1024 block', description
			data = source.recv(1024)
			print "FrtA*** %s: %s" % ( description, data )
			#destination.sendall(data)
			if data:
				destination.sendall(data)
			else:
				#source.sendall(m1)
				destination.sendall(m1)
				#ssn=source.getsocketname()
				#dsn=destination.getsocketname()
				#print'ssn',ssn
				#print'dsn',dsn

				print'FrtAVp_ood!', data
				#source.shutdown(socket.SHUT_RD)
				#destination.shutdown(socket.SHUT_WR)
				#print'Pass rcv!'
				#print'data', data
		except socket.error, e:
			if isinstance(e.args, tuple):
				print "FrtANav Pipe  errno is :" , e
				if e[0] == errno.EPIPE:
					# remote peer disconnected
					print "FrtADetected remote disconnect"
					print'FrtAwtf'
					print'FrtAeif'
					#server ()
					source.shutdown(socket.SHUT_RDWR)
					server_socket.shutdown(socket.SHUT_RDWR)

					source.close()
					server_socket.close()
					time.sleep(15)


					break
				else:
					print'FrtAsome err re-lunch s=',s
					# determine and handle different error
					#server_socketAcceptr.close()
					#source.shutdown(socket.SHUT_RDWR)
					server_socket.shutdown(socket.SHUT_RDWR)

					source.close()
					server_socket.close()

					#destination.close()
					#source.shutdown(socket.SHUT_RDWR)
					#destination.shutdown(socket.SHUT_RDWR)
					time.sleep(15)


					#server()

					#pass
					break
			else:
				print "FrtAsocket error ", e
				#sour.close()
				#tgt.close()
				#sour.shutdown(socket.SHUT_RDWR)
				print 'FrtAsock errr closedx'
				#break
		except IOError, e:
			# Hmmm, Can IOError actually be raised by the socket module?
			print "FrtAGot IOError: ", e
			#break
			#print'Nav error eo data /Try w? '
			#data=None
			#acceptr()
			#break
			print'FrtANavdataEow= ', data
			print'FrtANavPipe done'

	print'FrtANavdataOow=??? '
	#server_socketAcceptr.close()

	#thread.exit()
	#time.sleep(5)
	server()
	#thread.start_new_thread(server, ())
	#thread.exit()


if __name__ == '__main__':
	main()
