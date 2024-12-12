# Try to print Data and force UDP ADDR pairing



import socket
import threading

# Function to relay UDP data between two clients
def udp_relay(rudp_1, tgt):
    print(f"UDP Relay started for Pair OBID: {tgt}")
    try:
        print(f"Client a={rudp_1}")
        print(f"Client b={tgt}")


        while True:
            data1, addr1 = rudp_1.recvfrom(1024)
            # data2, addr2 = rudp_2.recvfrom(1024)

            print(f"RCVING: {data1} >>>>FROM: {addr1}")
            # if addr == client_a:
            print(f"About to Send: {data1} >>>>TO: {tgt}")
            rudp_1.sendto(data1, tgt)
            # elif addr == client_b:
            # print(f"About to Send: {data} >>>>TO: {client_a}")

            # udp_server.sendto(data, client_a)
    except Exception as e:
        print(f"UDP Relay for Pair ID {pair_id} terminated: {e}")

# Function to relay TCP data between two clients
def tcp_relay(client_a, client_b):
    print("TCP Relay started.")
    try:
        while True:
            data = client_a.recv(1024)
            if not data:
                break
            client_b.sendall(data)
    except Exception as e:
        print(f"TCP Relay error: {e}")
    finally:
        client_a.close()
        client_b.close()

# UDP Pairing Server
def udp_pairing_server(udp_server):
    print("UDP Pairing Server started on port 5554...")
    udp_clients = []
    pair_id = 0
    addrFix='127.0.0.1', 5556
    portFix= 5554
    addrFix1='127.0.0.1', 5556
    portFix1= 5554

    udp_clients.append(addrFix)
    udp_clients.append(addrFix1)
    print(f"udp_clients = {udp_clients[0]}")
    print(f"udp_clients = {udp_clients[1]}")
	
    while True:
        print(f"len udp_clients = {len(udp_clients)}")
        # data, addr = udp_server.recvfrom(1024)
        # print(f"Received data from {addr}: {data.decode()}")

        # if addr not in udp_clients:
        #     udp_clients.append(addr)

        if len(udp_clients) == 2:
            client_a, client_b = udp_clients
            print(f"Pairing UDP clients: {client_a} <-> {client_b}")

            # Start a relay thread for the pair
            threading.Thread(
                target=udp_relay,
                args=(udp_server, client_a, client_b, pair_id),
                daemon=True
            ).start()
            print("RLy THread Launched.... breaking  while loop ")
            break
            # Clear clients list for the next pair
            # udp_clients.clear()
            pair_id += 1

# TCP Pairing Server
def tcp_pairing_server(tcp_server):
    print("TCP Server started on port 5555...")

    while True:
        print("Waiting for TCP clients...")
        client_a, addr_a = tcp_server.accept()
        print(f"TCP client connected: {addr_a}")
        # client_b, addr_b = tcp_server.accept()
        # print(f"TCP client connected: {addr_b}")

        # Start relay threads for both directions
        threading.Thread(target=tcp_relay, args=(client_a, client_a), daemon=True).start()
        # threading.Thread(target=tcp_relay, args=(client_b, client_a), daemon=True).start()

# Main function to run both servers
if __name__ == "__main__":
    # Create the UDP server socket
    apddr = '127.0.0.1', 5554
    drddr = '192.168.1.1', 5554
    m = 'Hello form APRely'
    mb = m.encode()
    udp_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # udp_server.bind(('127.0.0.1', 5554))
    # udp_server.bind(('127.0.0.1', 5554))
    udp_1.bind((apddr))
    # udp_2.bind(('127.0.0.1', 5554))
    udp_2.sendto(mb, drddr) 

    # Create the TCP server socket
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind(('127.0.0.1', 5555))
    tcp_server.listen(5)  # Allow up to 5 pending connections

    try:
        # Run UDP and TCP servers in separate threads
        # threading.Thread(target=udp_pairing_server, args=(udp_server,), daemon=True).start()
        threading.Thread(target=udp_relay, args=(udp_1, drddr,), daemon=True).start()
        threading.Thread(target=udp_relay, args=(udp_2, apddr,), daemon=True).start()

        # tcp_pairing_server(tcp_server)
    except KeyboardInterrupt:
        print("Shutting down servers...")
    finally:
        udp_1.close()
        udp_2.close()

        tcp_server.close()


