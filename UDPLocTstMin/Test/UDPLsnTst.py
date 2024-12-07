import socket
import time


# Function to relay UDP data (dummy example)
def udp_relay(udp_server, pair_id):
    print(f"UDP Relay started for Pair ID: {pair_id}")
    try:
        while True:
            # Dummy data to send
            data = f"HI From UDPLsnTst".encode()
            # Send data to a specific address
            udp_server.sendto(data, ('127.0.0.1', 5554))
            print(f"Sent: {data}")
            # Send packets at a fixed interval (e.g., 30 Hz)
            time.sleep(1 / 4.0)

    except Exception as e:
        print(f"UDP Relay for Pair ID = {pair_id} terminated: {e}")

# Main function to run the server
if __name__ == "__main__":
    # Create the UDP server socket
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("UDP server initialized.")

    # Bind to a local port (if needed)
    udp_server.bind(('127.0.0.2', 5554))

    try:
        udp_relay(udp_server, 23)
    except KeyboardInterrupt:
        print("Shutting down servers...")
    finally:
        udp_server.close()
