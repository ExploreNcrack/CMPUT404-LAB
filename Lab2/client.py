#!/usr/bin/env python3
"""
uses the socket library to connect to www.google.com and requests a page.
"""
import socket

# http port
Port = 80
Host = "www.google.com"
Buffer_Size = 1024

payload = """GET / HTTP/1.0
Host: {HOST}

""".format(HOST=Host)


def connect_socket(addr):
	(family, socketype, proto, cannoname, sockaddr) = addr
	try: 
		s = socket.socket(family, socketype, proto)
		s.connect(sockaddr)
		print("Connected")
		s.sendall(payload.encode())
		full_data = b""
		while True:
			data = s.recv(Buffer_Size)
			if not data:
				break
			full_data += data
		print(full_data)

	except:
		print("Did not connect")
		pass

	finally:
		s.close()

if __name__ == "__main__":
	addr_info = socket.getaddrinfo(Host, Port, proto=socket.SOL_TCP)
	addr = addr_info[0]
	connect_socket(addr)
	


