import socket

# domain:port

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

while True:
    print('Before .accept()')
    client_socket, addr = server_socket.accept()
    print('Com=nnection from', addr)

    while True:
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = 'Hello world\n'.encode()
            client_socket.send(response)

    print('outside inner while  loop')
    client_socket.close()
