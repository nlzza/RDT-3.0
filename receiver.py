import socket
from constants import *
from functions import *
from packet import generate_checksum
from time import sleep

def main():
    """
    Main function where program execution begins
    """
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(receiver_ip_port)

    count = 1
    print_count = 0 # Used to give a blank line after every three prints
    while True:

        m = s.recvfrom(max_size)
        msgs = m[0].decode().split()
        seq_num = msgs[0]
        checksum = msgs[1]
        msg = msgs[2]

        if generate_checksum(msg) != checksum:
            # Send negative acknowledgement
            expected_seq_num = count % 2
            neg = 0 if expected_seq_num else 1
            pkt = make_receive_packet(neg)
            s.sendto(bytes(pkt), sender_ip_port)
            print(f"Packet {count} corrupted. Negative acknowledgement sent")
            print_count = print_blank_line(print_count)
        else:
            # Packet received correctly
            # so send positive acknowledgement
            
            if int(seq_num) == (count % 2):
                print(f"Packet {count} successfully received")
                # sleep(5) # use for case of premature timeout
                pkt = make_receive_packet(seq_num)
                s.sendto(bytes(pkt), sender_ip_port)
                count += 1
                print_count = print_blank_line(print_count)
            else:
                print(f"Duplicate packet received. Acknowledgement sent")
                pkt = make_receive_packet(seq_num)
                s.sendto(bytes(pkt), sender_ip_port)
                print_count = print_blank_line(print_count)

    s.close()

if __name__ == "__main__":
    main()