import socket
from constants import *
from functions import *
from packet import generate_checksum
from multiprocessing import Process
from time import sleep

def process_func(socket, pkt, pktnum):
    """
    Handles timeouts
    """
    while True:
        sleep(timeout)
        socket.sendto(bytes(pkt), receiver_ip_port)
        print(f"Packet {pktnum} resent")

def main():
    """
    Main function where program execution begins
    """

    packet_size = int(input("Enter the packet size in bytes: "))
    packet_size = validate(packet_size, f"The packet size must be between {header_size + 1}"
                           f" and {max_size}! Re-enter: ", header_size + 1, max_size)

    packet_count = int(input("Enter the number of packets to be sent: "))
    packet_count = validate(packet_count, "The number of packets must be a positive integer! Re-enter: ", 1)
    print()

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(sender_ip_port)
    acks = [False] * packet_count

    packet_num = 1
    while packet_num <= packet_count:
        
        pkt = make_send_packet(packet_size, packet_num % 2)
        s.sendto(bytes(pkt), receiver_ip_port)
        
        t = Process(target = process_func, args = (s, pkt, packet_num))
        t.start()
        print(f"Packet {packet_num} sent")

        while True:
            m = s.recvfrom(max_size)
            msgs = m[0].decode().split()
            checksum = msgs[0]
            msg = int(msgs[1])

            if (msg == packet_num % 2) and (generate_checksum(msg) == checksum):
                t.terminate()
                acks[packet_num - 1] = True
                print(f"Acknowledgement {msg} for packet {packet_num} received\n")
                packet_num += 1
                break

    s.close()

if __name__ == "__main__":
    main()
