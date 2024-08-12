from constants import *

class Packet:
    """
    Class representing a packet
    """
    def __init__(self, msg):
        """
        Class constructor
        """
        self.msg = msg
        self.checksum = generate_checksum(msg)
    
    def __bytes__(self):
        """
        Returns the object in bytes form
        """
        s = f'{self.checksum} {self.msg}'
        return bytes(s, encoding = "UTF-8")

class SenderPacket(Packet):
    """
    Class representing sender's packet
    """
    def __init__(self, seq, msg):
        """
        Class constructor
        """
        super().__init__(msg) # Calling parent constructor
        self.seq_num = seq
    
    def __bytes__(self):
        """
        Returns the object in bytes form
        """
        s = f'{self.seq_num} {self.checksum} {self.msg}'
        return bytes(s, encoding = "UTF-8")

def generate_checksum(msg):
    """
    Generate checksum
    """
    sum = 0
    for char in str(msg):
        sum += ord(char)
    if sum <= max_size:
        return bin(sum ^ 0b1111111111111111)
    else:
        return bin((sum - max_size) ^ 0b1111111111111111)