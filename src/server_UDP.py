import socket
import sys
import math
import random

def ping_pong(addr, taxa):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(addr)
    
    while True:
        print("------- Server is listening -------\n")
        data, address = s.recvfrom(4096)
        print("Server received: ", data.decode('utf-8'), "\n")

        # Probabilistically lose packets by not sending them
        randomValue = random.uniform(0.0, 1.0)
        if (randomValue <= (1.0 - taxa)):
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

    taxa_perda = float(input("Type the artificial loss rate(%) of your ping-pong: "))/100
    server_address = (ip, port)
    ping_pong(server_address, taxa_perda)



#-----------------------------------------------------
if __name__ == '__main__':
    main()