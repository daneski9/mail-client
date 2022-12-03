
#Dane Coleman 
from socket import *

msg = "\r\n I love Computer Networks"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.csus.edu",25)
# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
recv = clientSocket.recv(1024)
print (recv)
if recv[:3] != '220':
    print ('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
print (recv1)
if recv1[:3] != '250':
    print ('250 reply not received from server.')
 
# Send MAIL FROM command and print server response.
mailcommand = 'MAIL FROM: realJoeBiden@gmail.com\r\n'
clientSocket.send(mailcommand.encode())
recv2 = clientSocket.recv(1024)
print (recv2)
if recv2[:3] !='250':
    print('250 reply not received from server.')
# Send RCPT TO command and print server response. 
RCPTcommand = 'RCPT TO: <danecoleman@csus.edu>\r\n'
clientSocket.send(RCPTcommand.encode())
recv3 = clientSocket.recv(1024)
print (recv3)
if recv3[:3] !='250':
    print('250 reply not received from server.')
# Send DATA command and print server response. 
DATAcommand = 'DATA\r\n'
clientSocket.send(DATAcommand.encode())
recv4 = clientSocket.recv(1024)
print (recv4)
if recv4[:3] !='354':
    print('354 reply not received from server.')
# Send message data.
mymsg = "hello, how are you?"
clientSocket.send(mymsg.encode())
clientSocket.send(endmsg.encode())  #ends with a single period.
recv5 = clientSocket.recv(1024)
print(recv5.decode())
if recv5[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
QUITcommand = 'QUIT\r\n'
clientSocket.send(QUITcommand.encode())
recv6 = clientSocket.recv(1024)
print (recv6)
