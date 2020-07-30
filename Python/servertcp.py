import logging
from datetime import datetime
import socket
from threading import Thread


# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        logging.info("[+] New server socket thread started")

    def run(self):
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                continue
            # logging.info(''.join([str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), ' ', str(data)]))
            print(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), "[", self.ip, "] ", data)
            #conn.send(data)  # echo


# Multithreaded Python server : TCP Server Socket Program Stub
# logging.basicConfig(filename='gateway-tcp.log', level=logging.INFO)
TCP_IP = '0.0.0.0'
TCP_PORT = 8006
BUFFER_SIZE = 1020  # Usually 1024, but we need quick response

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpServer.listen(4)
    # logging.info("Multithreaded Python server : Waiting for connections from TCP clients...")
    print("Multithreaded Python server : Waiting for connections from TCP clients...")
    (conn, (ip, port)) = tcpServer.accept()
    newthread = ClientThread(ip, port)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()