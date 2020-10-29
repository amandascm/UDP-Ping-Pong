
# UDP Ping Pong

This is a project developed by [mesps](github.com/mesps), [amandascm](github.com/amandascm), [tta13](github.com/tta13), [Luis-Alves2](github.com/Luis-Alves2) and [Washhh](github.com/Washhh)   for the 'Infraestrutura da comunicação' (Communication Infrastructure) discipline of CIn-UFPE. 
The client side determines the number of pings that will be sent to the server and the server side determines the artificial loss rate (to simulate the loss of messages in a communication with unreliable data transfer, since it is based on the User Datagram Protocol).

### Execution
Server execution:
```
$ python3 server_UDP.py serverIP serverPort
```
Client execution:
```
$ python3 client_UDP.py serverIP serverPort
```
