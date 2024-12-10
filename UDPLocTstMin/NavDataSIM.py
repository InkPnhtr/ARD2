import socket
import time

# Configuration for the navdata simulation
NAVDATA_HOST = "127.0.0.1"
NAVDATA_PORT = 5554

# Simulated navdata packet structure
def create_navdata_packet():
    return (
        b"\x00\x00\x00\x01"  # Header (example placeholder)
        b"\x00\x00\x00\x00"  # Drone state
        b"\x00\x00\x00\x0A"  # vx = 10
        b"\x00\x00\x00\x05"  # vy = 5
        b"\x00\x00\x00\x00"  # vz = 0
        b"\x00\x00\x05\xDC"  # altitude = 1500
        b"\x00\x00\x00\x0A"  # rotX = 0.0
        b"\x00\x00\x00\x05"  # rotY = 0.0
        b"\x00\x00\x22\xB8"  # rotZ = 45.0 (example packed value)
    )

def main():
    # Create a UDP socket
    navdata_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # navdata_socket.bind((NAVDATA_HOST, NAVDATA_PORT))
    # UdpSktLst[j].bind((LstnHost, UdpPrtLst)) # listen


    print(f"Simulating navdata packets to {NAVDATA_HOST}:{NAVDATA_PORT}")
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
