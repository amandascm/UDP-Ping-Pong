import socket
import sys
import time
import numpy

def ping_pong(addr, n_times):
    # Create socket for client-server
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)

    rtts = []

    # Send data through UDP protocol n times
    for i in range(n_times):
        # Send ping
        send_data = "ping"
        sent_at = time.time_ns()
        s.sendto(send_data.encode('utf-8'), addr)

        print("\n------- Message number: ", (i+1), " -------\n")
        print("Client sent: ", send_data, "\n")

        try:
            # Receive pong
            data, address = s.recvfrom(4096)
            print("Client received: ", data.decode('utf-8'), "\n")
            
            # Count RTT and append to array
            recvd_at = time.time_ns()
            rtt = recvd_at - sent_at
            rtts.append(rtt)
            print("RTT: ", rtt, "ns\n")

        except socket.timeout:
            # Receive nothing
            print("Client received: null\n")
            print("Timeout!!! Try again... \n")
            continue

    #Send 'finish' message to server
    s.sendto('end connection'.encode('utf-8'), addr)

    # Close the socket
    s.close()

    return rtts

def main():
    # Check if it was well compiled and has 2 args
    if len(sys.argv) == 3:
        ip = sys.argv[1]
        port = int(sys.argv[2])
    else:
        print("Run like: python3 client_UDP.py serverIP serverPORT")
        exit(1)

    server_address = (ip, port)
    n_times = int(input('Type the amount of times you want to ping-pong: '))

    # Round Trip Time array
    rtts = ping_pong(server_address, n_times)

    # Ping Pong statistics
    print("Maximum RTT: %.2f ns" % max(rtts))
    print("Minimum RTT: %.2f ns" % min(rtts))
    print("Average RTT: %.2f ns" % numpy.mean(numpy.array(rtts)))
    print("Amount of sent pings: %d" % n_times)
    print("Amount of received pongs: %d" % len(rtts))

#-----------------------------------------------------
if __name__ == '__main__':
    main()