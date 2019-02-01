import socket, sys, struct
import threading
import hashlib

def sha256_checksum(filename, sock, block_size=65536):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            sha256.update(block)
    digest = sha256.hexdigest()
    
    print("digest: "+ digest)
    send_message(sock, filename+'.sha256')
    send_message(sock, digest)

def create_socket(HOST, PORT):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST,PORT))
    sock.listen(5)
    return sock

def send_file(name, conn):
    
    
    filename = recv_message(conn)
    
    #GERA SHA256 DO ARQUIVO E MANDA PRO SERVIDOR CONFIAVEL
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('', 50000))
    send_message(sock, 'servidor')
    sha256_checksum(filename, sock)
    sock.close()
    
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

def send_message(sock, message):

    sock.send(struct.pack('i',len(message)))
    sock.send(message.encode('UTF-8'))
if __name__ == '__main__':
    
    HOST = ''
    PORT = 9000

    sock = create_socket(HOST, PORT)
    
    while True:
        conn, addr = sock.accept()
        print(addr)
        t = threading.Thread(target=send_file, args = ('send_file',conn))
        t.start()
