import socket, sys, struct
import threading

def create_socket(HOST, PORT):

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
    
    
    if len(sys.argv) < 2:
        print("Uso: "+sys.argv[0]+" <PORT> <arquivo>")
        print("PORT SERVIDOR ARQUIVO: 8000\nPORT SERVIDOR CONFIAVEL:50000")
        
        sys.exit()
    
    PORT = int(sys.argv[1])
    filename = sys.argv[2]
    
    sock = create_socket(HOST, PORT)
    if PORT == 50000:
        send_message(sock, 'cliente')
    recv_file(sock, filename)


