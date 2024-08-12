
sender_ip_port = ('localhost', 9999)
receiver_ip_port = ('localhost', 8888)
header_size = 9 # source port (2) + dest port (2) + 
                # length(2) + checksum(2) + seq(1)
max_size = 65527
timeout = 3