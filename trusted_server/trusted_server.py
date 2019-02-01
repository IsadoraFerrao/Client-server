import socket, sys, struct
import threading

def create_socket_server(HOST, PORT):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST,PORT))
    sock.listen(5)
    return sock

def send_file(name, conn):
    
    
    filename = recv_message(conn)
    
    with open(filename, 'rb') as f:
        bytes_to_send = f.read(1024)
        while bytes_to_send:
            conn.send(bytes_to_send)
            bytes_to_send = f.read(1024)
    conn.close()

def recv_digest(name, sock):

    filename = recv_message(sock)
    digest = recv_message(sock)
    with open(filename, 'w') as f:
        f.write(digest)
        
    """    
    with open(filename, 'wb') as f:
        bytes_to_recv = sock.recv(1024)
        while bytes_to_recv:
            f.write(bytes_to_recv)
            bytes_to_recv = sock.recv(1024)
    """
    sock.close()
    
def recv_message(conn):
    
    buf = conn.recv(struct.calcsize('i'))[0]
    message = conn.recv(buf).decode()
    return message

def send_message(sock, message):

    sock.send(struct.pack('i',len(message)))
    sock.send(message.encode('UTF-8'))

if __name__ == '__main__':

    HOST = ''
    PORT = 50000
    
    s_sock = create_socket_server(HOST,PORT) #sock para se passar por servidor
    
    while True:
        conn, addr = s_sock.accept()
        opt = recv_message(conn)
        if opt == 'cliente':
            t = threading.Thread(target=send_file, args=('send_file', conn))
            t.start()
        if opt == 'servidor':
            t = threading.Thread(target=recv_digest, args=('recv_digest', conn))
            t.start()
