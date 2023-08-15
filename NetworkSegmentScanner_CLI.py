

import socket
from datetime import datetime

net_addr=input("Enter the address of the network segment ###.###.###.###:")
net_addr_split=net_addr.split('.')
delimiter='.'

net_addr_intermediate=net_addr_split[0] + delimiter +net_addr_split[1] + delimiter + net_addr_split[2] + delimiter

net_segment_start=int(input("Enter network segment start address .###"))
net_segment_end=int(input("Enter network segment end address .###"))
net_segment_end= net_segment_end + 1
time_Start=datetime.now()


# Special "Formula" to see if address is alive
def scan_addr(targetAddress):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    is_aliveResult=sock.connect_ex((targetAddress,135))

    if is_aliveResult==0:
        return 1
    else:
        return 0

# Iterate through address to see if alive
def sweepAddr():
    for ip in range (net_segment_start,net_segment_end):
        targetAddress=net_addr_intermediate + str(ip)
        if (scan_addr(targetAddress)): #check for response to target address
            print(targetAddress, "is alive")

sweepAddr() # Iterative loop through the address range.
time_End=datetime.now()
time_Total=time_End - time_Start
print ("Scanning completed in: ",time_Total)



