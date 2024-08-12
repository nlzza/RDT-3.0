import random
import string
import packet
from constants import *

def validate(n, err, lower, upper = 10000000):
    """"
    Ensures that lower <= n <= upper
    """
    while (n < lower or n > upper):
        n = int(input(err))
    return n

def make_send_packet(size, seq):
    """
    Makes sending packet
    """
    # Generate random message of apt size
    msg = generate_message(size - header_size)
    return packet.SenderPacket(seq, msg)

def make_receive_packet(msg):
    """
    Makes acknowledgement packet
    """
    return packet.Packet(msg)

def generate_message(len):
    """
    Generates a random message (string)
    of specified length
    """
    return ''.join(random.choices(string.ascii_letters, k = len))

def print_blank_line(print_count):
    """
    Used to give a blank line after every three prints
    """
    print_count += 1
    if print_count % 3 == 0:
        print()
    return print_count
