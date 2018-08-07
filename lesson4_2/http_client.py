import socket
request = 'GET /CScourses/03b1_minimal.html HTTP/1.1\r\nHost: indstudy1.org\r\n\r\n'
"""
GET /CScourses/03b1_minimal.html HTTP/1.1
Host: indstudy1.org

"""
sock = socket.create_connection(('69.89.31.113', 80))
sock.sendall(request.encode(encoding='utf-8'))
data = sock.recv(1000)
sock.close()
print(data.decode(encoding='utf-8'))