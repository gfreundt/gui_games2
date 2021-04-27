import socket
from _thread import *

class Main:
	def __init__(self):
		self.all_string = ' ' * 16


def new_client(client_id, client_conn):
    n=0
    while n < 500:
        data_from_client = client_conn.recv(256).decode('utf-8')  # block code
        #print(f'[SERVER] Data recieved from Client: {data_from_client}')
        data.all_string += data_from_client
        #print(n, client_id, data.all_string)
        client_conn.sendall(str.encode(data.all_string))
        n += 1
    conn.close()
	


# Init Network
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'localhost'
port = 54320
server_ip = socket.gethostbyname(server)

s.bind((server, port))
s.listen(5) # max number of connections
print('[SERVER] Waiting for a connection')


data = Main()

new_id = 0
while True:
    conn, addr = s.accept()  # block code
    conn.sendall(str(new_id).encode())
    print(f'[SERVER] Connected to: {addr}. Assigned ID: {new_id}')
    start_new_thread(new_client, (new_id, conn))
    new_id += 1