import socket
import sys
import math

def ping_pong(addr, taxa):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(addr)

    # Receive n_times from client to calculate packet loss
    n_times, address = s.recvfrom(4096)
    dont_lose = math.floor(float(n_times)*(1 - taxa))

    for i in range(int(n_times)):
        print("------- Server is listening -------\n")
        data, address = s.recvfrom(4096)
        print("Server received: ", data.decode('utf-8'), "\n")

        # Artificially lose packets by not sending them
        if (i < dont_lose):
            send_data = "pong"
            s.sendto(send_data.encode('utf-8'), address)
        
        print("Server sent: ", send_data,"\n\n")
    
    # Close the socket
    s.close()

def main():
    # Check if it was well compiled and has 2 args
    if len(sys.argv) == 3:
        ip = sys.argv[1]
        port = int(sys.argv[2])
    else:
        print("Run like: python3 server_UDP.py serverIP serverPORT")
        exit(1)

    taxa_perda = float(input("Type the artificial loss rate(%) of your king kong: "))/100
    server_address = (ip, port)
    ping_pong(server_address, taxa_perda)



#-----------------------------------------------------
if __name__ == '__main__':
    main()