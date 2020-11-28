import socket
from _thread import *
import sys

server = '192.168.1.97'  # ipconfig - to get the IPaddr IPv4 (Address +/- = Default Gateway)
port = 5555

# initialize the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # types of connections

try:
    sock.bind((server, port))
except socket.error as error:
    str(error)

sock.listen(2)  # open the post for 2 people and listen
print("I am waiting for the connection. Server has started")


def read_pos(str):
    str = str.split(',')
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0] + ',' + str[1])


pos = [(0, 0), (100, 100)]  # hold positions of the players


def thread_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    # conn.send(str.encode('I have connected'))
    reply = ''
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            # reply = data.decode('utf-8')
            pos[player] = data

            if not data:
                print('I have disconnected')
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print(f'I have received: {data}')
                print(f'I am sending: {reply}')

            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print('I have lost connection...')
    conn.close()


current_player = 0

while True:
    conn, addr = sock.accept()  # Accept the connection
    print(f'I have connected to: {addr}')

    start_new_thread(thread_client, (conn, current_player))
    current_player += 1  # Keep tracking which player we are using

