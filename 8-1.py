from socket import *
HOST = ''                                     #(1)
PORT = 11443                                  #(2)

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)     #(3)
s.bind((HOST, PORT))
s.listen(10)                                  #(4)

conn, addr = s.accept()
print 'Connected by', addr
data = conn.recv(1024)
while 1:
     command = raw_input("Enter shell command or quit: ")   #(5)
     conn.send(command)                                     #(6)
     if command == "quit": break 
     data = conn.recv(1024)                                 #(7)
     print data
conn.close()
