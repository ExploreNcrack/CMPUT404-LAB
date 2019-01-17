#!/usr/bin/env python3
"""
 listens for incoming connections and echos any received data.
"""
import socket

# local host (standard loopback interface address)
Host = "127.0.0.1"
# port in listening for 
Port = 8001

try:
	# create socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Bind the socket to address. The socket must not already be bound.
	s.bind((Host, Port))
	# Enable a server to accept connections.
	s.listen()
	# conn is a new socket object usable to send and receive data on the connection
	# and address is the address bound to the socket on the other end of the connection.
	conn, addr = s.accept()
	if conn:
		print("Connected by", addr)
	while True:
		data = conn.recv(1024)
		print("The message receive: %s"%data.decode("utf-8"))
		if not data:
			s.close()
			break
		conn.sendall(data)
except socket.error as err:
	print("socket creation failed with error %s"%(err))

