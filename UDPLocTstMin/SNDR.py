# Try to print Data and force UDP ADDR pairing

import socket
import threading

# Function to relay UDP data between two clients
def udp_relay(rudp_1, tgt):
    print(f"UDP Relay started for Pair OBID: {tgt}")
    try:
        print(f"Client a={rudp_1}")
        print(f"Client b={tgt}")
        I=0


        while (I<10):
            data1, addr1 = rudp_1.recvfrom(1024)
            # data2, addr2 = rudp_2.recvfrom(1024)

            print(f"RCVING:{I} >>>>FROM: ")
            # if addr == client_a:
            print(f"About to Send:  >>>>TO: {tgt}")
            #rudp_1.sendto(data1, tgt)
            # elif addr == client_b:
            # print(f"About to Send: {data} >>>>TO: {client_a}")

            # udp_server.sendto(data, client_a)
            I+=1
    except Exception as e:
        print(f"UDP Relay for Pair ID {I} terminated: {e}")


# Main function to run both servers
if __name__ == "__main__":
    # Create the UDP server socket
    apddr = '127.0.0.1', 5564
    # drddr = '192.168.1.1', 5554
    drddr = '127.0.0.1', 5574

    m = 'Hello form APRely'
    mb = m.encode()
    udp_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # udp_server.bind(('127.0.0.1', 5554))
    # udp_server.bind(('127.0.0.1', 5554))
    # udp_1.bind((apddr))
    # udp_2.bind(('127.0.0.1', 5554))
    udp_2.sendto(mb, drddr) 

    try:
        # Run UDP and TCP servers in separate threads
        # threading.Thread(target=udp_pairing_server, args=(udp_server,), daemon=True).start()
        threading.Thread(target=udp_relay, args=(udp_1, drddr)).start()
        # threading.Thread(target=udp_relay, args=(udp_2, apddr,)).start()

        # tcp_pairing_server(tcp_server)
    except KeyboardInterrupt:
        print("Shutting down servers...")
    finally:
        # udp_1.close()
        # udp_2.close()

        # tcp_server.close()
        print("Bye...")
