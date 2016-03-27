# coding=utf-8
import socket

port = 2222
list = 1
dict = {
    'foo': 2014,
    'com': 'apple',
    'tel': 110,
    'addr': 'Mark'
}


def send_client(client, address):
    try:
        client.settimeout(500)
        buf = client.recv(1024)
        if buf in dict.keys():
            client.send(str(dict[buf]))
        else:
            client.send("There's no %s." % buf)
    except socket.timeout:
        print 'time out'
    client.close()


def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    sock.listen(list)

    while True:
        client, address = sock.accept()
        send_client(client, address)

if __name__ == "__main__":
    print 'Server is running on port %d; press Ctrl-C to terminate.' % port
    main()
