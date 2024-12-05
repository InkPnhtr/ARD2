import socket
import threading

# UDP Relay function
def udp_relay(server_socket, client_a, client_b):
    print("UDP relay thread started.")
    while True:
        try:
            data, addr = server_socket.recvfrom(1024)
            if addr == client_a:
                print(f"Relaying UDP data from {addr} to {client_b}")
                server_socket.sendto(data, client_b)
            elif addr == client_b:
                print(f"Relaying UDP data from {addr} to {client_a}")
                server_socket.sendto(data, client_a)
        except Exception as e:
            print(f"UDP Relay Error: {e}")
            break

# TCP Relay function
def tcp_relay(client_socket, other_client_socket):
    print("TCP relay thread started.")
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Relaying TCP data to the other client.")
            other_client_socket.sendall(data)
    except Exception as e:
        print(f"TCP Relay Error: {e}")
    finally:
        client_socket.close()
        other_client_socket.close()

# Start the server
def start_relay_server():
    # UDP setup
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server.bind(('0.0.0.0', 12345))
    print("UDP server started on port 12345.")
    
    # TCP setup
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind(('0.0.0.0', 12346))
    tcp_server.listen(1)
    print("TCP server started on port 12346.")

    udp_clients = []

    try:
        while True:
            # Handle UDP pairing
            if len(udp_clients) < 2:
                print("Waiting for UDP clients...")
                data, addr = udp_server.recvfrom(1024)
                print(f"Received UDP data from {addr}")
                if addr not in udp_clients:
                    udp_clients.append(addr)
                    print(f"UDP client {addr} connected.")
                if len(udp_clients) == 2:
                    print(f"UDP clients paired: {udp_clients}")
                    threading.Thread(target=udp_relay, args=(udp_server, udp_clients[0], udp_clients[1]), daemon=True).start()

            # Handle TCP pairing
            print("Waiting for TCP clients...")
            client_a, addr_a = tcp_server.accept()
            print(f"TCP client connected: {addr_a}")
            client_b, addr_b = tcp_server.accept()
            print(f"TCP client connected: {addr_b}")

            threading.Thread(target=tcp_relay, args=(client_a, client_b), daemon=True).start()
            threading.Thread(target=tcp_relay, args=(client_b, client_a), daemon=True).start()
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        udp_server.close()
        tcp_server.close()

if __name__ == "__main__":
    start_relay_server()
