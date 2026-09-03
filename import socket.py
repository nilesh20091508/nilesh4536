import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.google.com", 80))
print("connected to gooogle")
