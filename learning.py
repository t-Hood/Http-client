import socket

ip_target = input("Enter host: ")
ip_port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_target, ip_port))
s.send(f"GET / HTTP/1.0\r\nHost: {ip_target}\r\n\r\n".encode())

response = s.recv(4096)
print(response.decode())
s.close()
input("Press enter to quit")