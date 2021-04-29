import socket


class NetworkServer:
    def __init__(self, max_conn):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_ip = socket.gethostbyname(socket.gethostname()) 
        self.server_port = 54320
        self.addr = (self.server_ip, self.server_port)
        self.sock.bind((self.server_ip, self.server_port))
        self.sock.listen(max_conn) # max number of connections



class NetworkClient:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip_list = ['192.168.1.20', '192.168.1.3']
        self.port = 54320
        for self.server_ip in ip_list:
            print(f'[CLIENT] Attempting to connect to Server at {self.server_ip}')
            try:
                self.addr = (self.server_ip, self.port)
                self.id = self.connect()
                print('[CLIENT] Server Connection Successful.')
                break
            except:
                print('[CLIENT] Server Connection Error.')


    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(128).decode()


