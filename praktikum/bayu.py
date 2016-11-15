from socket import socket, AF_INET,SOCK_STREAM

class Bayu(object):
	def isOpen(self,IPADD,PORT):
		s = socket(AF_INET,SOCK_STREAM)
		s.settimeout(5)
		return s.connect_ex((IPADD,PORT))