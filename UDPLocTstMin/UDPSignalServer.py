import socket

def start_signaling_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('0.0.0.0', 12345))
    print("Signaling server started on port 12345...")

    clients = []
    
    while True:
        data, addr = server.recvfrom(1024)
        print(f"Received {data} from {addr}")

        if addr not in clients:
            clients.append(addr)
        
        if len(clients) == 2:
            print("Sending peer information to clients...")
            # Send Client A's info to Client B
            server.sendto(f"{clients[1][0]}:{clients[1][1]}".encode(), clients[0])
            # Send Client B's info to Client A
            server.sendto(f"{clients[0][0]}:{clients[0][1]}".encode(), clients[1])
            clients.clear()

if __name__ == "__main__":
    start_signaling_server()
