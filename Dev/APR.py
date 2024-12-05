import socket
import time
import threading

# Configuration for the navdata simulation
APP_HOST = "192.168.0.1"
FRLY_HOST = "192.168.0.15"
NAVDATA_PORT = 5554
CTRL_PORT = 5553
VID_PORT = 5555
def main():
    # Create a UDP socket
    navdata_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    navdata_socket.bind((APP_HOST, NAVDATA_PORT))# listen
    ctrl_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ctrl_socket.bind((APP_HOST, CTRL_PORT))# listen
    print(f"Lstn {APP_HOST}:{NAVDATA_PORT}")


    def AppToFrly():
        data = navdata_socket.recvfrom(1024)
        try:
            while data:
                ddd

    try:
        while True:
            # Create and send navdata packet
            # data, addr = navdata_socket.recvfrom(1024)
            # print ('d,a=',data, addr)

            navdata_packet = create_navdata_packet()
            navdata_socket.sendto(navdata_packet, (NAVDATA_HOST, NAVDATA_PORT))
            print(f"Sent navdata packet: {navdata_packet}")

            # Send packets at a fixed interval (e.g., 30 Hz)
            time.sleep(1 / 30.0)
    except KeyboardInterrupt:
        print("\nSimulation interrupted by user.")
    finally:
        navdata_socket.close()
        print("Navdata socket closed.")

if __name__ == "__main__":
    main()

