import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.IF_INET, socket.SOCK_STREAM)
        self.server = '192.168.1.97'
        self.port = 5555
        self.addr = (self.server, self.port)
        self.connect()



