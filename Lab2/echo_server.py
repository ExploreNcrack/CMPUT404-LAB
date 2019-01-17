#!/usr/bin/env python3
"""
 listens for incoming connections and echos any received data.
"""
import socket

Host = ""
Port = 8001
Buffer_Size = 1024


def main():
	# create socket
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		s.bind((Host,Port))
		s.listen(1) # make socket listen

		# listen forever for connection
		while True:
			conn, addr = s.accept() # accept incoming connections	
			full_data = b""  # byte string
			while True:
				data = conn.recv(Buffer_Size)
				if not data:
					break
				full_data += data 
			# send all back to client
			conn.sendall(full_data)



if __name__ == "__main__":
	main()

