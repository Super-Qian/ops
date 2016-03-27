#!/usr/bin/python

import socket
host = "localhost"
port = 2222


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        mesg = raw_input("Input what to search or press Ctrl - C to quit: ")
        sock.send(mesg.strip())
        print sock.recv(1024)
        sock.close()
    except Exception as e:
        print e
        exit(1)

if __name__ == "__main__":
    while True:
        main()
