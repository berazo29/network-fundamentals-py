import argparse
from sys import argv
import socket


parser = argparse.ArgumentParser(description="""This is a very basic client program""")
parser.add_argument('port', type=int, help='This is the port to connect to the server on', action='store')
args = parser.parse_args(argv[1:])

try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[S]: Server socket created\ninfo: {}".format(ss))
except socket.error as error:
    print("Server socket error: {}".format(error))
    exit()

server_addr = ('', args.port)
ss.bind(server_addr)
ss.listen(1)

# print server info
host = socket.gethostname()
print("[S]: Server hostname is {}".format(host))
localhost_ip = socket.gethostbyname(host)
print("[S]: Server IP address is {}".format(localhost_ip))
print("[S]: Server port number is {}".format(args.port))

# accept a client
csockid, addr = ss.accept()
print("[S]: Got a connection request from a client at {}".format(addr))

with csockid:
    while True:
        data = csockid.recv(512)
        data = data.decode('utf-8')
        print(data)
        if not data:
            break
        csockid.sendall(data.encode('utf-8'))

ss.close()
exit()