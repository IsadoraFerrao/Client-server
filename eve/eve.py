import socket, sys, struct
import threading

#SE PASSANDO POR SERVIDOR
def create_socket_server(HOST, PORT):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST,PORT))
    sock.listen(5)
    return sock

def send_file(name, conn, c_sock):
    
    
    filename = recv_message(conn)
    recv_file(c_sock, filename)
    
    with open(filename, 'a') as f:
        f.write('echo "SEU ARQUIVO FOI ALTERADO MUHAHAHA"\n')
    
    with open(filename, 'rb') as f:
        bytes_to_send = f.read(1024)
        while bytes_to_send:
            conn.send(bytes_to_send)
            bytes_to_send = f.read(1024)
    conn.close()

def recv_message(conn):
    
    buf = conn.recv(struct.calcsize('i'))[0]
    message = conn.recv(buf).decode()
    return message

#SE PASSANDO POR CLIENTE
def create_socket_client(HOST, PORT):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST,PORT))
    return sock

def recv_file(sock, filename):

    send_message(sock, filename)

    with open(filename, 'wb') as f:
        bytes_to_recv = sock.recv(1024)
        while bytes_to_recv:
            f.write(bytes_to_recv)
            bytes_to_recv = sock.recv(1024)
    sock.close()

def send_message(sock, message):

    sock.send(struct.pack('i',len(message)))
    sock.send(message.encode('UTF-8'))

if __name__ == '__main__':

    HOST = ''
    PORT_CLIENT = 8000 #porta para se conectar com o cliente
    PORT_SERVER = 9000 #porta para se conectar com o servidor
    
    c_sock = create_socket_client(HOST,PORT_SERVER) #sock para se passar por cliente
    s_sock = create_socket_server(HOST,PORT_CLIENT) #sock para se passar por servidor
    
    while True:
        conn, addr = s_sock.accept()
        t = threading.Thread(target=send_file, args=('send_file', conn, c_sock))
        t.start()
