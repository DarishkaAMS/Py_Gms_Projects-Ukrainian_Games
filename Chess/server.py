import socket
from _thread import *
import sys

server = '192.168.1.97'  # ipconfig - to get the IPaddr IPv4 (Address +/- = Default Gateway)
port = 5555

# initialize the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # types of connections

try:
    sock.bind((server, port))
except socket.error as e:
    str(e)

sock.listen(2)  # open the post for 2 people and listen
print("I am waiting for the connection. Server has started")


def thread_client(conn):
    conn.send(str.encode('I have connected'))
    reply = ''
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')

            if not data:
                print('I have disconnected')
                break
            else:
                print(f'I have received: {reply}')
                print(f'I am sending: {reply}')

            conn.sendall(str.encode(reply))
        except:
            break

    print('I have lost connection...')
    conn.close()


while True:
    conn, addr = sock.accept()  # Accept the connection
    print(f'I have connected to: {addr}')

    start_new_thread(thread_client, (conn, ))





