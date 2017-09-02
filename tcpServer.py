#!/usr/bin/python3
# __autor__ == '__Ivanoel__'
# Servidor TCP

import socket

def Main():

	host = '127.0.0.1'
	port = 5000

	s = socket.socket()
	s.bind((host, port))

	s.listen(1)
	c, addr = s.accept()

	print("Conexão de: " + str(addr))

	while True:
		data = c.recv(1024).decode('utf-8')

		if not data:
			break
		print("Do usuario conectado: " + data)

		data = data.upper()

		print("Transmissão: " + data)
		c.send(data.encode('utf-8'))
	c.close()

if __name__ == '__main__':
	Main()
