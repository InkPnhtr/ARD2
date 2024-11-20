import socket
import sys
import thread


listen_host = "127.0.0.1"
listen_port = 5555
listen_port1 = 5551
listen_port2 = 5552
listen_port3 = 5555

target_host = "127.0.0.1"
target_port = 5565

def main():
	thread.start_new_thread(server, () )
	lock = thread.allocate_lock()
	lock.acquire()
	lock.acquire()

def server(*settings):
	try:
		msg='frlyblubbtcp'

		dock_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#dock_socket.bind((listen_host, listen_port)) # listen

		dock_socket.connect((listen_host, listen_port)) # listen


		dock_socket.send(msg) # listen
		print 'FRLY: sent hs blubbtcp to:', listen_host, listen_port


		dock_socket.listen(5)
		dock_socket.settimeout(5)

		print "*** listening on %s:%i" % ( listen_host, listen_port )
		while True:
			client_socket, client_address = dock_socket.accept()
			client_socket.settimeout(5)


			print "*** from %s:%i to %s:%i" % ( client_address, listen_port, target_host, target_port )
			server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			server_socket.connect((target_host, target_port))

			server_socket.settimeout(5)


			thread.start_new_thread(forward, (client_socket, server_socket, "client -> server" ))
			thread.start_new_thread(forward, (server_socket, client_socket, "server -> client" ))
	finally:
		thread.start_new_thread(server, () )

def forward(source, destination, description):
	data = 'x'
	while data:
		try:
			foo= source.gettimeout()
			print'trying To=', foo

			data = source.recv(1024)
			print "*** %s: %s" % ( description, data )
			if data:
				destination.sendall(data)
			else:
				source.shutdown(socket.SHUT_RD)
				destination.shutdown(socket.SHUT_WR)
				print'Pass rcv!'
				print'data, addr' ,data, addr
		except socket.error, e:
			if isinstance(e.args, tuple):
				print "Nav Pipe  errno is :" , e[0]
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
			#print'Nav error eo data /Try w? '
			#data=None
			#acceptr()
			#break
			print'NavdataEow= ', data
			print'NavPipe done'

	print'NavdataOow= ', data
	#thread.exit()
	time.sleep(5)
	server()
	#thread.start_new_thread(server, ())
	thread.exit()

if __name__ == '__main__':
	main()
