#begin the scapy script.
#please change the file directory according to your requirement 
import scapy.all

#reading a pcap file
packets = scapy.all.rdpcap('Your Directory/.pcap')

# outputing the Destination and Source MAC
for packet in packets:
    print('-----------')
    print('src_mac:{0}'.format(packet.src))
    print('dst_mac:{0}'.format(packet.dst))

# IP plays
    ip =packet.payload

    print('src_ip:{0}'.format(ip.src))
    print('dst_ip:{0}'.format(ip.dst))
# Protocol Pays
    if ip.proto == 17:
        udp = ip.payload
        print('udp_sport:{0}'.format(udp.sport))
        print('udp_dport:{0}'.format(udp.dport))

    if ip.proto == 6:
        tcp = ip.payload
        print('tcp_sport:{0}'.format(tcp.sport))
        print('tcp_dport:{0}'.format(tcp.dport))

print('----------------\n')

-------------------------------------------------------------------------------------