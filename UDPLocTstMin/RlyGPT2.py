import socket
import threading

def udp_relay(client_a, client_b, pair_id):
    """Relay data between two UDP clients."""
    print(f"Relay started for Pair ID: {pair_id}")
    try:
        while True:
            # Relay Client A -> Client B
            data, addr = udp_server.recvfrom(1024)
            if addr == client_a:
                udp_server.sendto(data, client_b)
            # Relay Client B -> Client A
            elif addr == client_b:
                udp_server.sendto(data, client_a)
    except Exception as e:
        print(f"Relay thread for Pair ID {pair_id} terminated: {e}")

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



def udp_pairing_server():
    """Main server to pair and relay UDP clients."""
    global udp_pairs, udp_pair_id

    print("UDP Pairing Server started on port 12345...")
    udp_clients = []

    while True:
        data, addr = udp_server.recvfrom(1024)
        print(f"Received data from {addr}: {data.decode()}")

        if addr not in udp_clients:
            udp_clients.append(addr)
        
        if len(udp_clients) == 2:
            client_a, client_b = udp_clients
            print(f"Pairing clients: {client_a} <-> {client_b}")
            
            # Assign a unique pair ID
            udp_pairs[udp_pair_id] = (client_a, client_b)

            # Start a relay thread for the pair
            threading.Thread(
                target=udp_relay, 
                args=(client_a, client_b, udp_pair_id), 
                daemon=True
            ).start()
            
            # Clear clients list for the next pair
            udp_clients.clear()
            udp_pair_id += 1

        # Handle TCP pairing
        print("Waiting for TCP clients...")
        client_a, addr_a = tcp_server.accept()
        print(f"TCP client connected: {addr_a}")
        client_b, addr_b = tcp_server.accept()
        print(f"TCP client connected: {addr_b}")

        threading.Thread(target=tcp_relay, args=(client_a, client_b), daemon=True).start()
        threading.Thread(target=tcp_relay, args=(client_b, client_a), daemon=True).start()


if __name__ == "__main__":
    # Global variables to manage UDP pairs
    udp_pairs = {}
    udp_pair_id = 0

    # Create the UDP server socket
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server.bind(('127.0.0.1', 12345))

    # TCP setup
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind(('127.0.0.1', 12346))
    tcp_server.listen(1)
    print("TCP server started on port 12346.")


    try:
        udp_pairing_server()
    except KeyboardInterrupt:
        print("Shutting down server...")
    finally:
        udp_server.close()
        tcp_server.close()

