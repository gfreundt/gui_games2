import socket
import gui_games_network as network
from _thread import *

class Server:
	def __init__(self):
		self.data = '  ' * 64
		self.net = network.NetworkServer(max_conn=2)
		self.active_connections = []


def new_client_thread(client_id, client_conn):
    while True:
        data_from_client = client_conn.recv(256).decode('utf-8')  # block code
        if data_from_client == 'wait':
        	pass
        elif data_from_client == 'gameover':
        	break
        else:
        	stream.data = data_from_client[:]
        client_conn.sendall(str.encode(stream.data))
    client_conn.close()
    return client_id
	

def main():
	print(f'[GUI GAMES SERVER] Active in Local IP {stream.net.server_ip}')
	print('[GUI GAMES SERVER] Waiting for a connection.')

	new_id = 0
	while True:
	    conn, addr = stream.net.sock.accept()  # block code
	    conn.sendall(str(new_id).encode())
	    print(f'[GUI GAMES SERVER] Connected to: {addr}. Assigned ID: {new_id}')
	    stream.active_connections.append([new_id, addr, conn])
	    thread_id = start_new_thread(new_client_thread, (new_id, conn))
	    new_id += 1
	print(f'[GUI GAMES SERVER] Disconnected from ID: {thread_id}')


stream = Server()
main()