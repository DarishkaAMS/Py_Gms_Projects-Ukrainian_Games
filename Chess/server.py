import socket
from _thread import *
import sys

server = ''
port = 5555

# initialize the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # types of connections

try:
    sock.bind((server, port))
except socket.error as e:
    str(e)

sock.listen(2)  # open the post for 2 people and listen
print("We are waiting  fot the connection. Server has started")


def thread_client(conn):
    reply = ''
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')

            if not data:
                print('Disconnected')
                break
            else:
                print(f'Received: {reply}')
                print(f'Sending: {reply}')

            conn.sendall(str.encode(reply))
        except:
            break


while True:
    conn, addr = sock.accept()  # Accept the connection
    print(f'Connected to: {addr}')

    start_new_thread(thread_client, (conn, ))





